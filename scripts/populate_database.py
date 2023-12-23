from scripts.create_heroes import create_heroes
from scripts.delete_heroes import delete_heroes
from scripts.create_sponsors import create_sponsors

def run():
    create_sponsors()
    delete_heroes()
    create_heroes()
