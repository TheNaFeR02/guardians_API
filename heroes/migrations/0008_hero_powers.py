# Generated by Django 4.2.1 on 2023-11-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0007_hero_character_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='powers',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
