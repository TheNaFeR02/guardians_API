# Generated by Django 4.2.1 on 2023-11-05 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0006_alter_hero_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='character_friends',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
