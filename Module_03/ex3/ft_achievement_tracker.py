#!/usr/bin/python3

# +++++++++++++++++++++++++++ import +++++++++++++++++++++++++++

import random as rand

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Achievement Tracker System ==="
player_str = "Player %s: %s"
all_distinct_str = "All distinct achievements: %s"
common_str = "Common achievements: %s"
only_has_str = "Only %s has: %s"
missing_str = "%s is missing: %s"

# --------------- lists ---------------

player_names = [
    'Alice',
    'Bob',
    'Charlie',
    'Dylan',
]

# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++


class Archivements:

    """
    This class serves as an container for archievements
    """

    _achievements_list = [
        'Crafting Genius', 'World Savior',
        'Master Explorer', 'Collector Supreme',
        'Untouchable', 'Boss Slayer',
        'Strategist', 'Unstoppable',
        'Speed Runner', 'Survivor',
        'Treasure Hunter', 'First Steps',
        'Sharp Mind', 'Hidden Path Finder'
    ]

    @classmethod
    def get_len(cls) -> int:
        return (len(cls._achievements_list))

    @classmethod
    def get_all(cls) -> set[str]:
        return (set(cls._achievements_list))

    @classmethod
    def get_n_random_achievements(cls, n: int) -> set[str]:

        random_achievements: set[str]

        if (n == -1):
            return (set(cls._achievements_list))

        try:
            random_achievements = set(
                rand.sample(cls._achievements_list, n)
            )
        except ValueError:
            random_achievements = set()

        return (random_achievements)


class Player:

    """
    Normally Player would also contains HP, strength, etc... but
    in this particular case we just have the achievements,
    class would get to big and I was to lazy ;)
    """

    _name: str
    _achievements: set[str]

    def __init__(self, name: str) -> None:
        self._name = name
        self._achievements = set()

    def set_achievements(self, achievements: set[str]) -> None:
        self._achievements = achievements

    def get_achievements(self) -> set[str]:
        return (self._achievements)

    def get_name(self) -> str:
        return (self._name)

    def get_unachieved(
        self,
        all_achievements: set[str] = Archivements.get_all()
    ) -> set[str]:

        return (self._achievements.difference(all_achievements))

    def get_unique_achievements(
        self,
        other_achievements: list[set[str]]
    ) -> set[str]:

        unique: set[str]

        unique = self._achievements
        for achievements in other_achievements:
            unique = unique.difference(achievements)
        return (unique)


# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++

# --------------- explicitly requeseted ---------------


def gen_player_achievements() -> set[str]:

    """
    Create a function gen_player_achievements()
    that will use a large fixed list of achievements
    to randomly assign a set to a player.
    Choose a random number of achievements,
    then pick this number of achievements from the list to build
    and return the set.
    """

    number_of_achievements: int

    number_of_achievements = rand.randint(0, Archivements.get_len())
    return (Archivements.get_n_random_achievements(number_of_achievements))


# --------------- run ---------------


def main() -> None:

    players: list[Player]
    all_distinct: set[str]
    common: set[str]

    print(intro_str, '\n')
    players = [Player(name) for name in player_names]
    all_distinct = set()
    common = Archivements.get_all()

    for player in players:
        player.set_achievements(
            gen_player_achievements()
        )

    for player in players:
        print(
            player_str % (player.get_name(), player.get_achievements())
        )
    print('')

    for player in players:
        all_distinct = all_distinct.union(player.get_achievements())
    print(
        all_distinct_str % all_distinct
    )
    print('')

    for player in players:
        common = common.intersection(player.get_achievements())
    print(
        common_str % common
    )
    print('')

    for player in players:
        unique = player.get_achievements()

        for compare in players:
            if (compare == player):
                continue
            unique = unique.difference(compare.get_achievements())

        print(
            only_has_str % (player.get_name(), unique)
        )
    print('')

    for player in players:
        print(
            missing_str % (
                player.get_name(),
                Archivements.get_all().difference(player.get_achievements())
            )
        )

# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
