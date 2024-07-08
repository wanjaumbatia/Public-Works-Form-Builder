from django.shortcuts import render
from scrapper.utils import get_place_details, get_places_by_query
# Create your views here.
def query_data(request):
    if request.method == "POST":
        query = request.POST['query']
        query_arr = query.split(',')        
        for item in query_arr:
            places = get_places_by_query(query)
            if places:
                for place in places:
                    place_id = place.get('place_id')
                    details = get_place_details(place_id)
                    if details:
                        print(details)
            else:
                print('No data found for ', item)
                
                
    return render(request, 'scrapper/query.html')
