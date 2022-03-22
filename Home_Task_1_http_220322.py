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
    return (list_heroes)

def most_intelligence():
    url = "https://www.superheroapi.com/api.php/2619421814940190/search/Captain_America"
    resp = requests.get(url)
    pprint(resp.json())

input_heroes()