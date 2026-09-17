#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
from ex0.base import Creature

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    spaceholder = "[Spaceholder]"

    attack = "%s uses %s!"


# ---------------------------- creature settings ----------------------------


class BaseCreatureValues:

    aquabub = ("Aquabub", "Water")
    flameling = ("Flameling", "Fire")


class EvolvedCreatureValues:

    torragon = ("Torragon", "Water")
    pyrodon = ("Pyrodon", "Fire")


class AttackContainer:

    lvl_0_water = "Water Gun"
    lvl_1_water = "Hydro Pump"

    lvl_0_fire = "Ember"
    lvl_1_fire = "Flamethrower"


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class Flameling(Creature):

    """
    lvl 0 fire creature
    """

    def __init__(self) -> None:

        name: str
        typus: str

        name, typus = BaseCreatureValues.flameling
        super().__init__(name=name, typus=typus)

    def attack(self, opponent: typing.Any = None) -> str:

        if (isinstance(opponent, Creature)):
            opponent.defend()

        return (
            StringContainer.attack %
            (super().__name, AttackContainer.lvl_0_fire)
        )
