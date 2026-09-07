#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import alchemy as alchm

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class FileVariables:

    name = "=== Transmutation 2 ==="
    include = "Import alchemy module only"
    test = "Testing lead_to_gold: "


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- run ----------------------------


def main() -> None:

    gold: str

    print(FileVariables.name)
    print(FileVariables.include)

    print(FileVariables.test, end='')
    gold = alchm.transmutation.lead_to_gold()
    print(gold)


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
