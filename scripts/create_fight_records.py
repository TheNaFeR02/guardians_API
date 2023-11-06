import random
from heroes.models import Fight
from heroes.models import Hero
from villains.models import Villain


def run():
    # print(Hero.objects.get(id=119156))
    villains = Villain.objects.all()
    result_choices = ['hero_won', 'villain_won', 'draw']

    for villain in villains:
        print(villain.character_enemies)
        for id in villain.character_enemies.keys():
            try:
                hero = Hero.objects.get(id=id)

                num_fights = random.randint(0, 10)
               
                i = 0
                while (i < num_fights):
                    fight = Fight(
                        hero=hero,
                        villain=villain,
                        result=result_choices[random.randint(0, 2)]
                    )
                    fight.save()
                    i+=1
            except:
                print('The villain fought with somebody who is not a hero in our database')

            
