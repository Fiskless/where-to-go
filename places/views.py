from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Place
# Create your views here.


def show_place_page(request, place_id):

    place = get_object_or_404(Place, id=place_id)

    images_url = [image.img.url for image in place.images.all()]

    context = {
        "title": place.title,
        "imgs": images_url,
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lon
        }
    }

    return JsonResponse(context,
                        safe=False,
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})
