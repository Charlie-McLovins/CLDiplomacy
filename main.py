from game.player import Player
from game.unit_manager import Unit_Manager
from mapping.game_map import Game_Map
from random import Random


def main():
    game_map = Game_Map("resources\\test2.json")
    players = init_players(game_map)
    unit_manager = Unit_Manager(game_map, players)


    selected_country = None

    while selected_country is None:
        countries = game_map.countries
        countries_str = "Available Countries are: "
        for c in countries:
            countries_str += f"{c.display_name}, "
        print(countries_str[0: len(countries_str) - 4])
        selection = input("Please select a Country: ")
        if selection in ["quit", "q", ""]:
            return
        selected_country = game_map.get_country(selection)

    print(f"You have selected: {selected_country.display_name}")
    tile = Random().choice(selected_country.territory)
    while True:
        connections = tile.get_connections()
        f_connections = ""
        for c in connections:
            t = game_map.get_tile(c)
            f_connections += f"{t.name} ({t.sym}), "
        f_connections = f_connections[0:len(f_connections) - 2]
        print(f"Currently located in: {tile.name}\n"
              f"Can move to: {f_connections}")
        user_input = input("Choose tile to move too: ")
        if user_input in ["quit", "q", ""]:
            return
        if user_input in ["help", "h", "--help", "-h"]:
            print("this is where help should go")
            continue
        if tile.check_connection(user_input):
            tile = game_map.get_tile(user_input)
            continue
        else:
            print("Tile or command unrecognized; Try again")


def init_players(game_map: Game_Map):
    players = []
    for country in game_map.countries:
        if country.display_name == "":
            continue
        players.append(Player(country.display_name, country.color, country.territory))
    return players

if __name__ == "__main__":
    main()
