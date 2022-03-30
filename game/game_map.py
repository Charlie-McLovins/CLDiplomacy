from game.tile import Tile, Tile_Type
from game.player import Player
from game.unit import Unit, Unit_Type

_TILES = [
    ["One", "1", Tile_Type.Land, True],
    ["Two", "2", Tile_Type.Coast, False],
    ["Three", "3", Tile_Type.Sea, True],
    ["Four", "4", Tile_Type.Coast, True]
]

def _jank_tile_extractor(index):
    return Tile(_TILES[index][0], _TILES[index][1], _TILES[index][2], _TILES[index][3])

class Game_Map:
    def __init__(self):
        self.tiles = []
        # self.players = []
        # self.units = []

        for item in _TILES:
            self._jank_load(len(self.tiles))
        # TODO load from map file

        self.tiles[0].connections = [self.tiles[1], self.tiles[3]]
        self.tiles[1].connections = [self.tiles[0], self.tiles[2]]
        self.tiles[2].connections = [self.tiles[1], self.tiles[3]]
        self.tiles[3].connections = [self.tiles[0], self.tiles[2]]


        # self.players.append(Player([
        #     Unit(Unit_Type.Army, self.tiles[0])
        # ]))

    

    def _jank_load(self, index):
        self.tiles.append(_jank_tile_extractor(index))

    def __repr__(self):
        string = ""

        for tile in self.tiles:
            string += f"{tile}\n"

        # string += "\n\n\n"

        # for player in self.players:
        #     string += f"{player}\n"

        return string
