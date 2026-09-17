#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import ex0.obj as obj
import ex0.base as blueprint

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    spaceholder = "[Spaceholder]"


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class FlameFactory(blueprint.Factory):

    """
    Factory for Fire type Creatures
    """

    _base = obj.Flameling
    _evolved = obj.Pyrodon

    @classmethod
    def create_base(cls) -> obj.Flameling:
        return (cls._base())

    @classmethod
    def create_evolved(cls) -> obj.Pyrodon:
        return (cls._evolved())


class AquaFactory(blueprint.Factory):

    """
    Factory for Water type Creatures
    """

    _base = obj.Aquabub
    _evolved = obj.Torragon

    @classmethod
    def create_base(cls) -> obj.Aquabub:
        return (cls._base())

    @classmethod
    def create_evolved(cls) -> obj.Torragon:
        return (cls._evolved())
