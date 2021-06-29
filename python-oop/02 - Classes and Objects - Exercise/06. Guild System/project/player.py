from typing import Dict


class Player:
    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str, int] = {}
        self.guild: str = 'Unaffiliated'

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and o.name == self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills:
            return 'Skill already added'
        self.skills[skill_name] = mana_cost
        return f'Skill {skill_name} added to the collection of the player {self.name}'
        
    def player_info(self) -> str:
        message = []
        nl = '\n'

        message.append(f'Name: {self.name}')
        message.append(f'Guild: {self.guild}')
        message.append(f'HP: {self.hp}')
        message.append(f'MP: {self.mp}')
        for skill, cost in self.skills.items():
            message.append(f'==={skill} - {cost}')
        return nl.join(message) + nl
