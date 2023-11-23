import random
from heroes.models import Schedule, Hero
from datetime import datetime

color_list = [
    "#001f3f",  # Dark Blue
    "#004b33",  # Dark Green
    "#8b0000",  # Dark Red
    "#4b0082",  # Dark Purple
    "#333333",  # Dark Gray
    "#3498db",  # Light Blue
    "#2ecc71",  # Light Green
    "#e74c3c",  # Light Red
    "#9b59b6",  # Light Purple
    "#bdc3c7"   # Light Gray
]


def run():
    # Sunday
    # School Event
    # Schedule(hero=Hero.objects.get(id=5210), title='Go to school', start="2023-11-19" +
    #          "T09:00:00", end="2023-11-19"+"T13:00:00", color=color_list[random.randint(0, 9)]).save()

    # # Lunch
    # Schedule(hero=Hero.objects.get(id=5210), title='Lunch', start="2023-11-19"+"T13:00:00",
    #          end="2023-11-19"+"T14:00:00", color=color_list[random.randint(0, 9)]).save()

    # # Homework
    # Schedule(hero=Hero.objects.get(id=5210), title='Homework', start="2023-11-19"+"T14:00:00",
    #          end="2023-11-19"+"T17:00:00", color=color_list[random.randint(0, 9)]).save()

    # # Family time
    # Schedule(hero=Hero.objects.get(id=5210), title='Family time', start="2023-11-19" +
    #          "T18:00:00", end="2023-11-19"+"T20:00:00", color=color_list[random.randint(0, 9)]).save()


# Days from Monday (20) to Friday (24)
  # for day in range(20, 25):
  #   # School Event
  #   Schedule(hero=Hero.objects.get(id=hero_id), title='Go to school', start=f"2023-11-{day:02d}T09:00:00",
  #            end=f"2023-11-{day:02d}T13:00:00", color=color_list[random.randint(0, 9)]).save()

  #   # Lunch
  #   Schedule(hero=Hero.objects.get(id=hero_id), title='Lunch', start=f"2023-11-{day:02d}T13:00:00",
  #            end=f"2023-11-{day:02d}T14:00:00", color=color_list[random.randint(0, 9)]).save()

  #   # Homework
  #   Schedule(hero=Hero.objects.get(id=hero_id), title='Homework', start=f"2023-11-{day:02d}T14:00:00",
  #            end=f"2023-11-{day:02d}T17:00:00", color=color_list[random.randint(0, 9)]).save()

  #   # Family time
  #   Schedule(hero=Hero.objects.get(id=hero_id), title='Family time', start=f"2023-11-{day:02d}T18:00:00",
  #            end=f"2023-11-{day:02d}T20:00:00", color=color_list[random.randint(0, 9)]).save()


  Schedule.objects.all().delete()

  for hero in Hero.objects.all():
    # hero_id = 5210
    hero_id = hero.id


    # Teenagers Schedule ----------------------------------------------------------------------------------
    if(hero.age >= 13 and hero.age<=20):
      # Days in November from Wednesday (1) to Thursday (30)
      for day in range(1, 31):
        # Calculate the day of the week (0: Sunday, 1: Monday, ..., 6: Saturday)
        day_of_week = (day + 2) % 7

        # Check if the day is not Sunday (6) or Saturday (5)
        if day_of_week != 6 and day_of_week != 0:
            # School Event
            Schedule(hero=Hero.objects.get(id=hero_id), title='Go to school', start=f"2023-11-{day:02d}T09:00:00",
                     end=f"2023-11-{day:02d}T13:00:00", color=color_list[random.randint(0, 9)]).save()

            # Lunch
            Schedule(hero=Hero.objects.get(id=hero_id), title='Lunch', start=f"2023-11-{day:02d}T13:00:00",
                     end=f"2023-11-{day:02d}T14:00:00", color=color_list[random.randint(0, 9)]).save()

            # Homework
            Schedule(hero=Hero.objects.get(id=hero_id), title='Homework', start=f"2023-11-{day:02d}T14:00:00",
                     end=f"2023-11-{day:02d}T17:00:00", color=color_list[random.randint(0, 9)]).save()

            # Family time
            Schedule(hero=Hero.objects.get(id=hero_id), title='Family time', start=f"2023-11-{day:02d}T18:00:00",
                     end=f"2023-11-{day:02d}T20:00:00", color=color_list[random.randint(0, 9)]).save()
      
        if day_of_week == 0:
            Schedule(hero=Hero.objects.get(id=hero_id), title='Go to Church', start=f"2023-11-{day:02d}T10:00:00",
                    end=f"2023-11-{day:02d}T12:00:00", color=color_list[random.randint(0, 9)]).save()
        
        if day_of_week == 6:
          Schedule(hero=Hero.objects.get(id=hero_id), title='Walk the dog', start=f"2023-11-{day:02d}T07:00:00",
                    end=f"2023-11-{day:02d}T09:00:00", color=color_list[random.randint(0, 9)]).save()
        
          Schedule(hero=Hero.objects.get(id=hero_id), title='Play Videogames', start=f"2023-11-{day:02d}T16:00:00",
                    end=f"2023-11-{day:02d}T18:00:00", color=color_list[random.randint(0, 9)]).save()
      continue
    # -----------------------------------------------------------------------------------------------------

    # Adults Schedule -------------------------------------------------------------------------------------
    for day in range(1,31):
      day_of_week = (day + 2) % 7

      if day_of_week != 6 and day_of_week != 0:
        # Breakfast
        Schedule(hero=Hero.objects.get(id=hero_id), title='Breakfast', start=f"2023-11-{day:02d}T09:00:00",
                  end=f"2023-11-{day:02d}T13:00:00", color=color_list[random.randint(0, 9)]).save()

        # Take kids to school
        Schedule(hero=Hero.objects.get(id=hero_id), title='Take kids to school', start=f"2023-11-{day:02d}T13:00:00",
                  end=f"2023-11-{day:02d}T14:00:00", color=color_list[random.randint(0, 9)]).save()

        # Work
        Schedule(hero=Hero.objects.get(id=hero_id), title='Work', start=f"2023-11-{day:02d}T14:00:00",
                  end=f"2023-11-{day:02d}T17:00:00", color=color_list[random.randint(0, 9)]).save()

        # Protect the lobe
        Schedule(hero=Hero.objects.get(id=hero_id), title='Protect the globe', start=f"2023-11-{day:02d}T18:00:00",
                  end=f"2023-11-{day:02d}T20:00:00", color=color_list[random.randint(0, 9)]).save()
      
      if day_of_week == 0:
            Schedule(hero=Hero.objects.get(id=hero_id), title='Go to Church', start=f"2023-11-{day:02d}T10:00:00",
                    end=f"2023-11-{day:02d}T12:00:00", color=color_list[random.randint(0, 9)]).save()
        
      if day_of_week == 6:
        Schedule(hero=Hero.objects.get(id=hero_id), title='Workout/Gym', start=f"2023-11-{day:02d}T07:00:00",
                  end=f"2023-11-{day:02d}T09:00:00", color=color_list[random.randint(0, 9)]).save()
      
        Schedule(hero=Hero.objects.get(id=hero_id), title='Yoga', start=f"2023-11-{day:02d}T16:00:00",
                  end=f"2023-11-{day:02d}T18:00:00", color=color_list[random.randint(0, 9)]).save()
    # -----------------------------------------------------------------------------------------------------

          
      