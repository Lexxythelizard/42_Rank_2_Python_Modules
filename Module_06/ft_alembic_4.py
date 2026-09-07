#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import alchemy

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# TODO:
#   - modify alchemy/__init__.py and exclud create earth
#   - try except block
#   - write comment: caus eerro should be erro in mypy...


class FileVariables:

    name = "=== Alembic 4 ==="
    include = "Accessing the alchemy module using 'import alchemy'"
    test = "Testing create_air: "
    test_exception = "Now show that not all functions can be reached"
    test_exception += "\nThis will raise an exception!"
    test_1 = "Testing create_earth: "


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- run ----------------------------


def main() -> None:

    cast: str

    print(FileVariables.name)
    print(FileVariables.include)
    print(FileVariables.test, end='')
    cast = alchemy.create_air()

    print(FileVariables.test_exception)
    print(FileVariables.test_1, end='')
    cast = alchemy.create_earth()
    print(cast)


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
