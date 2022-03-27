import enum


class Tile:
    def __init__(self, type, connections, name, symbol, supply_depot, unit):
        self.type = type
        self.connections = connections
        self.name = name
        self.symbol = symbol
        self.supply_depot = supply_depot
        self.unit = unit


class Tile_Type(enum.Enum):
    Land = "land"
    Coast = "coast"
    Sea = "sea"
