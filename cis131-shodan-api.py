"""
Souleyman Mahamat
CIS-131
04/15/2025

This script uses the Shodan API to search for devices in Arizona with
"in-tank inventory" somewhere in their metadata. It filters the results and
prints selected information fields for each match as no prior template was
provided.
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

    for result in results['matches']:
        ip_str = result.get('ip_str', 'N/A')
        org = result.get('org', 'N/A')
        location = result.get('location', {})
        city = location.get('city', 'N/A')
        country_name = location.get('country_name', 'N/A')
        port = result.get('port', 'N/A')
        product = result.get('product', 'N/A')
        data_snippet = result.get('data', '').strip().split('\n')[0]  # Only first line

        print(f"IP Address: {ip_str}")
        print(f"Organization: {org}")
        print(f"City: {city}")
        print(f"Country: {country_name}")
        print(f"Port: {port}")
        print(f"Product: {product}")
        print(f"Data: {data_snippet}")
        print("-" * 40)

except shodan.APIError as e:
    print(f"Shodan API Error: {e}")