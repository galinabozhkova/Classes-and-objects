from project.pokemon import Pokemon


class Trainer():
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def check_if_in (self, pokemon_name):
        for el in self.pokemon:
            if el.name == pokemon_name:
                return True
        return False


    def add_pokemon(self, pokemon: Pokemon):
        if self.check_if_in(pokemon.name):
            return f"This pokemon is already caught"

        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self,pokemon_name) :
        if self.check_if_in(pokemon_name):
            for el in self.pokemon:
                if el.name == pokemon_name:
                    self.pokemon.remove(el)
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}"
        for el in self.pokemon:
            result += f"\n- {el.pokemon_details()}"
            return result





