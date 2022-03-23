class Player:
    def __init__(self, country, color, territory):
        self.country = country
        self.color = color
        self.territory = territory

    def __repr__(self):
        territory_str = ""
        for t in self.territory:
            territory_str += f"{t.name}, "
        return f"Player is playing as: {self.country}\n" \
               f"Represented by the color: {self.color}\n" \
               f"And controls: {territory_str[0:len(territory_str) - 2]}"
