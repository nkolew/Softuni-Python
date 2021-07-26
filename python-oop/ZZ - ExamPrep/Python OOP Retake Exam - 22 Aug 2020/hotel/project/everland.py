from collections import deque
from typing import ClassVar, Deque, List

from project import Room


class Everland:
    __rooms: Deque[Room]
    _DAYS_IN_MONTH: ClassVar[int] = 30

    def __init__(self) -> None:
        self.__rooms = deque()

    @property
    def rooms(self):
        return list(self.__rooms)

    def add_room(self, room: Room) -> None:
        self.__rooms.append(room)

    def get_monthly_consumptions(self) -> str:
        """
        Calculate the expenses of each room + the room_cost
        and return the result in the following format:
        "Monthly consumption: {total_consumption}$."
        """

        monthly = sum(self._get_monthly_due_for_room(r)
                     for r in self.__rooms)

        return f"Monthly consumptions: {monthly:.2f}$."

    def _get_monthly_due_for_room(self, room: Room) -> float:
        return (room.__class__._ROOM_COST + room.expenses * self.__class__._DAYS_IN_MONTH)

    def _room_has_enough_budget_to_pay(self, room: Room) -> bool:
        return room.budget >= self._get_monthly_due_for_room(room)

    # def _get_payment_info_for_room(self, room: Room) -> str:
    #     if self._room_has_enough_budget_to_pay(room):
    #         room_monthly_expenses = self._get_monthly_due_for_room(room)
    #         room.budget -= room_monthly_expenses
    #         return f'{room.family_name} paid {room_monthly_expenses:.2f}$ and have {room.budget:.2f}$ left.'

    #     self.rooms.remove(room)
    #     return f'{room.family_name} does not have enough budget and must leave the hotel.'

    def pay(self) -> str:
        """
        Each room represents one of the following strings:
        •	If the budget of the family is enough to pay for the month
            – "{family_name} paid {expenses+room_cost}$ and have {new_budget}$ left."
        and reduce the budget of the family
        •	If the budget is NOT enough to pay for the month
            – "{family_name} does not have enough budget and must leave the hotel."
        and remove the room from the rooms list
        Return all the information by joining the strings by a new line
        """

        # message = [self._get_payment_info_for_room(r) for r in self.rooms]

        # return '\n'.join(message)
        message = []

        i = 0
        end = len(self.__rooms)

        while i < end:
            r = self.__rooms.popleft()

            if not self._room_has_enough_budget_to_pay(r):
                message.append(
                    f'{r.family_name} does not have enough budget and must leave the hotel.')

                i += 1
                continue

            room_monthly_expenses = self._get_monthly_due_for_room(r)
            r.budget -= room_monthly_expenses
            self.__rooms.append(r)
            message.append(
                f'{r.family_name} paid {room_monthly_expenses:.2f}$ and have {r.budget:.2f}$ left.')
            i += 1

        return '\n'.join(message)

    def status(self) -> str:
        message = []

        total_population = sum(r.members_count for r in self.__rooms)

        message.append(f'Total population: {total_population}')

        for r in self.__rooms:
            monthly_expenses = self.__class__._DAYS_IN_MONTH * r.expenses
            message.append(
                f'{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {monthly_expenses:.2f}$')
            if r.children:
                for i, c in enumerate(r.children, start=1):
                    message.append(
                        f'--- Child {i} monthly cost: {c.cost * self.__class__._DAYS_IN_MONTH:.2f}$')

            if r.__class__._APPLIANCES:
                appliances_monthly_cost = sum(
                    a.cost for a in r.__class__._APPLIANCES) * self.__class__._DAYS_IN_MONTH * r.members_count
                message.append(
                    f'--- Appliances monthly cost: {appliances_monthly_cost:.2f}$')

        return '\n'.join(message)
