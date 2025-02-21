import googlemaps
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import os

def get_email_from_website(url):
    """
    Scrape a website URL for an email address.
    Returns the first found email, or an empty string if none is found.
    """
    try:
        response = requests.get(url, timeout=10)
        html = response.text
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)
        return emails[0] if emails else ""
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def sanitize_filename(name):
    """
    Remove characters not allowed in filenames.
    """
    return "".join(c for c in name if c not in r'\/:*?"<>|')

def search_businesses(gmaps, search_query):
    """
    Search businesses using the Google Places API with pagination.
    """
    results = []
    page_token = None
    while True:
        if page_token:
            places_result = gmaps.places(query=search_query, page_token=page_token)
        else:
            places_result = gmaps.places(query=search_query)
        results.extend(places_result.get('results', []))
        page_token = places_result.get('next_page_token')
        if page_token:
            time.sleep(2)  # wait for the token to become valid
        else:
            break
    return results

def get_business_details(gmaps, place_id):
    """
    Retrieve detailed business information using the Place Details API.
    """
    details_response = gmaps.place(place_id=place_id)
    return details_response.get('result', {})

def main():
    # Initialize Google Maps client
    api_key = input("Enter your Google Maps API Key: ").strip()
    gmaps = googlemaps.Client(key=api_key)
    
    # Get the location and the path to the text file containing business categories.
    location = input("Enter a location (City, Zipcode or State): ").strip()
    file_path = input("Enter the path to your text file with business categories (one per line): ").strip()
    
    # Read business categories from the text file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            queries = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    master_data = []
    
    # Process each business category
    for query in queries:
        search_query = f"{query} in {location}"
        print(f"\nSearching for businesses with query: '{search_query}'")
        results = search_businesses(gmaps, search_query)
        print(f"Found {len(results)} businesses for category '{query}'.")
        
        business_data = []
        for place in results:
            place_id = place['place_id']
            details = get_business_details(gmaps, place_id)
            name = details.get('name', '')
            address = details.get('formatted_address', '')
            phone = details.get('formatted_phone_number', '')
            website = details.get('website', '')
            email = ""
            
            # If a website is provided, attempt to scrape for an email address.
            if website:
                print(f"Scraping website for {name}: {website}")
                email = get_email_from_website(website)
                time.sleep(1)
            
            row = {
                "Category": query,
                "Name": name,
                "Address": address,
                "Phone": phone,
                "Website": website,
                "Email": email
            }
            business_data.append(row)
            master_data.append(row)
        
        # Save results for this business category into its own Excel file.
        df = pd.DataFrame(business_data)
        safe_query = sanitize_filename(query)
        output_file = f"business_data_{safe_query}.xlsx"
        df.to_excel(output_file, index=False)
        print(f"Data for category '{query}' saved to {output_file}.")
    
    # Save all the aggregated data into a master Excel file.
    df_master = pd.DataFrame(master_data)
    master_file = "master_business_data.xlsx"
    df_master.to_excel(master_file, index=False)
    print(f"\nMaster file saved to {master_file}.")

if __name__ == "__main__":
    main()
