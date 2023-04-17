import json

import requests

response = requests.get('https://api.kodim.cz/python-data/people')
print(response.text)


#data = response.json()
#print(data)


