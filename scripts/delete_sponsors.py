from heroes.models import Sponsor

def delete_sporsors():
    Sponsor.objects.all().delete()


def run():
    delete_sporsors()