from typing import List


MAX_HP = 100
MAX_MP = 200


class Hero:
    """Each hero has name(str), health points(hp: int) and mana points (mp: int)
    """

    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name: str = name
        self.hp: int = hp
        self.mp: int = mp

    def get_hp(self) -> int:
        """Returns the Health value

        Returns:
            int: hp value
        """
        return self.hp

    def get_mp(self) -> int:
        """Returns the Mana value

        Returns:
            int: mp value
        """
        return self.mp

    def set_hp(self, v: int):
        """Sets the Health value

        Args:
            v (int): new health value
        """
        self.hp = v

    def set_mp(self, v: int):
        """Sets the Mana value

        Args:
            v (int): new mana value
        """
        self.mp = v

    def __repr__(self) -> str:
        """Text representation of the object. For debugging only

        Returns:
            str: Object attributes
        """
        return f'{self.name}|{self.hp}|{self.mp}'

    def cast_spell(self, mp_needed: int, spell: str) -> str:
        """If the hero has the required MP, he casts the spell, thus reducing his MP

        Args:
            mp_needed (int): Mana points needed to cast the spell
            spell (str): Name of the spell

        Returns:
            str: Message to print after the command
        """
        if self.mp >= mp_needed:
            new_mp = self.mp - mp_needed
            self.set_mp(new_mp)
            return f'{self.name} has successfully cast {spell} and now has {self.mp} MP!'
        return f'{self.name} does not have enough MP to cast {spell}!'

    def take_damage(self, damage: int, attacker: str) -> tuple:
        """Reduce the hero HP by the given damage amount. If the hero has died, remove him from your party

        Args:
            damage (int): Damage points taken
            attacker (str): Name of the Attacker

        Returns:
            tuple: killed: bool, Message to print
        """
        if self.hp < damage:
            self.hp = damage
        new_hp = self.hp - damage
        self.set_hp(new_hp)
        if self.get_hp() == 0:
            return True, f'{self.name} has been killed by {attacker}!'
        return False, f'{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!'

    def recharge(self, charge: int) -> str:
        """The hero increases his MP.

        Args:
            charge (int): Mana recharge value

        Returns:
            str: Message to print
        """
        if self.mp + charge > MAX_MP:
            charge = MAX_MP - self.mp
        new_mp = self.mp + charge
        self.set_mp(new_mp)
        return f'{self.name} recharged for {charge} MP!'

    def heal(self, amount: int) -> str:
        """The hero increases his HP

        Args:
            amount (int): Heal value

        Returns:
            str: Message to print
        """
        if self.hp + amount > MAX_HP:
            amount = MAX_HP - self.hp
        new_hp = self.hp + amount
        self.set_hp(new_hp)
        return f'{self.name} healed for {amount} HP!'


class Game:
    def __init__(self) -> None:
        """Creates blank list for storing Hero objects"""
        self.heroes: List[Hero] = []

    def create_hero(self, name: str,  hp: int, mp: int) -> None:
        """Creates a Hero object and append it to the list of heroes

        Args:
            name (str): name of the Hero
            hp (int): health points of the Hero
            mp (int): mana points of the Hero
        """
        hp = hp if hp < MAX_HP else MAX_HP
        mp = mp if mp < MAX_MP else MAX_MP
        self.heroes.append(Hero(name, hp, mp))

    def action(self, command: str, name: str, tokens: list) -> str:
        """Execute the command

        Args:
            command (str): Command to execute
            name (str): Name of the hero
            tokens (list): complimentary data for the execution of the command

        Returns:
            str: Message to be printed after execution of the command
        """
        if command == 'CastSpell':
            if len(tokens) != 2:
                return f'Invalid input'
            mp_needed, spell = tokens
            mp_needed = int(mp_needed)
            for h in self.heroes:
                if h.name == name:
                    return h.cast_spell(mp_needed, spell)

        elif command == 'TakeDamage':
            if len(tokens) != 2:
                return f'Invalid input'
            damage, attacker = tokens
            damage = int(damage)
            for i, h in enumerate(self.heroes):
                if h.name == name:
                    killed, message = h.take_damage(damage, attacker)
                    if killed:
                        self.heroes.pop(i)
                    return message

        elif command == 'Recharge':
            if len(tokens) != 1:
                return f'Invalid input'
            charge = int(''.join(tokens))
            for h in self.heroes:
                if h.name == name:
                    return h.recharge(charge)

        elif command == 'Heal':
            if len(tokens) != 1:
                return f'Invalid input'
            amount = int(''.join(tokens))
            for h in self.heroes:
                if h.name == name:
                    return h.heal(amount)

        return f'Invalid input'

    def __repr__(self) -> str:
        result = []
        nl = '\n'
        for hero in sorted(self.heroes, key=lambda x: (-x.hp, x.name)):
            result.append(f'{hero.name}')
            result.append(f'  HP: {hero.hp}')
            result.append(f'  MP: {hero.mp}')
        return nl.join(result)


g = Game()
n = int(input())

for _ in range(n):
    data = input()
    name, hp, mp = data.split()
    hp, mp = int(hp), int(mp)
    g.create_hero(name, hp, mp)

while True:
    data = input()
    if data == 'End':
        break
    command, name, *tokens = data.split(' - ')
    print(g.action(command, name, tokens))

print(g)
