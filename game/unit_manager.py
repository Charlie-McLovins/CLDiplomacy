from mapping.game_map import Unit_Type, Game_Map
from game.player import Player


class Unit_Manager:
    def __init__(self, game_map: Game_Map, players):
        self.map = game_map
        self.players = players

    def execute_moves(self, **moves):
        for k, v in moves.items():
            print(f"Key: {k}, Value: {v}")
