# Generated by Django 5.0.3 on 2024-05-15 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_restaurant_cuisine_restaurant_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='food_img_url_1',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='food_img_url_2',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='img_url',
        ),
    ]
