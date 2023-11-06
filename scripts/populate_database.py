# Guardians of the Globe.

import json
import os
import requests
import random
from django.core.files import File
from heroes.models import Hero, Sponsor
from villains.models import Villain


# To obtain an API Key from comicvine go to: https://comicvine.gamespot.com/api/
API_KEY = '317892504d283a7b070ccf31f08d1a616b477352'

# Bring the list of character members of the team and save them locally in characters_list.json


def fetch_and_save_members_team():
    url = f'http://comicvine.gamespot.com/api/team/4060-41091/?api_key={API_KEY}&format=json&field_list=characters'

    # This is a bug from the API. The API request a User-Agent field in the Header but it doesn't matter what value you give.
    headers = {'User-Agent': 'User'}
    response = requests.get(url, headers=headers)

    # response.status_code == 200 -> OK.
    team_members_list = response.json()
    with open('team_members_list.json', 'w') as f:
        json.dump(team_members_list, f)

    f.close()


def fetch_and_save_team_members_info():
    f = open('team_members_list.json')

    data = json.load(f)

    members = {'team_members': []}

    for hero in data['results']['characters']:
        # print(hero)
        url = f"{hero['api_detail_url']}?api_key={API_KEY}&format=json"

        headers = {'User-Agent': 'User'}
        response = requests.get(url, headers=headers)

        # team_member = response.json()
        team_member_info = response.json()['results']

        members['team_members'].append(team_member_info)

    with open('team_members_info.json', 'w') as team:
        json.dump(members, team)

    f.close()


def fetch_and_save_team_members_images():
    if not os.path.exists('assets/images/heroes'):
        os.makedirs('assets/images/heroes')

    f = open('team_members_info_local.json')

    members = json.load(f)

    for hero in members['team_members']:
        url = hero['image']['original_url']

        response = requests.get(url).content

        with open(f'assets/images/heroes/{hero["id"]}_{hero["name"]}.jpg', 'wb') as image_file:
            image_file.write(response)

    f.close()


def populate_database_heroes():
    f = open('team_members_info_local.json')
    members = json.load(f)

    for hero in members['team_members']:
        id = hero['id']
        name = hero['name']
        age = random.randint(0, 100)  # This is because no heroe has an age.
        description = hero['deck']

        with open(f'assets/images/heroes/{hero["id"]}_{hero["name"]}.jpg', 'rb') as image_file:
            image = File(image_file)

            hero = Hero(
                id=id,
                name=name,
                age=age,
                image_url=image,
                description=description,
            )

            hero.save()

        print("HEROE INSTANCE:", hero)


def add_character_friends_field():
    f = open('team_members_info_local.json')
    members = json.load(f)

    for hero in members['team_members']:
        obj = Hero.objects.filter(id=int(hero['id']))
        friends = {}
        for i, friend in enumerate(hero['character_friends']):
            friends[i] = friend['name']
        print(friends)
        obj.update(character_friends=friends)

    f.close()


def add_powers_field():
    f = open('team_members_info_local.json')
    members = json.load(f)

    for hero in members['team_members']:
        obj = Hero.objects.filter(id=int(hero['id']))
        powers = {}
        for i, superpower in enumerate(hero['powers']):
            powers[i] = superpower['name']
        obj.update(powers=powers)

    f.close()


def fetch_and_save_enemies_list():
    url = f'http://comicvine.gamespot.com/api/team/4060-41091/?api_key={API_KEY}&format=json&field_list=character_enemies'

    # This is a bug from the API. The API request a User-Agent field in the Header but it doesn't matter what value you give.
    headers = {'User-Agent': 'User'}
    response = requests.get(url, headers=headers)

    # response.status_code == 200 -> OK.
    team_members_list = response.json()
    with open('villain_members_list.json', 'w') as f:
        json.dump(team_members_list, f)

    f.close()


def fetch_and_save_enemies_info():
    f = open('villain_members_list.json')

    data = json.load(f)

    members = {'villain_members': []}

    for villain in data['results']['character_enemies']:
        url = f"{villain['api_detail_url']}?api_key={API_KEY}&format=json"

        headers = {'User-Agent': 'User'}
        response = requests.get(url, headers=headers)

        villain_info = response.json()['results']
        members['villain_members'].append(villain_info)

    with open('villain_members_info.json', 'w') as file:
        json.dump(members, file)

    f.close()


