import requests

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'AIzaSyAk5UwwQ6TZyJ1pER_5bJhiUkUWWreLFSY'
BASE_URL = 'https://maps.googleapis.com/maps/api/place'

def get_place_details(place_id):
    # Define the fields you want to retrieve
    fields = 'name,rating,review,user_ratings_total,formatted_address,geometry,international_phone_number,opening_hours,website,place_id,types,formatted_phone_number'

    # Make a request to the Place Details endpoint
    response = requests.get(f'{BASE_URL}/details/json', params={
        'place_id': place_id,
        'fields': fields,
        'key': API_KEY
    })

    if response.status_code == 200:
        data = response.json().get('result', {})
        place_details = {
            'title': data.get('name'),
            'reviews': [review.get('text') for review in data.get('reviews', [])],
            'review_points': data.get('rating'),
            'total_reviews': data.get('user_ratings_total'),
            'address': data.get('formatted_address'),
            'phone': data.get('international_phone_number', data.get('formatted_phone_number')),
            'website': data.get('website'),
            'working_hours': data.get('opening_hours', {}).get('weekday_text', []),
            'google_id': data.get('place_id'),
            'latitude': data.get('geometry', {}).get('location', {}).get('lat'),
            'longitude': data.get('geometry', {}).get('location', {}).get('lng'),
            'combined_coordinates': f"{data.get('geometry', {}).get('location', {}).get('lat')}, {data.get('geometry', {}).get('location', {}).get('lng')}",
            'category': data.get('types'),
            'page_url': f'https://www.google.com/maps/place/?q=place_id:{data.get("place_id")}'
        }
        return place_details
    else:
        print('Failed to retrieve place details')
        return None

def get_places_by_query(query, location='0,0', radius=1000):
    # Make a request to the Places Text Search endpoint
    response = requests.get(f'{BASE_URL}/textsearch/json', params={
        'query': query,
        'location': location,
        'radius': radius,
        'key': API_KEY
    })  
    print(response.json())
    if response.status_code == 200:
        data = response.json().get('results', [])
        return data
    else:
        print('Failed to retrieve places')
        return None

if __name__ == "__main__":
    query = 'restaurants in New York'
    places = get_places_by_query(query)

    if places:
        for place in places:
            place_id = place.get('place_id')
            details = get_place_details(place_id)
            if details:
                print(details)
    else:
        print('No places found')
