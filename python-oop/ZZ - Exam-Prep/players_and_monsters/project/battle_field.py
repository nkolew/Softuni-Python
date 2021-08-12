from project.player.player import Player


class BattleField:
    @staticmethod
    def fight(attacker: Player, enemy: Player) -> None:
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        attacker.apply_bonus(), enemy.apply_bonus()

        attacker.attack(enemy)
        if enemy.is_dead:
            return

        enemy.attack(attacker)
        if attacker.is_dead:
            return
