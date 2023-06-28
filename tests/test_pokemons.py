import pytest
from codigo.poke import Pokemons
import pandas as pd
from pytest import mark as marker
import logging


class TestClass:

    @pytest.fixture
    def test_get_result_from_my_api(self):

        input = 'https://pokemonapi.franciscovaldec.repl.co/pokemon'
        request = Pokemons(input)

        return request

    @marker.dataframe_result
    def test_verify_the_type_of_result(self, test_get_result_from_my_api):
        response = test_get_result_from_my_api.GetAllPokemon()
        output = type(list())


        assert output == type(response)

    @marker.dataframe_result
    def test_check_with_my_function_is_a_datafrane(self, test_get_result_from_my_api):
        # given = We want transform my json result in a dataframe to analysis:
        # action: When the path of API is given

        # resull must be a dataframe

        df = test_get_result_from_my_api.GetDataFrame()

        assert type(df) == type(pd.DataFrame())

    def test_check_if_there_is_null_in_my_dataframe(self, test_get_result_from_my_api):
        # given = the dataset can be with NAN values
        # action = When someone given the URI of API
        # the result must be zero
        result = 0

        df = test_get_result_from_my_api.GetDataFrame()
        check_null = list(df.isna().sum())

        assert sum(check_null) == result

    def test_check_if_all_column_is_correct(self, test_get_result_from_my_api):
        df = test_get_result_from_my_api.GetDataFrame()
        columns = df.columns

        for col in columns:
            lista = []
            if col in ["attack", "defense", "generation", "hp", "id",
                           "legendary", "name", "sp_atk", "sp_atk",
                           "speed", "total", "type_1", "type_2", "sp_def"]:
                logging.info(col)
            else:
                assert False, f"the column {col} there is not a column desired"


