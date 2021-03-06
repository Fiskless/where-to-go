from django.core.management.base import BaseCommand
from places.models import Place
import requests
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse, unquote
import os


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
            image_path = urlparse(picture_url).path
            image_name = unquote(os.path.split(image_path)[1])
            image.save(f"media/{image_name}")
            place.images.create(img=image_name)

    def add_arguments(self, parser):
        parser.add_argument(
            'link',
            help='add link as an argument'
        )
