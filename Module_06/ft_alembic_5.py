#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

from alchemy import create_air

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class FileVariables:

    name = "=== Alembic 5 ==="
    include = "Accessing the alchemy module using 'from alchemy import ...'"
    test = "Testing create_air: "


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- run ----------------------------


def main() -> None:

    cast: str

    print(FileVariables.name)
    print(FileVariables.include)
    print(FileVariables.test, end='')
    cast = create_air()
    print(cast)


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
