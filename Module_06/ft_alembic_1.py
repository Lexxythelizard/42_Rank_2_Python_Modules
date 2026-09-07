#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

from elements import create_water

# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class FileVariables:

    name = "=== Alembic 1 ==="
    include = "Using: 'from ... import ...' structure to access elements.py"
    test = "Testing create_water: "


# ---------------------------- run ----------------------------


def main() -> None:

    cast: str

    print(FileVariables.name)
    print(FileVariables.include)
    print(FileVariables.test, end='')
    cast = create_water()
    print(cast)


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
