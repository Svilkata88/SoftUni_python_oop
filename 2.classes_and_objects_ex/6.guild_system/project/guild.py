from typing import List
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, _player: str):
        if _player in list(map(lambda _player: _player.name, self.players)):
            for obj in self.players:
                if obj.name == _player:
                    self.players.remove(obj)
                    obj.guild = "Unaffiliated"
                    return f"Player {_player} has been removed from the guild."
        return f'Player {_player} is not in the guild.'

    def guild_info(self):
        info = [f'Guild: {self.name}']
        for el in self.players:
            info.append(el.player_info())
        return '\n'.join(info)


player = Player("George", 50, 100)
print(player.player_info())
guild_1 = Guild(f'Storms')
guild_1.assign_player(player)
guild_1.kick_player('George')
print()
print(guild_1.guild_info())
