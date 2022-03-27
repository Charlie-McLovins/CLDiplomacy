import enum


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

    def __repr__(self):
        return f"Name: {self.name}({self.symbol}), " \
               f"Type: {self.tile_type.name}, " \
               f"There is {'' if self.supply_depot else 'not '}a supply depot present"

    def deferred_init(self, connections):
        self.connections = connections
