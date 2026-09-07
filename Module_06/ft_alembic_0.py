#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import elements

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class FileVariables:

    name = "=== Alembic 0 ==="
    include = "Using: 'import ...' structure to access elements.py"
    test = "Testing create_fire: "


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- run ----------------------------


def main() -> None:

    cast: str

    print(FileVariables.name)
    print(FileVariables.include)
    print(FileVariables.test, end='')
    cast = elements.create_fire()
    print(cast)


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
