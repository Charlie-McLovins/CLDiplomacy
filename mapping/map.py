import json


def load(path):
    with open(path) as file:
        decoder = json.JSONDecoder()
        return decoder.raw_decode(json.dumps(file.read()))

class Map:
    def __init__(self):
        map = load("resources\\test.json")
        print("test")
        print(map)
        print("\n")
        print("test")
        print(type(map.__class__))

