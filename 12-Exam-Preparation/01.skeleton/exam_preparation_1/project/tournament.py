from typing import List
from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {"KneePad": KneePad,  "ElbowPad": ElbowPad}
    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam , "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception("Invalid equipment type!")
        new_equipment = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")
        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."
        new_team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)
        equipment = next((e for e in reversed(self.equipment) if e.__class__.__name__ == equipment_type), None)
        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)
        if team not in self.teams:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        count = [e.increase_price() for e in self.equipment if e.__class__.__name__ == equipment_type]
        return f"Successfully changed {len(count)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = next((t for t in self.teams if t.name == team_name1), None)
        team_2 = next((t for t in self.teams if t.name == team_name2), None)

        if team_1.__class__.__name__ != team_2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        total_points_team_1 = team_1.advantage + sum([points.protection for points in team_1.equipment])
        total_points_team_2 = team_2.advantage + sum([points.protection for points in team_2.equipment])

        if total_points_team_1 > total_points_team_2 or total_points_team_1 < total_points_team_2:
            team_1.win() if total_points_team_1 > total_points_team_2 else team_2.win()
            return f"The winner is {team_1.name if total_points_team_1 > total_points_team_2 else team_2.name}."
        return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda team: -team.wins)
        result = [f'Tournament: {self.name}', f'Number of Teams: {len(self.teams)}', 'Teams:']
        [result.append(t.get_statistics()) for t in sorted_teams]
        return '\n'.join(result)

