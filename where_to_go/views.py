from django.shortcuts import render
from places.models import Place
from django.urls import reverse


def show_main_page(request):
    place_features = []
    places = Place.objects.all()

    for place in places:

        place_serialized = {
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
        place_features.append(place_serialized)

    places_serialized = {
        "type": "FeatureCollection",
        "features": place_features
    }

    return render(request, 'main_page.html', context={"places": places_serialized})
