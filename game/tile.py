import enum
from game import unit


class Tile_Type(enum.Enum):
    Land = "land"
    Coast = "coast"
    Sea = "sea"


class Tile:
    def __init__(self, name: str, symbol: str, tile_type: Tile_Type, supply_depot: bool):
        self.tile_type = tile_type
        self.name = name
        self.symbol = symbol
        self.supply_depot = supply_depot
        self.connections = None
        self.unit = None

    def __repr__(self):
        connections_or_unit = ""
        if self.unit is not None:
            connections_or_unit += ", \n"
            connections_or_unit += f"A {self.unit.get_unit_name()} is stationed here"
        if self.connections is not None:
            connections_or_unit += ", \nThis tile is connected to "
            for tile in self.connections:
                connections_or_unit += f"{tile.name}, "

        return f"Name: {self.name}({self.symbol}), " \
               f"Type: {self.tile_type.name}, " \
               f"There is {'' if self.supply_depot else 'not '}a supply depot present" \
               f"{connections_or_unit}"

    def _deferred_init(self, connections):
        self.connections = connections
