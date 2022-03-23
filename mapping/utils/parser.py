import json
from mapping import map


class Parser:
    def __init__(self, path):
        self.path = path
        self.data = None
        self.countries = []
        self.load()

    def load(self):
        with open(self.path) as file:
            self.data = json.loads(file.read())
        #self.debug()
        self.countries = self.data["countries"]

    def get_data(self):
        return self.data

    def get_attribute(self, attribute):
        return self.data[attribute]

    def debug(self):
        # print(self.data)
        #print(type(self.data))
        for t in self.data:
            #print(f"{t}\n{type(t)}\n\n{self.data[t]}\n{type(self.data[t])}\n\n")
            #print(f"{type(self.data)}{type(t)}")
            c_dict = self.data[t]
            # print(c_dict)
            # print(f"Type of c_dict:{type(c_dict)}")
            for c in c_dict:
                if isinstance(c_dict, dict):
                    print(c_dict[c])
                # print(f"{type(c_dict)}{type(c)}")
                # print(c)
                # print(type(c))
            # for s in c_dict:
            #     print(s)
            #     print(type(s))
                #print(f"{s}\n{type(s)}\n\n{self.data[t][s]}\n{type(self.data[t][s])}\n\n")
