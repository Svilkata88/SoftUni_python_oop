from typing import Dict


class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.mp = mp
        self.hp = hp
        self.name = name
        self.skills: Dict[str, int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill: str, mana_cost: int):
        if skill in self.skills:
            return "Skill already added"
        self.skills[skill] = mana_cost
        return f"Skill {skill} added to the collection of the player {self.name}"

    def player_info(self):
        info = [f'Name: {self.name}', f'Guild: {self.guild}', f'HP: {self.hp}', f'MP: {self.mp}']
        for skill, mana in self.skills.items():
            info.append(f'==={skill} - {mana}')
        return '\n'.join(info)
