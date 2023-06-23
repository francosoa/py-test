from codigo.poke import Pokemons
import pandas as pd

class TestClass:

    def test_verify_the_type_of_result(self):
        #Given > quando passa uma URI
        input = 'https://pokemonapi.franciscovaldec.repl.co/pokemon'
        output = type(list())

        request = Pokemons(input)
        result = request.GetAllPokemon()


        assert output == type(result)

    def test_check_with_my_function_is_a_datafrane(self):
        #given = We want transform my json result in a dataframe to analysis:
        #action: When the path of API is given
        call_api = Pokemons('https://pokemonapi.franciscovaldec.repl.co/pokemon')

        #resull must be a dataframe:
        result = "<class 'pandas.core.frame.DataFrame'>"

        df = call_api.GetDataFrame()

        assert type(df) == type(pd.DataFrame())

