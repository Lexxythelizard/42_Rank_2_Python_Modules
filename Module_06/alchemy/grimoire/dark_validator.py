#!/usr/bin/python3

from alchemy.grimoire.dark_spellbook import dark_spell_record

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    valid = "VALID"
    invalid = "INVALID"


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class DarkSpells:

    valid_ingredients: list[str]

    valid_ingredients = [
        "bats", "frogs", "arsenic", "eyeball"
    ]


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------

def validate_ingredients(ingredients: str) -> str:

    for el in ingredients.split():
        if el.lower() in DarkSpells.valid_ingredients:
            return (StringContainer.valid)
    return (StringContainer.invalid)


# ---------------------------- run ----------------------------


def main() -> None:
    dark_spell_record("Darkest spell ever", "bat arsenic")


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++


if __name__ == '__main__':

    main()
