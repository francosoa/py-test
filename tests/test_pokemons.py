from codigo.poke import Pokemons
import pandas as pd
from pytest import mark as marker


class TestClass:
    @marker.dataframe_result
    def test_verify_the_type_of_result(self):
        # Given > when give an URI
        input = 'https://pokemonapi.franciscovaldec.repl.co/pokemon'
        output = type(list())

        request = Pokemons(input)
        result = request.GetAllPokemon()

        assert output == type(result)

    @marker.dataframe_result
    def test_check_with_my_function_is_a_datafrane(self):
        # given = We want transform my json result in a dataframe to analysis:
        # action: When the path of API is given
        call_api = Pokemons('https://pokemonapi.franciscovaldec.repl.co/pokemon')
        # resull must be a dataframe

        df = call_api.GetDataFrame()

        assert type(df) == type(pd.DataFrame())

    def test_check_if_there_is_null_in_my_dataframe(self):
        # given = the dataset can be with NAN values
        # action = When someone given the URI of API
        response = Pokemons('https://pokemonapi.franciscovaldec.repl.co/pokemon')
        # the result must be zero
        result = 0

        df = response.GetDataFrame()
        check_null = list(df.isna().sum())

        assert sum(check_null) == result
