from django.shortcuts import render
from places.models import Place
import json


def show_main_page(request):
    data = []
    places = Place.objects.all()
    for place in places:

        dict_for_place = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.place_id,
                "detailsUrl": place.details_url
            }
        }
        data.append(dict_for_place)
    places_list=json.dumps(data)
    print(data)

    return render(request, 'main_page.html', context={"data":places_list})



