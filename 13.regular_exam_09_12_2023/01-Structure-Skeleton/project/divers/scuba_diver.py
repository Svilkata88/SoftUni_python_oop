from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    def __init__(self, name):
        super().__init__(name, 540)
        self.__initial_oxygen_level = self.oxygen_level

    def miss(self, time_to_catch: int):
        if self.oxygen_level - int(time_to_catch * 0.3) < 0:
            self.oxygen_level = 0
            return
        self.oxygen_level -= int(time_to_catch * 0.3)
        if self.oxygen_level == 0:
            self.has_health_issue = True

    def renew_oxy(self):
        self.oxygen_level = self.__initial_oxygen_level
