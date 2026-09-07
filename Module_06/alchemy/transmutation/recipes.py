#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import alchemy as alchm
import elements as pri_elements
import alchemy.elements as sec_elements

# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------

class StringContainer:

    lead_to_gold = "Recipe transmuting Lead to Gold:"
    lead_to_gold += " brew ’%s’ and ’%s’ mixed with ’%s’"

# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++

# ---------------------------- abstr/par ----------------------------

# class

# ---------------------------- child ----------------------------

# class

# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------

def lead_to_gold() -> str:

    return (
        StringContainer.lead_to_gold %
        (
            sec_elements.create_air(),
            alchm.strength_potion(),
            pri_elements.create_fire())
        )


# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:
    pass


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
