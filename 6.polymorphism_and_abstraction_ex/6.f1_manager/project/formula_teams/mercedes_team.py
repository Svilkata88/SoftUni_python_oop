from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    SPONSORS = {'Petronas': {1: 1000000, 3: 500000}, 'TeamViewer': {5: 100000, 7: 50000}}
    EXPENSES = 200000
    revenue = 0

    def calculate_revenue_after_race(self, race_pos: int):
        sponsor_1 = MercedesTeam.SPONSORS['Petronas'][self.ranges(race_pos, 'Petronas')] if race_pos \
                                                                                     in range(1, 4) else 0
        sponsor_2 = MercedesTeam.SPONSORS['TeamViewer'][self.ranges(race_pos, 'TeamViewer')] if race_pos \
                                                                                      in range(1, 8) else 0

        def revenue():
            MercedesTeam.revenue = sponsor_1 + sponsor_2
            return MercedesTeam.revenue - MercedesTeam.EXPENSES

        self.budget += revenue()
        return f"The revenue after the race is {revenue()}$. Current budget {self.budget}$"

    @staticmethod
    def ranges(n: int, sponsor: str) -> int:
        result = 0
        if n == 1 and sponsor == 'Petronas':
            result = 1
        elif n in range(2, 4) and sponsor == 'Petronas':
            result = 3
        elif n in range(1, 6) and sponsor == 'TeamViewer':
            result = 5
        elif n in range(6, 8) and sponsor == 'TeamViewer':
            result = 7
        return result





