from typing import List
from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISHES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVERS:
            return f"{diver_type} is not allowed in our competition."
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if diver:
            return f"{diver_name} is already a participant."
        diver = self.VALID_DIVERS[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISHES:
            return f"{fish_type} is forbidden for chasing in our competition."
        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if fish:
            return f"{fish_name} is already permitted."
        fish = self.VALID_FISHES[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if not diver:
            return f"{diver_name} is not registered for the competition."
        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."
        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."
        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_with_health_issue = [d for d in self.divers if d.has_health_issue]
        for d in divers_with_health_issue:
            d.update_health_status()
            d.renew_oxy()
        return f"Divers recovered: {len(divers_with_health_issue)}"

    def diver_catch_report(self, diver_name: str):
        diver = next(d for d in self.divers if d.name == diver_name)
        result = [f"**{diver_name} Catch Report**"]
        for f in diver.catch:
            result.append(f.fish_details())
        return '\n'.join(result)

    def competition_statistics(self):
        divers_without_health_issue = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(divers_without_health_issue, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        result = ['**Nautical Catch Challenge Statistics**']
        for d in sorted_divers:
            result.append(str(d))
        return '\n'.join(result)
