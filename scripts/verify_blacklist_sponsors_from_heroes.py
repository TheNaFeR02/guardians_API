from heroes.models import Hero


def run():
    heroes = Hero.objects.all()
    for hero in heroes:
        hero.check_sponsors()