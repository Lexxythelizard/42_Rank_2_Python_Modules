#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import ex1.obj as obj
import ex0.base as blueprint

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    spaceholder = "[Spaceholder]"


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class HealingCreatureFactory(blueprint.CreatureFactory):

    """
    Factory for Creatures with healing abillities
    """

    _base = obj.Sproutling
    _evolved = obj.Bloomelle

    @classmethod
    def create_base(cls) -> obj.Sproutling:
        return (cls._base())

    @classmethod
    def create_evolved(cls) -> obj.Bloomelle:
        return (cls._evolved())


class TransformCreatureFactory(blueprint.CreatureFactory):

    """
    Factory for Creatures with transform abillities
    """

    _base = obj.Shiftling
    _evolved = obj.Morphagon

    @classmethod
    def create_base(cls) -> obj.Shiftling:
        return (cls._base())

    @classmethod
    def create_evolved(cls) -> obj.Morphagon:
        return (cls._evolved())
