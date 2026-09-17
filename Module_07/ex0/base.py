#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import abc
import typing

# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------

class StringContainer:

    spaceholder = "[Spaceholder]"
    description = "%s is a %s type Creature"
    object_str = "Creature: {name: %s, type: %s}"
    attack = "%s uses %s!"

# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++

# ---------------------------- abstr/par ----------------------------


class Creature(abc.ABC):

    """
    Generic Creature
    """

    __name: str = "Gen Creature"
    __type: str = "gen Type"

    def __init__(self, name: str = "", typus: str = "") -> None:

        if (not isinstance(name, str)):
            raise TypeError(StringContainer.spaceholder)
        if (not isinstance(typus, str)):
            raise TypeError(StringContainer.spaceholder)
        if (name):
            self.__name = name
        if (typus):
            self.__type = typus

    def __str__(self) -> str:
        return (StringContainer.object_str % (self.__name, self.__type))

    def describe(self) -> str:
        return (StringContainer.description % (self.__name, self.__type))

    @abc.abstractmethod
    def attack(self, opponent: typing.Any = None) -> str:
        pass


class Factory(abc.ABC):

    """
    Generic Factory
    """

    @classmethod
    @abc.abstractmethod
    def create_base(cls) -> Creature:
        pass

    @classmethod
    @abc.abstractmethod
    def create_evolved(cls) -> Creature:
        pass
