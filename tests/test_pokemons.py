from codigo.poke import Pokemons

class TestClass:

    def test_verify_the_type_of_result(self):
        #Given > quando passa uma URI
        input = 'https://pokemonapi.franciscovaldec.repl.co/pokemon'
        output = type(list())

        request = Pokemons(input)
        result = request.GetAllPokemon()


        assert output == type(result)
