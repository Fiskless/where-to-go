from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Place
# Create your views here.


def show_place_page(request, post_id):

    place =get_object_or_404(Place, id=post_id)

    images_url = []
    for image in place.image_set.all():
        image_url = image.img.url
        images_url.append(image_url)

    place_data = {
        "title": place.title,
        "imgs":images_url,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat":place.lat,
            "lng":place.lon
        }
    }

    return JsonResponse(place_data,
                        safe=False,
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})