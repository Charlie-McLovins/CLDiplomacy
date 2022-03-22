import json
from mapping import map


class Parser:
    def __init__(self):
        pass

    def load(self, path):
        with open(path) as file:
            print(json.dumps(file))
