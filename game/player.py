class Player:
    def __init__(self, country, color, territory, ai=True):
        self.country = country
        self.color = color
        self.territory = territory
        self.ai = ai

    def __repr__(self):
        territory_str = ""
        for t in self.territory:
            territory_str += f"{t.name}, "
        return f"Player is playing as: {self.country}\n" \
               f"Represented by the color: {self.color}\n" \
               f"And controls: {territory_str[0:len(territory_str) - 2]}"

    def get_move(self):
        return self._get_move_ai() if self.ai else self._get_move_player()

    def _get_move_player(self):
        return ""

    def _get_move_ai(self):
        return ""

    def take_control(self):
        self.ai = False
