"""
Souleyman Mahamat
CIS-131
04/15/2025

This script uses the Shodan API to search for devices in Arizona with
"in-tank inventory" somewhere in their metadata. It filters the results and
prints selected information fields.
"""

import shodan
import json

# The API key
API_KEY = "HlcQg6bwaPefM3fOM8jPG94GcoBXZR5W"

# Initialize the API
api = shodan.Shodan(API_KEY)

# Define the search query
query = "'in-tank inventory' state:'AZ'"

try:
    # Perform the search
    results = api.search(query)

    print(f"Total results found: {results['total']}\n")

    for match in results['matches']:
        banner = match.get("data", "").strip()

        # Check if banner contains the expected section
        if "IN-TANK INVENTORY" in banner:
            # Optional cleanup: remove non-printable chars
            clean_banner = ''.join(c for c in banner if c.isprintable() or c in "\n\r\t")
            
            print(clean_banner)

except shodan.APIError as e:
    print(f"Shodan API Error: {e}")