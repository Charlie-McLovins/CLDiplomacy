import sys

from mapping.map import Map
from random import Random


def main():
    map = Map("resources\\test2.json")
    tile = map.get_tile(Random().choice(map.get_tiles()))
    while True:
        connections = tile.get_connections()
        f_connections = ""
        for c in connections:
            t = map.get_tile(c)
            f_connections += f"{t.name} ({t.sym}), "
        f_connections = f_connections[0:len(f_connections) - 2]
        print(f"Currently located in: {tile.name}\n"
              f"Can move to: {f_connections}")
        user_input = input("Choose tile to move too: ")
        if user_input in ["quit", "q", ""]:
            break
        if user_input in ["help", "h", "--help", "-h"]:
            print("this is where help should go")
            continue
        if tile.check_connection(user_input):
            tile = map.get_tile(user_input)
            continue
        else:
            print("Tile or command unrecognized; Try again")

if __name__ == "__main__":
    main()
