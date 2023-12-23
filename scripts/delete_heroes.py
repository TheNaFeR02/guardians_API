from heroes.models import Hero

def delete_heroes():
    Hero.objects.all().delete()


def run():
    delete_heroes()