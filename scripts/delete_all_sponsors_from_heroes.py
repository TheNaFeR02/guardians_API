from heroes.models import Hero

def run():

    heroes = Hero.objects.all()

    for hero in heroes:
        hero.sponsors = {}
        hero.save()