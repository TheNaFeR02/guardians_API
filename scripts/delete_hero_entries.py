from heroes.models import Hero


def run():
    Hero.objects.all().delete()
    
    