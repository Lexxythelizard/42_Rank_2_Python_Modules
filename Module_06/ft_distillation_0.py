#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

from alchemy.potions import healing_potion, strength_potion

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class FileVariables:

    name = "=== Distillation 0 ==="
    include = "Direct access to alchemy/potions.py"
    test = "Testing strength_potion: "
    test_1 = "Testing healing_potion: "


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- run ----------------------------


def main() -> None:

    brew: str

    print(FileVariables.name)
    print(FileVariables.include)

    print(FileVariables.test, end='')
    brew = strength_potion()
    print(brew)

    print(FileVariables.test, end='')
    brew = healing_potion()
    print(brew)


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
