#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import alchemy.grimoire as grimoir

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class FileVariables:

    name = "=== Kaboom 1 ==="
    include = "Access to alchemy/grimoire/dark_spellbook.py directly"
    test = "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION"


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- run ----------------------------


def main() -> None:

    print(FileVariables.name)
    print(FileVariables.include)
    print(FileVariables.test)

    spell = grimoir.dark_spell_record("black fire", "eyeball fire and bat")
    print(spell)

# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++


if __name__ == '__main__':

    main()
