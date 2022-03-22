import requests

from pprint import pprint

# input the names of heroes
def input_heroes():
    list_heroes = []
    name = ''
    while name != 'stop':
        name = input('Input the name of hero (else: "stop"): ')
        if name == 'stop':
            break
        else:
            list_heroes.append(name)
    return list_heroes

# creating the dictionary of heroes with their intelligences
def dict_heroes_intel():
    heroes = input_heroes()
    print(f'You are input the names: {heroes}.')
    heroes_intell_dict = {}
    for item in heroes:
        url = f"https://www.superheroapi.com/api.php/2619421814940190/search/{item}"
        resp_name = requests.get(url)
        try:
            int_hero = resp_name.json()['results'][0]['powerstats']['intelligence']
        except LookupError:
            print(f'Wrong name: {item}.')
        else:
            heroes_intell_dict[item] = int(int_hero)         
    return heroes_intell_dict

# the method of choosing most intelligence hero 
def most_intell_hero():
    intel_hero = dict_heroes_intel()
    intel_hero_sorted = sorted(intel_hero.items(), key=lambda item: item[1])
    best_hero = intel_hero_sorted[(len(intel_hero_sorted) - 1)][0]
    intell_level = intel_hero_sorted[(len(intel_hero_sorted) - 1)][1]
    print(f'The heroes are: {intel_hero_sorted}.\nThe most intelligence hero is {best_hero} with the grade intelligence {intell_level}.')

most_intell_hero()