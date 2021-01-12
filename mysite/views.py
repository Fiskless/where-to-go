from django.shortcuts import render
from places.models import Place
from django.http import HttpResponseRedirect
from django.urls import reverse
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
                "detailsUrl": reverse("place-page", args=[place.id])
            }
        }
        data.append(dict_for_place)
    places_list=json.dumps(data, indent= 2, ensure_ascii=True, default=str)

    return render(request, 'main_page.html', context={"data":places_list})



