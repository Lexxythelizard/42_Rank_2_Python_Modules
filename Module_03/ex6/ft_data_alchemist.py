#!/usr/bin/python3

# +++++++++++++++++++++++++++ import +++++++++++++++++++++++++++

import random

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Game Data Alchemist ==="

initial_list_str = "Initial list of players: %s"
filtered_list_str = "New list with all names capitalized: %s"
capitalized_list_str = "New list of capitalized names only: %s"
score_dict_str = "Score dict: %s"
average_score_str = "Score average is %.2f"
high_score_str = "High scores: %s"

# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++


# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++

# --------------- utils ---------------


def is_capital(s: str) -> bool:

    if (not s):
        return (False)
    return (s.capitalize() == s)


# --------------- main ---------------


def main() -> None:

    players_initial_list: list[str]
    players_filtered_capitalized: list[str]
    players_capitalized: list[str]
    score_dict: dict[str, int]
    high_score_dict: dict[str, int]

    average_score: float | int
    number_of_players: int

    print(intro_str, '\n')

    players_initial_list = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam'
    ]

    players_filtered_capitalized = [
        player for player in players_initial_list if is_capital(player)
    ]

    players_capitalized = [
        player.capitalize() for player in players_initial_list
    ]

    score_dict = {
        player: random.randint(0, 999) for player in players_capitalized
    }

    number_of_players = len(score_dict.values())
    average_score = sum(score_dict.values()) / number_of_players

    high_score_dict = {
        pl: sc for pl, sc in score_dict.items() if sc > average_score
    }

    print(initial_list_str % players_initial_list)
    print(capitalized_list_str % players_capitalized)
    print(filtered_list_str % players_filtered_capitalized, '\n')
    print(score_dict_str % score_dict)
    print(average_score_str % average_score)
    print(high_score_str % high_score_dict)


# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
