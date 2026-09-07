#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import alchemy as alchm

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class FileVariables:

    name = "=== Distillation 1 ==="
    include = "Using: 'import alchemy' structure to access potions"
    test = "Testing strength_potion: "
    test_1 = "Testing healing_potion: "


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- run ----------------------------


def main() -> None:

    brew: str

    print(FileVariables.name)
    print(FileVariables.include)

    print(FileVariables.test, end='')
    brew = alchm.strength_potion()
    print(brew)

    print(FileVariables.test, end='')
    brew = alchm.healing_potion()
    print(brew)


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
