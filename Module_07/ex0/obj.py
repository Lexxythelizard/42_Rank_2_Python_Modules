#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
from ex0.base import Creature

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    spaceholder = "[Spaceholder]"

    attack = "%s uses %s%s!"


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

        aim: str

        if (isinstance(opponent, Creature)):
            aim = " against %s" % opponent.describe().split()[0]
        else:
            aim = " against %s" % str(opponent) if opponent else ""

        return (
            StringContainer.attack %
            (self.describe().split()[0], AttackContainer.lvl_0_fire, aim)
        )


class Aquabub(Creature):

    """
    lvl 0 water creature
    """

    def __init__(self) -> None:

        name: str
        typus: str

        name, typus = BaseCreatureValues.aquabub
        super().__init__(name=name, typus=typus)

    def attack(self, opponent: typing.Any = None) -> str:

        aim: str

        if (isinstance(opponent, Creature)):
            aim = " against %s" % opponent.describe().split()[0]
        else:
            aim = " against %s" % str(opponent) if opponent else ""

        return (
            StringContainer.attack %
            (self.describe().split()[0], AttackContainer.lvl_0_water, aim)
        )


class Pyrodon(Creature):

    """
    lvl 1 fire creature
    """

    def __init__(self) -> None:

        name: str
        typus: str

        name, typus = EvolvedCreatureValues.pyrodon
        super().__init__(name=name, typus=typus)

    def attack(self, opponent: typing.Any = None) -> str:

        aim: str

        if (isinstance(opponent, Creature)):
            aim = " against %s" % opponent.describe().split()[0]
        else:
            aim = " against %s" % str(opponent) if opponent else ""

        return (
            StringContainer.attack %
            (self.describe().split()[0], AttackContainer.lvl_1_fire, aim)
        )


class Torragon(Creature):

    """
    lvl 1 water creature
    """

    def __init__(self) -> None:

        name: str
        typus: str

        name, typus = EvolvedCreatureValues.torragon
        super().__init__(name=name, typus=typus)

    def attack(self, opponent: typing.Any = None) -> str:

        aim: str

        if (isinstance(opponent, Creature)):
            aim = " against %s" % opponent.describe().split()[0]
        else:
            aim = " against %s" % str(opponent) if opponent else ""

        return (
            StringContainer.attack %
            (self.describe().split()[0], AttackContainer.lvl_1_water, aim)
        )
