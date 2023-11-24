from django.db import models
from villains.models import Villain


def upload_to(instance, filename):
    return '{filename}'.format(filename=filename)


def upload_to_images(instance, filename):
    return 'assets/images/heroes/{filename}'.format(filename=filename)


def upload_to_screen_url(instance, filename):
    return 'assets/images/heroes/screen_large_url/{filename}'.format(filename=filename)


class Hero(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    # image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image_url = models.ImageField(
        upload_to=upload_to_images, blank=True, null=True)
    # image_screen_large_url = models.ImageField(
    #     upload_to=upload_to, blank=True, null=True)
    image_screen_large_url = models.ImageField(
        upload_to=upload_to_screen_url, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    character_friends = models.JSONField(blank=True, default=dict)
    powers = models.JSONField(blank=True, default=dict)
    sponsors = models.JSONField(blank=True, default=dict)
    # Add other basic information fields like gender, description, etc.

    # Verify if the sponsors are in the Blacklist, if that's the case we eliminate the agreement.
    def check_sponsors(self):
        blacklist_ids = set(Blacklist.objects.values_list(
            'id', flat=True))  # Get a list of all blacklist IDs

        sponsors = self.sponsors.copy()

        print("Current Sponsors:", self.sponsors)
        for id in sponsors:
            if int(id) in blacklist_ids:
                print('Sponsor ID', id, 'is in the blacklist.')
                self.sponsors.pop(id)  # Eliminate this sponsor from the hero.

        print("Sponsors after blacklist check:", self.sponsors)

    def __str__(self):
        return f'{self.id}-{self.name}-{self.age}-{self.image_url}-{self.description}'


class Fight(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    villain = models.ForeignKey(Villain, on_delete=models.CASCADE)

    RESULT_CHOICES = [
        ('hero_won', 'Hero Won'),
        ('villain_won', 'Villain Won'),
        ('draw', 'Draw'),
    ]

    result = models.CharField(max_length=100, choices=RESULT_CHOICES)


class Ability(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Weakness(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Relationship(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Schedule(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    start = models.CharField(max_length=100, blank=True, null=True)
    end = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    # eventId = models.CharField(max_length=50, blank=True, null=True)
    # Include fields for managing schedules, school, and family meetings.


class Sponsor(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # ~ image


class Blacklist(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    sponsor_name = models.CharField(max_length=100)

    def __str__(self):
        return self.sponsor_name
