from typing import List, Optional, Union

from project.medicine.medicine import Medicine
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    survivors: List[Survivor]
    supplies: List[Supply]
    medicine: List[Medicine]

    def __init__(self) -> None:
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self) -> List[FoodSupply]:
        food = [s for s in self.supplies if isinstance(s, FoodSupply)]
        if not food:
            raise IndexError('There are no food supplies left!')

        return food

    @property
    def water(self) -> List[WaterSupply]:
        water = [s for s in self.supplies if isinstance(s, WaterSupply)]
        if not water:
            raise IndexError('There are no water supplies left!')

        return water

    @property
    def painkillers(self) -> List[Painkiller]:
        painkillers = [m for m in self.medicine if isinstance(m, Painkiller)]
        if not painkillers:
            raise IndexError('There are no painkillers left!')

        return painkillers

    @property
    def salves(self) -> List[Salve]:
        salves = [m for m in self.medicine if isinstance(m, Salve)]
        if not salves:
            raise IndexError('There are no salves left!')

        return salves

    def add_survivor(self, survivor: Survivor) -> None:
        if survivor in self.survivors:
            raise ValueError(
                f'Survivor with name {survivor.name} already exists.')

        self.survivors.append(survivor)

    def add_supply(self, supply: Supply) -> None:
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine) -> None:
        self.medicine.append(medicine)

    def _pop_last_item_of_type(self, item_type: str) -> Union[Supply, Medicine, None]:
        collection_by_item_type = {
            'FoodSupply': self.supplies,
            'WaterSupply': self.supplies,
            'Painkiller': self.medicine,
            'Salve': self.medicine,
        }

        for index, item in reversed(list(enumerate(collection_by_item_type[item_type]))):
            if item.__class__.__name__ == item_type:
                return collection_by_item_type[item_type].pop(index)

        return None

    def heal(self, survivor: Survivor, medicine_type: str) -> Optional[str]:
        if not survivor.needs_healing:
            return

        medicine = self._pop_last_item_of_type(medicine_type)
        if not medicine:
            return

        medicine.apply(survivor)
        return f'{survivor.name} healed successfully with {medicine_type}'

    def sustain(self, survivor: Survivor, sustenance_type: str) -> Optional[str]:
        if not survivor.needs_sustenance:
            return

        sustenance = self._pop_last_item_of_type(sustenance_type)
        if not sustenance:
            return

        sustenance.apply(survivor)
        return f'{survivor.name} sustained successfully with {sustenance_type}'

    def next_day(self):
        for s in self.survivors:
            s.needs -= 2 * s.age

            food = self._pop_last_item_of_type('FoodSupply')
            if food:
                food.apply(s)

            water = self._pop_last_item_of_type('WaterSupply')
            if water:
                water.apply(s)
