from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):

    title = models.CharField('Название места', max_length=200)
    slug = models.CharField('Уникальный идентификатор локации',
                            max_length=100,
                            null=True,
                            blank=True,
                            unique=True)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = HTMLField('Длинное описание', blank=True)
    lat = models.FloatField('Ширина', max_length=200)
    lon = models.FloatField('Долгота', max_length=200)

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField('Картинка')
    place = models.ForeignKey(Place,
                              related_name='images',
                              verbose_name='Место',
                              on_delete=models.CASCADE)
    order = models.PositiveIntegerField('Порядковый номер картинки',
                                        default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.place.title
