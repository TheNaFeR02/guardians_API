from django.db import models

def upload_to(instance, filename):
    return '{filename}'.format(filename=filename)

def upload_to_images(instance, filename):
    return 'assets/images/villains/{filename}'.format(filename=filename)


def upload_to_screen_url(instance, filename):
    return 'assets/images/villains/screen_large_url/{filename}'.format(filename=filename)



# Create your models here.
class Villain(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    origin = models.CharField(max_length=100, blank=True, null=True)
    # image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # image_screen_large_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image_url = models.ImageField(
        upload_to=upload_to_images, blank=True, null=True)
    # image_screen_large_url = models.ImageField(
    #     upload_to=upload_to, blank=True, null=True)
    image_screen_large_url = models.ImageField(
        upload_to=upload_to_screen_url, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    character_enemies = models.JSONField(blank=True, default=dict)
    powers = models.JSONField(blank=True, default=dict)
    weaknesses = models.JSONField(blank=True, default=dict)

    def __str__(self):
        return f'{self.id}-{self.name}-{self.age}-{self.description}'

class Ability(models.Model): # Ability/Power
    villain = models.ForeignKey(Villain, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

# class Weakness(models.Model):
#     villain = models.ForeignKey(Villain, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     description = models.TextField()

