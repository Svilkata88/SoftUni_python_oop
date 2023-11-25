from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    SPONSORS = {'Oracle': {1: 1500000, 2: 800000}, 'Honda': {1: 20000, 2: 10000}}
    EXPENSES = 250000
    revenue = 0

    def calculate_revenue_after_race(self, race_pos: int):
        sponsor_1 = RedBullTeam.SPONSORS['Oracle'][self.ranges(race_pos, 'Oracle')] if race_pos in range(1, 3) else 0
        sponsor_2 = RedBullTeam.SPONSORS['Honda'][self.ranges(race_pos, 'Honda')] if race_pos in range(1, 11) else 0

        def revenue():
            RedBullTeam.revenue = sponsor_1 + sponsor_2
            return RedBullTeam.revenue - RedBullTeam.EXPENSES

        self.budget += revenue()
        return f"The revenue after the race is {revenue()}$. Current budget {self.budget}$"

    @staticmethod
    def ranges(n: int, sponsor) -> int:
        result = 0
        if n == 1 and sponsor == 'Oracle':
            result = 1
        elif n == 2 and sponsor == 'Oracle':
            result = 2
        elif n in range(1, 9) and sponsor == 'Honda':
            result = 1
        elif n in range(9, 11) and sponsor == 'Honda':
            result = 2
        return result
