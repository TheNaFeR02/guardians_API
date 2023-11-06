from django.db import models

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.
class Villain(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    origin = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    character_enemies = models.JSONField(blank=True, null=True)
    powers = models.JSONField(blank=True, null=True)
    weaknesses = models.JSONField(blank=True, null=True)

class Ability(models.Model): # Ability/Power
    villain = models.ForeignKey(Villain, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

# class Weakness(models.Model):
#     villain = models.ForeignKey(Villain, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     description = models.TextField()

