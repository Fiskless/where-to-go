from django.shortcuts import render
from places.models import Place
from django.urls import reverse



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
                "placeId": place.slug,
                "detailsUrl": reverse("place-page", args=[place.id])
            }
        }
        data.append(dict_for_place)

    places_dict = {
        "type": "FeatureCollection",
        "features": data
    }

    return render(request, 'main_page.html', context={"data":places_dict})


