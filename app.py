import json
import random

#note, even though requests is part of the app, it is unused at the moment.
# mostly bacause it's old and doesn't work.

# print a random city from the cities.json file
with open('cities.json') as f:
    cities = json.load(f)

# random number between 0 and the length of the list of cities
rndCity = random.randint(0, len(cities) - 1)
print(cities[rndCity]['city'])

# Some useless code
def useless(someNumber):
    someNumber += 1
