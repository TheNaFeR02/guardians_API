# Generated by Django 4.2.1 on 2023-11-01 20:00

from django.db import migrations, models
import django.db.models.deletion
import villains.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Villain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('birth', models.CharField(max_length=100)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to=villains.models.upload_to)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('villain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villains.villain')),
            ],
        ),
    ]
