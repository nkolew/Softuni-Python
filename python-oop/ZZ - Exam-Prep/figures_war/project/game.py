from typing import Optional

from project import (AreaBattle, Battle, CircumferenceBattle,
                     Figure, RelativeBattle, Suitcase)


class Game:
    figures: Suitcase
    battle_ground: Optional[Battle]

    def __init__(self) -> None:
        self.figures = Suitcase()
        self.battle_ground = None

    def _get_battle_ground_of_type(self, battle_type: str) -> Battle:
        battle_types = {
            'area': AreaBattle,
            'circumference': CircumferenceBattle,
            'relativity': RelativeBattle,
        }
        return battle_types[battle_type]()

    def _start_battle(self, figure_1: Figure,  figure_2: Figure) -> Optional[str]:
        if not self.battle_ground:
            return None

        winner = self.battle_ground.battle(figure_1, figure_2)
        if not winner:
            return None

        return winner.name

    def area_battle(self, figure_1: Figure,  figure_2: Figure) -> Optional[str]:
        self.battle_ground = self._get_battle_ground_of_type('area')
        return self._start_battle(figure_1, figure_2)

    def circumference_battle(self, figure_1: Figure,  figure_2: Figure) -> Optional[str]:
        self.battle_ground = self._get_battle_ground_of_type('circumference')
        return self._start_battle(figure_1, figure_2)

    def relative_battle(self, figure_1: Figure,  figure_2: Figure) -> Optional[str]:
        self.battle_ground = self._get_battle_ground_of_type('relativity')
        return self._start_battle(figure_1, figure_2)

    @staticmethod
    def _get_total_winner(*winners: Optional[str], figure_1: Figure, figure_2: Figure) -> Figure:
        figure_1_wins = len(
            [w for w in winners if isinstance(w, str) and w == figure_1.name]
        )

        figure_2_wins = len(
            [w for w in winners if isinstance(w, str) and w == figure_2.name]
        )

        return figure_1 if figure_1_wins >= figure_2_wins else figure_2

    def _battle_round(self) -> None:
        winner_1, winner_2, winner_3, figure_1, figure_2 = \
            None, None, None, None, None

        figure_1 = self.figures.repository.pop(0)
        figure_2 = self.figures.repository.pop(0)

        winner_1 = self.area_battle(
            figure_1,
            figure_2
        )

        winner_2 = self.circumference_battle(
            figure_1,
            figure_2
        )

        if not (winner_1 and winner_2) \
                or (winner_1 != winner_2):
            winner_3 = self.relative_battle(
                figure_1,
                figure_2
            )

        total_winner = self._get_total_winner(
            winner_1,
            winner_2,
            winner_3,
            figure_1=figure_1,
            figure_2=figure_2
        )

        if total_winner:
            self.figures.add(total_winner)

    def total_battle(self) -> Figure:
        while True:
            if len(self.figures.repository) == 1:
                break

            self._battle_round()

        return self.figures.repository[0]

    def __str__(self) -> str:
        winner = self.total_battle()

        return f'The winner is:\n{str(winner)}'
