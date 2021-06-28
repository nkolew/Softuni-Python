from typing import List

from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        return 'This pokemon is already caught'

    def release_pokemon(self, pokemon_name: str):
        for i, pokemon in enumerate(self.pokemons):
            if pokemon.name == pokemon_name:
                self.pokemons.pop(i)
                return f'You have released {pokemon_name}'
        return f'Pokemon is not caught'

    def trainer_data(self):
        message = []
        nl = '\n'

        message.append(f'Pokemon Trainer {self.name}')
        message.append(f'Pokemon count {len(self.pokemons)}')
        for pokemon in self.pokemons:
            message.append(f'- {pokemon.pokemon_details()}')

        return nl.join(message)
