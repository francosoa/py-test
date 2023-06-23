import pandas as pd
import requests
import json

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


    def GetDataFrame(self):
        response = requests.get(self.url)
        json_result = response.json()

        df = pd.json_normalize(json_result)

        return df


all_api = Pokemons('https://pokemonapi.franciscovaldec.repl.co/pokemon')

df = all_api.GetDataFrame()
print(df)