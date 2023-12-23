import json
import random
from villains.models import Villain
from django.core.files import File

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


def create_villains():

    f = open('villain_members_info.json')
    members = json.load(f)

    for villain in members['villain_members']:
        id = villain['id']
        name = villain['name']
        age = random.randint(0, 100)  # This is because no villain  has an age.
        description = villain['deck']

        image_data = open(
            f'assets/images/villains/{villain["id"]}_{villain["name"]}.jpg', 'rb')

        image_data_screen_large = open(
            f'assets/images/villains/screen_large_url/{villain["id"]}_{villain["name"]}.jpg', 'rb')

        # Create File objects using the in-memory data
        image_url = File(image_data)
        image_screen_large_url = File(image_data_screen_large)

        # remember that the enemies of a villain are ~usually a hero.
        character_enemies = {charac_enem['id']: charac_enem['name']
                             for charac_enem in villain['character_enemies']}

        powers = {index: power['name']
                  for index, power in enumerate(villain['powers'])}

        weaknesses = {index: weakness for index, weakness in enumerate(
            villain_weaknesses[villain['name']])}

        villainInstance = Villain(
            id=id,
            name=name,
            age=age,
            origin="",
            image_url='',
            image_screen_large_url='',
            description=description,
            character_enemies=character_enemies,
            powers=powers,
            weaknesses=weaknesses,
        )

        villainInstance.save()

        Villain.objects.filter(id=id).update(image_url=image_url)
        Villain.objects.filter(id=id).update(
            image_screen_large_url=image_screen_large_url)
        
        image_url.close()
        image_screen_large_url.close()




def run():
    create_villains()
