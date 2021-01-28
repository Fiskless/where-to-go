from django.core.management.base import BaseCommand
from places.models import Place
import requests
from PIL import Image
from io import BytesIO


class Command(BaseCommand):
    help = 'This command allow to add places on the map'

    def handle(self, *args, **options):
        response = requests.get(f"{options['link']}")
        response.raise_for_status()
        place_data = response.json()
        new_place, created = Place.objects.get_or_create(
            title=place_data['title'],
            short_description=place_data['description_short'],
            long_description=place_data['description_long'],
            lat=place_data['coordinates']['lat'],
            lon=place_data['coordinates']['lng']
        )

        for picture_index, picture_url in enumerate(place_data['imgs']):
            response_1 = requests.get(place_data['imgs'][picture_index])
            response_1.raise_for_status()
            image = Image.open(BytesIO(response_1.content))
            image.save(f"media/{place_data['imgs'][picture_index].split('/')[-1]}", save=True)
            new_image = new_place.place_images.create()
            new_image.img = f"{place_data['imgs'][picture_index].split('/')[-1]}"
            new_image.save()

    def add_arguments(self, parser):
        parser.add_argument(
            'link',
            help='add link as an argument'
        )
