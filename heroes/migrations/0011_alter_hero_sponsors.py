# Generated by Django 4.2.1 on 2023-11-05 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0010_blacklist_remove_sponsor_hero_remove_sponsor_origin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='sponsors',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
