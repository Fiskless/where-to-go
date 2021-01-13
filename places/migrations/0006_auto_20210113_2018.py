# Generated by Django 3.1.3 on 2021-01-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_remove_place_details_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['my_order']},
        ),
        migrations.AddField(
            model_name='image',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='image',
            name='picture_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер картинки по порядку'),
        ),
    ]
