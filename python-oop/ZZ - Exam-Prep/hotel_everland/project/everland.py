from typing import List

from project.rooms.room import Room

NL = '\n'


class Everland:
    rooms: List[Room]

    def __init__(self) -> None:
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self) -> str:
        total_consumption = sum(r.monthly_total for r in self.rooms)
        return f'Monthly consumptions: {total_consumption:.2f}$.'

    def _get_prepay_report_for_all_rooms(self) -> str:
        msg = []
        for r in self.rooms:
            msg.append(r.get_prepay_report())
        return NL.join(msg)

    def _collect_payments_for_all_rooms(self):
        for r in self.rooms:
            if not r.has_enough_to_pay:
                self.rooms.remove(r)
            r.make_payment()

    def pay(self) -> str:
        report = self._get_prepay_report_for_all_rooms()
        self._collect_payments_for_all_rooms()
        return report

    def status(self) -> str:
        total_population = sum(r.members_count for r in self.rooms)
        msg = []
        msg.append(
            f'Total population: {total_population}')
        msg.extend([str(r) for r in self.rooms])

        return NL.join(msg)
