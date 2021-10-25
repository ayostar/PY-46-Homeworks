from pprint import pprint

import requests


def super_hero_intelligence(super_hero):
    url = ' https://superheroapi.com/api/2619421814940190/search/' + super_hero
    response = requests.get(url)
    new_dict = {}
    new_dict = response.json()
    results = new_dict.get('results')
    for el in results:
        if el['name'] == super_hero:
            character_intelligence = el['powerstats']['intelligence']
            return int(character_intelligence)


if __name__ == '__main__':
    super_heroes = 'Hulk', 'Captain America', 'Thanos'
    character_name = ''
    max_character_intelligence = 0
    for superhero in super_heroes:
        current_character_intelligence = super_hero_intelligence(superhero)
        if current_character_intelligence > max_character_intelligence:
            character_name = superhero
            max_character_intelligence = current_character_intelligence
    print(f'Самый умный супергерой {character_name} с уровнем {max_character_intelligence}')

