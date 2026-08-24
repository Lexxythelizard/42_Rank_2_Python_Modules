#!/usr/bin/python3

# +++++++++++++++++++++++++++ import +++++++++++++++++++++++++++

import sys

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Command Quest ==="
outro_str = "All custom error types work correctly!"

arg0_str = "Programm name: %s"
arg1_str = "Arguments received: %d"
arg2_str = "Argument %d: %s"
arg3_str = "Total arguments: %d"
arg_null_str = "No arguments provited!"

# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++


# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++

# --------------- checker functions ---------------


def get_argc_argv() -> tuple[int, list[str]]:

    argv = sys.argv
    return (len(argv), argv)


def display_args(argc: int, argv: list) -> None:

    i = 1

    if (argc <= 1):
        print(arg_null_str)
        return

    print(arg1_str % (argc - 1))
    while (i < argc):
        print(arg2_str % ((i - 1), argv[i]))
        i += 1


# --------------- main ---------------


def main() -> None:

    print(intro_str)
    argc, argv = get_argc_argv()
    print(arg0_str % argv[0])
    display_args(argc, argv)
    print(arg3_str % argc)


# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
