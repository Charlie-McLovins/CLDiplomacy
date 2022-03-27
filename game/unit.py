import enum
from game.tile import Tile


class Unit_Type(enum.Enum):
    Army = "army"
    Fleet = "fleet"


class Unit:
    def __init__(self, unit_type: Unit_Type, tile: Tile):
        # TODO check unit type matches with tile type
        self.unit_type = unit_type
        self.tile = tile

    def __repr__(self):
        return f"Unit is of type {self.unit_type.name} and is located on tile: {self.tile}"

