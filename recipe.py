## -- Modules -- ##

import json
import requests
import sys

## -- Constant -- ##

URL = "https://api.techsmart.codes/nutrition/recipes"

#### ---- RECIPE SEARCH ---- ####

## -- Input -- ##

ingredient = input("Enter an ingredient to find a matching recipe: ")

params = {
    "ingredients_contains": ingredient,
    "limit": 1
    }

## -- Request -- ##



try:
    response = requests.get(URL, params=params)
    recipe = response.json()[0]
    
        
except:
    if response.status_code != 200:
        print("Error, status code is", response.status_code)
    print("Error")
    sys.exit()
    
#### ---- OUTPUT ---- ####

name = recipe["name"]
link = recipe["url"]
print(name + ": " + link)
