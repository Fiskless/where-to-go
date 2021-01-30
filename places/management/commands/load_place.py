from django.core.management.base import BaseCommand
from places.models import Place
import requests
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse, unquote


class Command(BaseCommand):
    help = 'This command allow to add places on the map'

    def handle(self, *args, **options):
        place_response = requests.get(f"{options['link']}")
        place_response.raise_for_status()
        raw_place = place_response.json()
        place, created = Place.objects.get_or_create(
            title=raw_place['title'],
            defaults={
                'short_description': raw_place['description_short'],
                'long_description': raw_place['description_long'],
                'lat': raw_place['coordinates']['lat'],
                'lon': raw_place['coordinates']['lng']
            }
        )

        for picture_url in raw_place['imgs']:
            picture_response = requests.get(picture_url)
            picture_response.raise_for_status()
            image = Image.open(BytesIO(picture_response.content))
            image_name = urlparse(picture_url).path.split('/')[-1]
            image.save(f"media/{image_name}", save=True)
            new_image = place.images.create(img=image_name)

    # >> > u = urlparse(
    #     "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/79403aa7fa5d1d2e06eabe8827e8c96e.jpg")
    # >> > u
    # ParseResult(scheme='https', netloc='raw.githubusercontent.com',
    #             path='/devmanorg/where-to-go-places/master/media/79403aa7fa5d1d2e06eabe8827e8c96e.jpg', params='',
    #             query='', fragment='')
    # >> > unquote(u.path.split('/')[-1])
    # '79403aa7fa5d1d2e06eabe8827e8c96e.jpg'

    def add_arguments(self, parser):
        parser.add_argument(
            'link',
            help='add link as an argument'
        )
