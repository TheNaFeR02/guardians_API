from heroes.models import Sponsor
import random
from django.core.files import File

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


def create_sponsors():

    for key, name in sponsors.items():
        sponsor = Sponsor(
            id=key,
            name=name,
            image_url='',
            amount=round(random.uniform(0, 1000000), 2),
        )

        image_path = f'assets/images/sponsors/{sponsor.name}.jpg' 
        with open(image_path, 'rb') as image_file:
            image = File(image_file)
            sponsor.image_url = image

            sponsor.save()


def run():
    create_sponsors()
