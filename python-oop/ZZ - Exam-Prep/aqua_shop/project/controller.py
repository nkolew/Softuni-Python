from itertools import chain
from typing import Dict, List, Optional, Type

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.base_decoration import BaseDecoration
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.base_fish import BaseFish
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    decorations_repository: DecorationRepository
    aquariums: List[BaseAquarium]

    def __init__(self) -> None:
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str) -> str:
        aquarium_types = {
            'FreshwaterAquarium': FreshwaterAquarium,
            'SaltwaterAquarium': SaltwaterAquarium,
        }
        if aquarium_type not in aquarium_types:
            return "Invalid aquarium type."

        self.aquariums.append(aquarium_types[aquarium_type](aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str) -> str:
        decoration_types = {
            'Ornament': Ornament,
            'Plant': Plant,
        }
        if decoration_type not in decoration_types:
            return "Invalid decoration type."

        self.decorations_repository.add(decoration_types[decoration_type]())
        return f"Successfully added {decoration_type}."

    def _find_aquarium(self, aquarium_name: str) -> Optional[BaseAquarium]:
        for i in self.aquariums:
            if i.name == aquarium_name:
                return i

        return None

    def _pop_first_decoration_of_type(self, decoration_type: str) -> Optional[BaseDecoration]:
        d = self.decorations_repository.find_by_type(decoration_type)
        if not isinstance(d, BaseDecoration):
            return None

        self.decorations_repository.remove(d)
        return d

    def insert_decoration(self, aquarium_name: str, decoration_type: str) -> Optional[str]:
        aquarium = self._find_aquarium(aquarium_name)
        if not aquarium:
            return None

        decoration = self._pop_first_decoration_of_type(decoration_type)
        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."

        aquarium.add_decoration(decoration)
        return f'Successfully added {decoration_type} to {aquarium_name}.'

    def add_fish(self, aquarium_name: str,
                 fish_type: str,
                 fish_name: str,
                 fish_species: str,
                 price: float) -> Optional[str]:
        aquarium = self._find_aquarium(aquarium_name)
        if not aquarium:
            return None

        fish_types: Dict[str, Type[BaseFish]] = {
            'FreshwaterFish': FreshwaterFish,
            'SaltwaterFish': SaltwaterFish,
        }

        if fish_type not in fish_types:
            return f"There isn't a fish of type {fish_type}."

        fish = fish_types[fish_type](fish_name, fish_species, price)
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str) -> Optional[str]:
        a = self._find_aquarium(aquarium_name)
        if not a:
            return None

        a.feed()
        return f'Fish fed: {len(a.fish)}'

    def calculate_value(self, aquarium_name: str) -> Optional[str]:
        a = self._find_aquarium(aquarium_name)
        if not a:
            return None

        value = sum(i.price for i in chain(a.fish, a.decorations))
        return f'The value of Aquarium {a.name} is {value:.2f}.'

    def report(self) -> str:
        return '\n'.join([a.str() for a in self.aquariums])
