API_KEY = 'AIzaSyCVHHlqVDOj477LhigLszsbloDISYHXClI'

import requests
import csv

# Replace 'YOUR_API_KEY' with your actual Google Places API key
LOCATION = 'Pretoria'
SEARCH_TERM = 'Shoprite'

def get_places(api_key, location, search_term):
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={search_term}+in+{location}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def get_place_details(api_key, place_id):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def format_opening_hours(hours_list):
    formatted_hours = []
    for hours in hours_list:
        parts = hours.split(': ')
        if len(parts) == 2:
            day, time_range = parts
            formatted_hours.append(time_range.replace('\u202f', '').replace('\u2009', ''))
    return formatted_hours

def main():
    data = get_places(API_KEY, LOCATION, SEARCH_TERM)
    scrapped_data = []
    if data:
        results = data.get('results', [])
        for place in results:
            name = place.get('name')
            address = place.get('formatted_address')
            place_id = place.get('place_id')
            latitude = place.get('geometry', {}).get('location', {}).get('lat')
            longitude = place.get('geometry', {}).get('location', {}).get('lng')
            combined_coordinates = f"{latitude},{longitude}"
            category = place.get('types', [])

            # Get place details for additional information
            details = get_place_details(API_KEY, place_id)
            if details:
                result = details.get('result', {})
                opening_hours = result.get('opening_hours', {}).get('weekday_text', 'No data available')
                if opening_hours != 'No data available':
                    opening_hours = format_opening_hours(opening_hours)
                reviews = result.get('reviews', [])
                review_points = result.get('rating', 'No data available')
                total_reviews = result.get('user_ratings_total', 'No data available')
                phone = result.get('formatted_phone_number', 'No data available')
                website = result.get('website', 'No data available')
                page_url = result.get('url', 'No data available')
            else:
                opening_hours = 'No data available'
                reviews = []
                review_points = 'No data available'
                total_reviews = 'No data available'
                phone = 'No data available'
                website = 'No data available'
                page_url = 'No data available'

            scrapped_data.append({
                'Name': name,
                'Address': address,
                'Opening Hours': opening_hours,
                'Reviews': reviews,
                'Review Points': review_points,
                'Total Reviews': total_reviews,
                'Phone': phone,
                'Website': website,
                'Google ID': place_id,
                'Latitude': latitude,
                'Longitude': longitude,
                'Combined Coordinates': combined_coordinates,
                'Category': category,
                'Page URL': page_url,
            })
    
    else:
        print("No data found.")
    
    with open('scrapped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'Name', 'Address', 'Opening Hours', 'Reviews', 'Review Points', 'Total Reviews',
            'Phone', 'Website', 'Google ID', 'Latitude', 'Longitude', 'Combined Coordinates',
            'Category', 'Page URL'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in scrapped_data:
            writer.writerow(entry) 

if __name__ == "__main__":
    main()
