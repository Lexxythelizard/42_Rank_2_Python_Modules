#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import abc
import typing

# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------

class StringContainer:

    spaceholder = "[Spaceholder]"

# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++

# ---------------------------- abstr/par ----------------------------


class HealCapability(abc.ABC):

    """
    Heal Capability
    """

    __name: str = "Heal Capabillity"

    def __str__(self) -> str:
        return (self.__name)

    @abc.abstractmethod
    def heal(self, target: typing.Any = None) -> str:
        pass


class TransformCapability(abc.ABC):

    """
    Transform Capability
    """

    __name: str = "Transform Capabillity"

    def __str__(self) -> str:
        return (self.__name)

    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass
