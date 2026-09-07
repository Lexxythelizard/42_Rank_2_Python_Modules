#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import elements as pri_elements
import alchemy.elements as sec_elements

# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------

class StringContainer:

    brew_healing = "Healing potion brewed with ’%s’ and ’%s’"
    brew_strength = "Strength potion brewed with '%s' and '%s'"

# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++

# ---------------------------- abstr/par ----------------------------

# class

# ---------------------------- child ----------------------------

# class

# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------

def healing_potion() -> str:

    return (
        StringContainer.brew_healing %
        (sec_elements.create_earth(), sec_elements.create_air())
        )


def strength_potion() -> str:

    return (
        StringContainer.brew_strength %
        (pri_elements.create_fire(), pri_elements.create_water())
        )

# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:
    pass


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
