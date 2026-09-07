#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import alchemy.transmutation as trans

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class FileVariables:

    name = "=== Transmutation 1 ==="
    include = "Import transmutation module directly"
    test = "Testing lead_to_gold: "


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- run ----------------------------


def main() -> None:

    gold: str

    print(FileVariables.name)
    print(FileVariables.include)

    print(FileVariables.test, end='')
    gold = trans.lead_to_gold()
    print(gold)


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
