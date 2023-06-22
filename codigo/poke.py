import pandas as pd
import requests

class Pokemons:
    def __init__(self, url):
        self.url = url

    def GetAllPokemon(self):

        response = requests.get(self.url)
        if response.status_code == 200:
            result = response.json()
        else:
            result = response.content

        return result


