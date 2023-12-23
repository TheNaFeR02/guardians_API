import json
import random
from heroes.models import Hero
from django.core.files import File
from scripts.delete_heroes import delete_heroes
from heroes.models import Sponsor
from scripts.create_sponsors import sponsors as sponsorsList


def create_heroes():

    f = open('team_members_info_local.json')
    members = json.load(f)

    for hero in members['team_members']:
        id = hero['id']
        name = hero['name']
        age = random.randint(13, 100)  # This is because no heroe has an age.
        description = hero['deck']

        image_data = open(f'assets/images/heroes/{hero["id"]}_{hero["name"]}.jpg', 'rb')
      
        image_data_screen_large = open(f'assets/images/heroes/screen_large_url/{hero["id"]}_{hero["name"]}.jpg', 'rb')

        # Create File objects using the in-memory data
        image_url = File(image_data)
        image_screen_large_url = File(image_data_screen_large)

        friends = {}
        for i, friend in enumerate(hero['character_friends']):
            friends[i] = friend['name']

        powers = {}
        for i, superpower in enumerate(hero['powers']):
            powers[i] = superpower['name']

        sponsors = {}
        k = 0
        num_sponsors = 4  # each hero has a maximum of 5 sponsors. Set the max you want here.
        while (k < num_sponsors):
            new_sponsor_key = random.randint(1, 20)
            # check if the hero doesn't have the sponsor already.
            if (new_sponsor_key not in sponsors):
                sponsors[new_sponsor_key] = sponsorsList[new_sponsor_key]
            k += 1   

        hero = Hero(
            id=id,
            name=name,
            age=age,
            image_url='', # problem here
            image_screen_large_url='', # problem here too.
            description=description,
            character_friends=friends,
            powers=powers,
            sponsors=sponsors,
        )

        hero.save()

        # this is to choose a file that already exist, otherwise when using save It will create a new image.
        Hero.objects.filter(id=id).update(image_url=image_url)
        Hero.objects.filter(id=id).update(image_screen_large_url=image_screen_large_url)

        image_url.close()
        image_screen_large_url.close()

    f.close()

    


def run():
    create_heroes()


