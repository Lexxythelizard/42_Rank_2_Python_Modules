#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import alchemy.grimoire as grimoire

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class FileVariables:

    name = "=== Kaboom 1 ==="
    include = "Using grimoire module directly"
    test = "Testing record light spell: "


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- run ----------------------------


def main() -> None:

    spell: str

    print(FileVariables.name)
    print(FileVariables.include)
    print(FileVariables.test, end='')

    spell = grimoire.light_spell_record("Fantasy", "fire earth and air")
    print(spell)


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++


if __name__ == '__main__':

    main()
