import json
import os

import requests


def hero_image_bg_from_api():
    if not os.path.exists('assets/images/heroes/screen_large_url'):
        os.makedirs('assets/images/heroes/screen_large_url')

    f = open('team_members_info_local.json')

    members = json.load(f)

    for hero in members['team_members']:
        url = hero['image']['screen_large_url']

        response = requests.get(url).content

        with open(f'assets/images/heroes/screen_large_url/{hero["id"]}_{hero["name"]}.jpg', 'wb') as image_file:
            image_file.write(response)

    f.close()

def run():
  hero_image_bg_from_api()