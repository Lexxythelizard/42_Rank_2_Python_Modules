#!/usr/bin/python3

# +++++++++++++++++++++++++++ import +++++++++++++++++++++++++++

import sys

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Command Quest ==="
outro_str = "All custom error types work correctly!"

no_score_str = "No scores provided. Usage: python3 %s "
no_score_str += "<score1> <score2> ..."
invalid_param_str = "Invalid parameter: '%s'"
scores_str = "Scores processed:\t%s\n"
scores_str += "Total players:\t\t%d\n"
scores_str += "Total score:\t\t%d\n"
scores_str += "Avarage Score:\t\t%.1f\n"
scores_str += "High score:\t\t%d\n"
scores_str += "Low score:\t\t%d\n"
scores_str += "Score Range:\t\t%d"

# --------------- dicts ---------------

digits = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
}

# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++


# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++


# --------------- process ---------------


def get_argc_argv() -> tuple[int, list[str]]:

    argv = sys.argv
    return (len(argv), argv)


# --------------- utils ---------------


def lxy_atoi(arg: str) -> int:

    base = 10
    n = 0

    i = 0
    sign = 1

    while ((arg[i] in [' ', '\t', '\r']) and (i < len(arg))):
        i += 1

    if (arg[i] == '-'):
        sign *= (-1)
    if (arg[i] in ['-', '+']):
        i += 1

    while ((i < len(arg)) and (arg[i] in digits)):
        n = n * base + (digits[arg[i]] * sign)
        i += 1

    return (n)


def is_digits(arg: str) -> bool:

    for c in arg:
        if (c not in digits):
            return False
    return True


# --------------- main ---------------


def main() -> None:

    argc: int
    argv: list[str]
    valid_args: list[int]
    invalid_args: list[str]
    program_name: str

    total_players: int
    total_score: int
    average_score: float
    high_score: int
    low_score: int
    score_range: int

    print(intro_str)
    argc, argv = get_argc_argv()
    program_name = argv[0]

    valid_args = [lxy_atoi(arg) for arg in argv if is_digits(arg)]
    invalid_args = [arg for arg in argv if not is_digits(arg)]
    invalid_args = invalid_args[1:]

    for arg in invalid_args:
        print(invalid_param_str % arg)

    if (not valid_args):
        print(no_score_str % program_name)
        return

    total_players = len(valid_args)
    total_score = sum(valid_args)
    average_score = total_score / total_players
    high_score = max(valid_args)
    low_score = min(valid_args)
    score_range = high_score - low_score

    print(
        scores_str % (
            valid_args,
            total_players,
            total_score,
            average_score,
            high_score,
            low_score,
            score_range
        )
    )

# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
