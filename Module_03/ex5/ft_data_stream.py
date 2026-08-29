#!/usr/bin/python3

# +++++++++++++++++++++++++++ import +++++++++++++++++++++++++++

import random
from typing import Generator

"""
NOTE:

    the typing import is just for declaration:
        --> declaration needed for mypy (--strict)

    Generator[<yielded type>, <send in type>, <final return>]

    yield makes a generator a generator: yield != return

    Yield expressions and statements are only used when defining a
    *generator* function, and are only used in the body of the generator
    function.  Using yield in a function definition is sufficient to cause
    that definition to create a generator function instead of a normal
    function.

"""

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Game Data Stream Processor ==="
event_str = "Event %d: Player %s did action %s"
built_list_str = "Built list of 10 events: %s"
got_event_str = "Got event from list: %s"
remains_str = "Remains in list: %s"

# --------------- data ---------------

players: list[str] = [
    "alice",
    "bob",
    "charlie",
    "dylan"
]
actions: list[str] = [
    "run", "move", "eat",
    "sleep", "grab", "release",
    "climb", "swim", "use"
]

# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++

# --------------- gen_event ---------------


def gen_event() -> Generator[tuple[str, str], None, None]:

    player: str
    action: str

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


# --------------- consume_event ---------------


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:

    idx: int
    event: tuple[str, str]

    while len(events) > 0:
        idx = random.randint(0, len(events) - 1)
        event = events.pop(idx)
        yield event


# --------------- main ---------------


def main() -> None:

    i: int
    gen: Generator[tuple[str, str], None, None]
    name: str
    action: str
    event_list: list[tuple[str, str]]
    event: tuple[str, str]

    print(intro_str)
    gen = gen_event()

    for i in range(1000):
        name, action = next(gen)
        print(event_str % (i, name, action))
    event_list = []
    gen = gen_event()

    for i in range(10):
        event = next(gen)
        event_list.append(event)
    print(built_list_str % event_list)

    for event in consume_event(event_list):
        print(got_event_str % (event,))
        print(remains_str % event_list)


# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
