#!/usr/bin/python3

# +++++++++++++++++++++++++++ import +++++++++++++++++++++++++++

import random

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Achievement Tracker System ==="
player_str = "Player %s: %s"
all_distinct_str = "All distinct achievements: %s"
common_str = "Common achievements: %s"
only_has_str = "Only %s has: %s"
missing_str = "%s is missing: %s"

# --------------- lists ---------------

achievements_list = [
    'Crafting Genius', 'World Savior',
    'Master Explorer', 'Collector Supreme',
    'Untouchable', 'Boss Slayer',
    'Strategist', 'Unstoppable',
    'Speed Runner', 'Survivor',
    'Treasure Hunter', 'First Steps',
    'Sharp Mind', 'Hidden Path Finder'
]

# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++


# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++


# --------------- process ---------------


def gen_player_achievements() -> set[str]:

    num_achievements: int
    selected_achievements: set[str]
    i: int
    achievement: str

    num_achievements = random.randint(4, len(achievements_list))
    selected_achievements = set()

    for i in range(num_achievements):
        achievement = random.choice(achievements_list)
        selected_achievements.add(achievement)

    return selected_achievements


# --------------- utils ---------------


def get_only_has(player_achievements: set[str],
                 all_other_achievements: set[str]) -> set[str]:

    only: set[str]

    only = player_achievements.difference(all_other_achievements)
    return only


# --------------- main ---------------


def main() -> None:

    alice_achievements: set[str]
    bob_achievements: set[str]
    charlie_achievements: set[str]
    dylan_achievements: set[str]
    all_players: dict[str, set[str]]

    all_distinct: set[str]
    common: set[str]
    others_union: set[str]
    missing: set[str]

    player_name: str
    player_set: set[str]
    other_name: str
    other_set: set[str]

    print(intro_str)

    alice_achievements = gen_player_achievements()
    bob_achievements = gen_player_achievements()
    charlie_achievements = gen_player_achievements()
    dylan_achievements = gen_player_achievements()

    all_players = {
        'Alice': alice_achievements,
        'Bob': bob_achievements,
        'Charlie': charlie_achievements,
        'Dylan': dylan_achievements
    }

    for player_name, player_set in all_players.items():
        print(player_str % (player_name, player_set))

    all_distinct = set()
    for player_set in all_players.values():
        all_distinct = all_distinct.union(player_set)
    print(all_distinct_str % all_distinct)

    common = alice_achievements.intersection(bob_achievements).intersection(
        charlie_achievements).intersection(dylan_achievements)
    print(common_str % common)

    for player_name, player_set in all_players.items():
        others_union = set()
        for other_name, other_set in all_players.items():
            if other_name != player_name:
                others_union = others_union.union(other_set)
        print(
            only_has_str % (
                player_name, get_only_has(player_set, others_union)
            )
        )

    for player_name, player_set in all_players.items():
        missing = all_distinct.difference(player_set)
        print(missing_str % (player_name, missing))


# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