def fetch_and_save_enemies_images():
    if not os.path.exists('assets/images/villains'):
        os.makedirs('assets/images/villains')

    f = open('villain_members_info.json')

    members = json.load(f)

    for villain in members['villain_members']:
        url = villain['image']['original_url']

        response = requests.get(url).content

        with open(f'assets/images/villains/{villain["id"]}_{villain["name"]}.jpg', 'wb') as image_file:
            image_file.write(response)

    f.close()


def populate_database_villains():
    villain_weaknesses = {
        "Battle Beast": ["Moral code", "Arrogance"],
        "Bi-Plane": ["Flightless", "Fragile body"],
        "Elephant": ["Large and slow", "Low intelligence"],
        "Furnace": ["Heat-based attacks", "Vulnerability to cold"],
        "Kursk": ["Magnetic attacks", "Limited mobility on land"],
        "Magnattack": ["Magnetic interference", "Overheating"],
        "Omni-Man": ["Kryptonite", "Emotional instability"],
        "Titan": ["Extreme temperatures", "Lack of flight"]
    }

    f = open('villain_members_info.json')
    members = json.load(f)

    for villain in members['villain_members']:
        id = villain['id']
        name = villain['name']
        age = random.randint(0, 100)  # This is because no villain  has an age.
        description = villain['deck']

        # remember that the enemies of a villain are ~usually a hero.
        character_enemies = {charac_enem['id']: charac_enem['name']
                             for charac_enem in villain['character_enemies']}

        powers = {index: power['name']
                  for index, power in enumerate(villain['powers'])}

        weaknesses = {index: weakness for index, weakness in enumerate(
            villain_weaknesses[villain['name']])}

        print(character_enemies)

        with open(f'assets/images/villains/{villain["id"]}_{villain["name"]}.jpg', 'rb') as image_file:
            image = File(image_file)

            villain = Villain(
                id=id,
                name=name,
                age=age,
                image_url=image,
                description=description,
                character_enemies=character_enemies,
                powers=powers,
                weaknesses=weaknesses,
            )

            villain.save()

        print("HEROE INSTANCE:", villain)

    f.close()


def create_sponsors_and_assign_to_heroes():
    sponsors = {
        1: "StarTech Industries",
        2: "VirtueCorp",
        3: "PowerGlide Energy",
        4: "GuardianTech Solutions",
        5: "Celestial Enterprises",
        6: "NovaHealth Pharmaceuticals",
        7: "Aegis Armory",
        8: "OmniCorp",
        9: "QuantumFusion Labs",
        10: "Pinnacle Innovations",
        11: "Titan Motors",
        12: "NebulaX Communications",
        13: "Infinity BioTech",
        14: "Solaris Solar Energy",
        15: "GuardianShield Insurance",
        16: "Horizon Aerospace",
        17: "Vigilant Security Systems",
        18: "EarthForce Conservation",
        19: "Zenith Robotics",
        20: "Elemental Elixirs"
    }

    for key, name in sponsors.items():

        sponsor = Sponsor(
            id=key,
            name=name,
            amount=round(random.uniform(0,1000000),2),
        )
        sponsor.save()

    # Assign the sponsors to the heroes.
    heroes = Hero.objects.all()


    for hero in heroes:
        if(hero.sponsors == None):
            hero.sponsors = {}
        
        # creating n new  num_sponsors.
        k=0
        num_sponsors = 4 # each hero has a maximum of 5 sponsors.
        while (k < num_sponsors):
            new_sponsor_key = random.randint(1, 20)
            # check if the hero doesn't have the sponsor already.
            if (new_sponsor_key not in hero.sponsors):
                hero.sponsors[new_sponsor_key] = sponsors[new_sponsor_key]
                hero.save()
            k+=1
        print(hero.sponsors)

def run():

    # fetch_and_save_members_team()
    # fetch_and_save_team_members_info()
    # fetch_and_save_team_members_images()
    # populate_database_heroes()
    # add_character_friends_field()
    # add_powers_field()

    # fetch_and_save_enemies_list()
    # fetch_and_save_enemies_info()
    # fetch_and_save_enemies_images()
    # populate_database_villains()

    # create_sponsors_and_assign_to_heroes()

    # create all of the sponsors.

    
    pass
    
        

   
