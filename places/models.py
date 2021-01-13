from django.db import models
from adminsortable2.admin import SortableAdminMixin

# Create your models here.
class Place(models.Model):

    title = models.CharField('Название места', max_length=200)
    place_id = models.CharField('Уникальный идентификатор локации', max_length=100, null=True)
    description_short = models.CharField('Короткое описание', max_length=300)
    description_long = models.TextField('Длинное описание')
    lat = models.FloatField('Ширина', max_length=200)
    lon = models.FloatField('Долгота', max_length=200)


    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    img = models.ImageField('Картинка')
    picture_number = models.IntegerField('Номер картинки по порядку', null=True, blank=True)
    place = models.ForeignKey(Place, verbose_name='Место', on_delete=models.CASCADE)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ["my_order"]


    def __str__(self):
        return f'{self.picture_number} {self.place}'
