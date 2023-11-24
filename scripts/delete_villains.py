from villains.models import Villain

def run():
    Villain.objects.all().delete()