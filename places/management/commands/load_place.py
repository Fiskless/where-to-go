from django.core.management.base import BaseCommand
from places.models import Place
import requests
from PIL import Image
from io import BytesIO


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

        for picture_index, picture_url in enumerate(raw_place['imgs']):
            picture_response = requests.get(raw_place['imgs'][picture_index])
            picture_response.raise_for_status()
            image = Image.open(BytesIO(picture_response.content))
            image.save(f"media/{raw_place['imgs'][picture_index].split('/')[-1]}", save=True)
            new_image = place.images.create()
            new_image.img = f"{raw_place['imgs'][picture_index].split('/')[-1]}"
            new_image.save()

    def add_arguments(self, parser):
        parser.add_argument(
            'link',
            help='add link as an argument'
        )
