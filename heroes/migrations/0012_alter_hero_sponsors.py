# Generated by Django 4.2.1 on 2023-11-05 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0011_alter_hero_sponsors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='sponsors',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
