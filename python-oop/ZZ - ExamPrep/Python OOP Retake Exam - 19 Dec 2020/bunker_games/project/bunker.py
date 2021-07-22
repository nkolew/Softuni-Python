from typing import List, Union

from project import (Survivor, Supply, Medicine,
                     FoodSupply, WaterSupply,
                     Painkiller, Salve)


class Bunker:
    survivors: List[Survivor]
    supplies: List[Supply]
    medicine: List[Medicine]

    def __init__(self) -> None:
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        """
        property that returns only the food objects from the supplies
        (if there are no food supplies, raise IndexError with message
        "There are no food supplies left!")
        """
        food = [s for s in self.supplies if isinstance(s, FoodSupply)]

        if not food:
            raise IndexError('There are no food supplies left!')

        return food

    @property
    def water(self):
        """
        property that returns only the water objects from the supplies
        (if there are no water supplies, raise IndexError with message
        "There are no water supplies left!")
        """
        water = [s for s in self.supplies if isinstance(s, WaterSupply)]

        if not water:
            raise IndexError('There are no water supplies left!')

        return water

    @property
    def painkillers(self):
        """
        property that returns only the painkiller objects from the medicine
        (if there are no painkillers, raise IndexError with message
        "There are no painkillers left!")
        """
        painkillers = [m for m in self.medicine if isinstance(m, Painkiller)]

        if not painkillers:
            raise IndexError('There are no painkillers left!')

        return painkillers

    @property
    def salves(self):
        """
        property that returns only the salve objects from the medicine
        (if there are no salves, raise IndexError with message
        "There are no salves left!")
        """
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

    @staticmethod
    def _pop_and_apply_last_item(survivor: Survivor, item_type: str, col: list) -> bool:
        for index, item in reversed(list(enumerate(col))):
            if item.__class__.__name__ == item_type:
                item.apply(survivor)
                col.pop(index)
                return True

        return False

    def heal(self, survivor: Survivor, medicine_type: str) -> Union[str, None]:
        if survivor.needs_healing:
            rv = self._pop_and_apply_last_item(
                survivor, medicine_type, self.medicine)
            if rv:
                return f'{survivor.name} healed successfully with {medicine_type}'

    def sustain(self, survivor: Survivor, sustenance_type: str) -> Union[str, None]:
        if survivor.needs_sustenance:
            rv = self._pop_and_apply_last_item(
                survivor, sustenance_type, self.supplies)
            if rv:
                return f'{survivor.name} sustained successfully with {sustenance_type}'

    def next_day(self, ):
        """
        First, the needs of each survivor get reduced by the result of multiplying his/her age by 2
        Then we need to sustain each survivor by giving him/her one food and one water supply
        """

        for s in self.survivors:
            s.needs -= (s.age*2)
            self.sustain(s, 'FoodSupply')
            self.sustain(s, 'WaterSupply')
