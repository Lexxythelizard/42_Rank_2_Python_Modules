#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import alchemy.grimoire.light_validator as light

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    record = "Spell recorded: %s (%s - %s)"
    no_name = "Magic of the empty hand huh?"
    no_name += "\nyou are not ready yet.\nName your spell!"


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------

def light_spell_allowed_ingredients() -> list[str]:

    return (light.LightSpells.valid_ingredients)


def light_spell_record(spell_name: str, ingredients: str) -> str:

    if (not isinstance(ingredients, str)):
        raise TypeError

    if (not spell_name):
        return (StringContainer.no_name)

    return (
        StringContainer.record %
        (
            spell_name, ingredients, light.validate_ingredients(ingredients)
        )
    )

# ---------------------------- run ----------------------------


def main() -> None:
    pass


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
