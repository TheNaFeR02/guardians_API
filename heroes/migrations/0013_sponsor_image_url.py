# Generated by Django 4.2.1 on 2023-11-08 20:36

from django.db import migrations, models
import heroes.models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0012_alter_hero_sponsors'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=heroes.models.upload_to),
        ),
    ]
