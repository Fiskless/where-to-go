from django.db import models

# Create your models here.
class Place(models.Model):

    title = models.CharField('Название места', max_length=200)
    description_short = models.CharField('Короткое описание', max_length=200)
    description_long = models.TextField('Длинное описание')
    lat = models.FloatField('Ширина', max_length=200)
    lon = models.FloatField('Долгота', max_length=200)

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    img = models.ImageField('Картинка', upload_to='places/pictures')
    picture_number = models.IntegerField('Номер картинки по порядку')
    place = models.ForeignKey(Place, verbose_name='Место', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.picture_number} {self.place}'