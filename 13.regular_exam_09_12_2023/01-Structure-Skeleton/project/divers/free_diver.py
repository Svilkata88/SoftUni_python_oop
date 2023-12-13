from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    def __init__(self, name):
        super().__init__(name, 120)
        self.__initial_oxygen_level = self.oxygen_level

    def miss(self, time_to_catch: int):
        if self.oxygen_level - int(time_to_catch * 0.6) < 0:
            self.oxygen_level = 0
            return
        self.oxygen_level -= int(time_to_catch * 0.6)
        if self.oxygen_level == 0:
            self.has_health_issue = True

    def renew_oxy(self):
        self.oxygen_level = self.__initial_oxygen_level

a_1 = FreeDiver('Peter')
a_1.miss(90)
print(a_1)
