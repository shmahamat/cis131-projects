"""
Souleyman Mahamat
CIS-131
04/15/2025

Shodan query for AZ in-tank inventory devices.
Emails report via Gmail and sends SMS via Twilio.
"""

import shodan
import json
import ezgmail
from ezgmail import EZGmailException
from twilio.rest import Client

# Config
API_KEY    = "HlcQg6bwaPefM3fOM8jPG94GcoBXZR5W"
QUERY      = "'in-tank inventory' state:'AZ'"

FROM_EMAIL = " "
TO_EMAIL   = " "

TWILIO_SID   = " "
TWILIO_TOKEN = " "
TWILIO_FROM  = "+1xxxxxxxxxx"
TWILIO_TO    = "+1xxxxxxxxxx"

# Initialize APIs
api = shodan.Shodan(API_KEY)
twilio_client = Client(TWILIO_SID, TWILIO_TOKEN)

def main():
    # Initialize Gmail using credentials.json
    try:
        ezgmail.init()
    except EZGmailException as e:
        print(f"Gmail init error: {e}")
        print("Make sure credentials.json is present and run ezgmail.init() manually.")
        return

    try:
        # Search Shodan
        results = api.search(QUERY)
        print(f"Total found: {results.get('total', 0)}")

        lines = []
        phoenix = False

        for match in results.get('matches', []):
            banner = match.get('data', '').strip()
            if 'IN-TANK INVENTORY' in banner:
                clean = ''.join(
                    c for c in banner
                    if c.isprintable() or c in '\n\r\t'
                )
                print(clean)
                lines.append(clean)

                city = match.get('location', {}).get('city', '')
                if city.lower() == 'phoenix':
                    phoenix = True

        report = "\r\n\n".join(lines) or "No entries found."

        # Send email
        ezgmail.send(
            TO_EMAIL,
            'Internet Gas Gauges in AZ',
            report,
        )
        print('Email sent')

        # Send SMS confirmation
        try:
            sms = twilio_client.messages.create(
                body='Report delivered via email',
                from_=TWILIO_FROM,
                to=TWILIO_TO
            )
            print('SMS SID:', sms.sid)
        except Exception as e:
            print('Twilio authentication error:', e)
            return

        # Send Phoenix alert if needed
        if phoenix:
            try:
                alert = twilio_client.messages.create(
                    body='ALERT: Gas gauge in Phoenix, AZ',
                    from_=TWILIO_FROM,
                    to=TWILIO_TO
                )
                print('Alert SID:', alert.sid)
            except Exception as e:
                print('Twilio alert error:', e)

    except shodan.APIError as e:
        print('Shodan error:', e)

if __name__ == '__main__':
    main()
