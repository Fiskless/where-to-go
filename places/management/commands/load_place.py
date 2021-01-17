from django.core.management.base import BaseCommand
from places.models import *
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
            title = place_data['title'],
            description_short=place_data['description_short'],
            description_long=place_data['description_long'],
            lat=place_data['coordinates']['lat'],
            lon=place_data['coordinates']['lng']
        )
        # new_picture = place_data.img.save('https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/35cbdddf2799337d8b571d141edec616.JPG')
        for picture_index, picture_url in enumerate(place_data['imgs']):
            response_1 = requests.get(place_data['imgs'][picture_index])
            image = Image.open(BytesIO(response_1.content))
            image.save(f"media/{place_data['imgs'][picture_index].split('/')[-1]}", save=True)
            new_image = new_place.image_set.create()
            new_image.img = f"{place_data['imgs'][picture_index].split('/')[-1]}"
            new_image.save()


        # >> > i = Image.open(BytesIO(r1.content))
        # >> > i.save('new_photo.jpg', save=True)
        # for picture in r2:
        #     ...
        #     print(picture.split('/')[-1])
        # p.image_set.create()
        # image1.img = 'new_photo.jpg'
        # >> > image1.save()

    def add_arguments(self, parser):
        parser.add_argument(
            'link',
            help='add link as an argument'
        )
