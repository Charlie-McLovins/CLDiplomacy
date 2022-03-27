from game.tile import Tile, Tile_Type
from game.player import Player
from game.unit import Unit, Unit_Type


class Game_Map:
    def __init__(self):
        self.tiles = []
        self.players = []
        self.units = []

        # TODO load from map file
        self.tiles.append(Tile("One", "1", Tile_Type.Land, True))
        self.tiles.append(Tile("Two", "2", Tile_Type.Coast, False))
        self.tiles.append(Tile("Three", "3", Tile_Type.Sea, True))
        self.tiles.append(Tile("Four", "4", Tile_Type.Coast, True))

        self.tiles[0].connections = [self.tiles[1], self.tiles[3]]
        self.tiles[1].connections = [self.tiles[0], self.tiles[2]]
        self.tiles[2].connections = [self.tiles[1], self.tiles[3]]
        self.tiles[3].connections = [self.tiles[0], self.tiles[2]]

        self.players.append(Player([
            Unit(Unit_Type.Army, self.tiles[0])
        ]))

    def __repr__(self):
        string = ""

        for tile in self.tiles:
            string += f"{tile}\n"

        string += "\n\n\n"

        for player in self.players:
            string += f"{player}\n"

        return string
