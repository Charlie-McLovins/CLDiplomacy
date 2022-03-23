import enum

from mapping.utils.parser import Parser


class Map:
    def __init__(self, path):
        self.parser = Parser(path)
        self.countries = []
        self.tiles = []
        self._load()
        # for t in self.tiles:
        #     print(t)
        # for c in self.countries:
        #     print(c)

    def _load(self):
        tiles = self.parser.get_attribute("tiles")
        for _, v in tiles.items():
            self.tiles.append(Tile(v["name"], v["symbol"], v["tile_type"], v["connections"]))
        # print(self.validate_load())
        countries = self.parser.get_attribute("countries")
        for _, v in countries.items():
            territory = []
            for n in v["territory"]:
                territory.append(self.get_tile(n))
            self.countries.append(Country(v["display_name"], v["color"], territory))

    def get_tile(self, name):
        for tile in self.tiles:
            if tile.name == name:
                return tile
            if tile.sym == name:
                return tile
        return None

    def get_tiles(self):
        tiles = []
        for t in self.tiles:
            tiles.append(t.name)
        return tiles

    def get_country(self, country):
        for c in self.countries:
            if c == country:
                return c
        return None


class Country:
    def __init__(self, display_name, color, territory):
        self.display_name = display_name
        self.color = color
        self.territory = territory

    def __repr__(self):
        return f"Name: {self.display_name}, Color: {self.color}, Territory: {self.territory}"

    def __eq__(self, other):
        if type(other) is Country:
            return other.display_name == self.display_name
        else:
            return other == self.display_name


class Tile:
    def __init__(self, name, sym, tile_type, connections):
        # Initial Map setup, Map info
        self.name = name
        self.sym = sym
        self.tile_type = tile_type
        self.connections = []
        for c in connections:
            self.connections.append(c)
        # Setup Phase 2, Owner info
        self.owner = None
        self.color = None
        self.unit = None
        self.supply_depot = None
        self.home_depot = None

    def __repr__(self):
        info = str(
            f"Name: {self.name}, Symbol: {self.sym}, Tile Type: {self.tile_type}, Connections: {self.connections}")
        if self.owner is not None:
            info += str(
                f"\nOwner: {self.owner}, Color: {self.color}, Unit: {self.unit}, Supply Depot: {self.supply_depot}, Home Depot{self.home_depot}")

        return info

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.sym

    def get_connections(self):
        return self.connections

    def check_connection(self, connection):
        if isinstance(connection, str):
            return connection in self.connections
        return connection.sym in self.connections

    def set_owner(self, country):
        self._set_owner(country.name, country.color, Unit.Empty, False)

    def _set_owner(self, owner, color, unit, supply_depot, home_depot=False):
        self.owner = owner
        self.color = color
        self.unit = unit
        self.supply_depot = supply_depot
        self.home_depot = home_depot

    def get_owner(self):
        return self.owner


class Tile_Type(enum.Enum):
    Land = "land"
    Coast = "coast"
    Sea = "sea"


class Unit(enum.Enum):
    Empty = "empty"
    Army = "army"
    Fleet = "fleet"
