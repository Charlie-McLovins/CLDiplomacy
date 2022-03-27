from game.unit import Unit


class Player:
    def __init__(self, units: []):
        # Class variables
        self.units = []

        # Type Checking for units array
        for unit in units:
            if not isinstance(unit, Unit):
                raise TypeError("Unit must be of type Unit")
            self.units.append(unit)

    def __repr__(self):
        string = ""

        for unit in self.units:
            string += f"{unit}\n"

        return string

