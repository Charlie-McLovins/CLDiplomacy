from game.game_map import Game_Map
from game.manager import Manager


GM = Game_Map()
MANAGER = Manager()
MANAGER.register_game_map(GM)
print(GM)
