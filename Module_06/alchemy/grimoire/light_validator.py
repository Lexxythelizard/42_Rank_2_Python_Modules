#!/usr/bin/python3

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------

class StringContainer:

    valid = "VALID"
    invalid = "INVALID"


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class LightSpells:

    valid_ingredients: list[str]

    valid_ingredients = [
        "fire", "air", "water", "earth"
    ]


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------

def validate_ingredients(ingredients: str) -> str:

    for el in ingredients.split():
        if el.lower() in LightSpells.valid_ingredients:
            return (StringContainer.valid)
    return (StringContainer.invalid)


# ---------------------------- run ----------------------------


def main() -> None:
    pass


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
