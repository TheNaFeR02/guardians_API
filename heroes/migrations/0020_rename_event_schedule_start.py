# Generated by Django 4.2.1 on 2023-11-22 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0019_schedule_event_schedule_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='event',
            new_name='start',
        ),
    ]
