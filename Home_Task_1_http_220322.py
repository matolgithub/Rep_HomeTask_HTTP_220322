import requests

import pprint

url = "https://superheroapi.com/api/2619421814940190/search/name"
resp = requests.get(url)
pprint(resp.json())
# pprint(resp.status_code)
# # print(resp.headers)
# print(resp.status_code)
# # print(resp.text)
# # print(resp.content)
# # print(resp.text)