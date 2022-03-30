import enum


class Unit_Type(enum.Enum):
    Army = "army"
    Fleet = "fleet"


class Unit:
    def __init__(self, unit_type: Unit_Type, owner):
        # TODO check unit type matches with tile type
        self.unit_type = unit_type
        self.owner = owner

    def get_unit_name(self):
        return self.unit_type.name

    def get_unit_type(self):
        return self.unit_type

    def get_owner(self):
        return self.owner

    def __repr__(self):
        return f"Unit is of type {self.unit_type.name} and is owned by: {self.owner}"
