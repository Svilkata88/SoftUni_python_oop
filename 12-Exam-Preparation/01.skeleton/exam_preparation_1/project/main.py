from project.tournament import Tournament

t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 200))
print(t.add_team('OutdoorTeam', 'Pirin', 'BG', 200))
print(t.sell_equipment('KneePad', 'Levski'))
print(t.sell_equipment('KneePad', 'Pirin'))
print(t.sell_equipment('ElbowPad', 'Levski'))
print(t.sell_equipment('ElbowPad', 'Pirin'))

print(t.play('Levski', 'Pirin'))
print(t.get_statistics())