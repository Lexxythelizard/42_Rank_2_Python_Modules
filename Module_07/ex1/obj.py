#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
from ex0.base import Creature
from ex1.base import HealCapability, TransformCapability

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    spaceholder = "[Spaceholder]"

    attack = "%s uses %s%s!"
    heal = "%s uses %s %s!"


# ---------------------------- creature settings ----------------------------


class BaseCreatureValues:

    sproutling = ("Sproutling", "Grass")
    shiftling = ("Shiftling", "Normal")


class EvolvedCreatureValues:

    bloomelle = ("Bloomelle", "Grass/Fairy")
    morphagon = ("Morphagon", "Normal/Dragon")


class MorpContainer:

    lvl_0_morph = "%s shifts into a sharper form!"
    lvl_1_morph = "%s morphs into a dragonic battle form!"

    lvl_0_unmorph = "%s returns to normal"
    lvl_1_unmorph = "%s stabilizes its form."


class AttackContainer:

    lvl_0_grass = "Vine Whip"
    lvl_1_grass = "Petal Dance"

    lvl_0_normal = "%s attacks%s normally"
    lvl_1_normal = "%s attacks%s normally"

    lvl_0_heal = "a small amount"
    lvl_1_heal = "a large amount"

    lvl_0_morphed = "performs a boosted strike"
    lvl_1_morphed = "unleashes a devastating morph strike"

# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class Sproutling(Creature, HealCapability):

    """
    lvl 0 grass creature
    """

    def __init__(self) -> None:

        name: str
        typus: str

        name, typus = BaseCreatureValues.sproutling
        super().__init__(name=name, typus=typus)

    def attack(self, opponent: typing.Any = None) -> str:

        aim: str

        if (isinstance(opponent, Creature)):
            aim = " against %s" % opponent.name
        else:
            aim = " against %s" % str(opponent) if opponent else ""

        return (
            StringContainer.attack %
            (self.name, AttackContainer.lvl_0_grass, aim)
        )

    def heal(self, target: typing.Any = None) -> str:

        aim: str

        if (isinstance(target, Creature)):
            aim = target.name
        else:
            aim = str(target) if target else "itself"

        return (
            StringContainer.heal %
            (self.name, AttackContainer.lvl_0_heal, aim)
        )


class Bloomelle(Creature, HealCapability):

    """
    lvl 1 grass and fairy creature
    """

    def __init__(self) -> None:

        name: str
        typus: str

        name, typus = EvolvedCreatureValues.bloomelle
        super().__init__(name=name, typus=typus)

    def attack(self, opponent: typing.Any = None) -> str:

        aim: str

        if (isinstance(opponent, Creature)):
            aim = " against %s" % opponent.name
        else:
            aim = " against %s" % str(opponent) if opponent else ""

        return (
            StringContainer.attack %
            (self.name, AttackContainer.lvl_1_grass, aim)
        )

    def heal(self, target: typing.Any = None) -> str:

        aim: str

        if (isinstance(target, Creature)):
            aim = target.name
        else:
            aim = str(target) if target else "itself"

        return (
            StringContainer.heal %
            (self.name, AttackContainer.lvl_1_heal, aim)
        )


class Shiftling(Creature, TransformCapability):

    """
    lvl 0 normal creature, is capable of transforming abillities
    """

    _transformed: bool

    def __init__(self) -> None:

        name: str
        typus: str

        name, typus = BaseCreatureValues.shiftling
        super().__init__(name=name, typus=typus)
        self._transformed = False

    def attack(self, opponent: typing.Any = None) -> str:

        aim: str

        if (isinstance(opponent, Creature)):
            aim = " %s" % opponent.name
        else:
            aim = " %s" % str(opponent) if opponent else ""

        if (self._transformed):
            return ((self.name + AttackContainer.lvl_0_morphed + aim + '!'))
        else:
            return (AttackContainer.lvl_0_normal % (self.name, aim))

    def transform(self) -> str:
        self._transformed = True
        return (MorpContainer.lvl_0_morph % self.name)

    def revert(self) -> str:
        self._transformed = False
        return (MorpContainer.lvl_0_unmorph % self.name)


class Morphagon(Creature, TransformCapability):

    """
    lvl 1 normal creature, is capable of transforming abillities
    """

    _transformed: bool

    def __init__(self) -> None:

        name: str
        typus: str

        name, typus = EvolvedCreatureValues.morphagon
        super().__init__(name=name, typus=typus)
        self._transformed = False

    def attack(self, opponent: typing.Any = None) -> str:

        aim: str

        if (isinstance(opponent, Creature)):
            aim = " %s" % opponent.name
        else:
            aim = " %s" % str(opponent) if opponent else ""

        if (self._transformed):
            return ((self.name + AttackContainer.lvl_1_morphed + aim + '!'))
        else:
            return (AttackContainer.lvl_1_normal % (self.name, aim))

    def transform(self) -> str:
        self._transformed = True
        return (MorpContainer.lvl_1_morph % self.name)

    def revert(self) -> str:
        self._transformed = False
        return (MorpContainer.lvl_1_unmorph % self.name)
