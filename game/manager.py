from game.player import Player
from game.game_map import Game_Map

class Manager:
    def __init__(self):
        self.game_map = None
        self.players = []
        self._game_won = False

    def register_game_map(self, game_map: Game_Map):
        if self.game_map is None:
            self.game_map = game_map
        else:
            print("Map has already been registered")

    def register_player(self, player: Player):
        if self.players.index(player) == -1:
            self.players.append(player)
        else:
            print("Player has already been registered")

    def get_moves(self):
        for player in self.players:
            for unit in player.units

    def force_winner(self):
        self._game_won = True

    def _check_winner(self):
        pass

    def get_winner(self):
        self._check_winner()
        return self._game_won
