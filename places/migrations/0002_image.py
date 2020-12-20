# Generated by Django 3.1.3 on 2020-12-20 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('picture_number', models.IntegerField(verbose_name='Номер картинки по порядку')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='Место')),
            ],
        ),
    ]