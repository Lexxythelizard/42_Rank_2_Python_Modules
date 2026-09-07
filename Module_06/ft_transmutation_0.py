#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

from alchemy.transmutation.recipes import lead_to_gold

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class FileVariables:

    name = "=== Transmutation 0 ==="
    include = "Using file alchemy/transmutation/recipes.py directly"
    test = "Testing lead_to_gold: "


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- run ----------------------------


def main() -> None:

    gold: str

    print(FileVariables.name)
    print(FileVariables.include)

    print(FileVariables.test, end='')
    gold = lead_to_gold()
    print(gold)


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
