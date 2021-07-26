from project.player.player import Player


class BattleField:
    beginner_hp_bonus = 40

    def fight(self, attacker: Player, enemy: Player):
        """
        •	If one of the users is_dead, raise new ValueError with message "Player is dead!"

        •	If a player is a beginner, increase his health with 40 points and 
            increase the damage points of each card in the players' deck with 30.

        •	Before the fight, both players get bonus health points from their deck. 
            (sum of all health points of his cards)

        •	Attacker attacks first and after that the enemy attacks 
            (deal damage points to opponent for each card). 
            If one of the players is dead, you should stop the fight.
        """

        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        attacker.apply_bonus(), enemy.apply_bonus()

        enemy.take_damage(attacker.damage_points)
        if enemy.is_dead:
            raise ValueError("Player is dead!")

        attacker.take_damage(enemy.damage_points)
        if attacker.is_dead:
            raise ValueError("Player is dead!")
