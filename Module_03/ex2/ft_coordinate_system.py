#!/usr/bin/python3

# +++++++++++++++++++++++++++ import +++++++++++++++++++++++++++

import math

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Game Coordinate System ==="
first_coords_str = "Get a first set of coordinates"
second_coords_str = "Get a second set of coordinates"
input_prompt_str = "Enter new coordinates as floats in format 'x,y,z': "
invalid_syntax_str = "Invalid syntax"
got_tuple_str = "Got a first tuple: %s"
coords_display_str = "It includes: X=%.1f, Y=%.1f, Z=%.1f"
distance_to_center_str = "Distance to center: %.4f"
distance_between_str = "Distance between the 2 sets of coordinates: %.4f"
error_convert_str = "Error on parameter '%s': "
error_convert_str += "could not convert string to float: '%s'"
error_keyboard_interrupt_str = "\nKeyboardInterrupt: stopping execution!"

dil = ','
origin_coords = (0.0, 0.0, 0.0)

# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++


class Pos:

    _coords: tuple[float, float, float]

    def __init__(
        self,
        coords: tuple[float, float, float]
    ) -> None:
        self._coords = coords

    def get_coords(
        self
    ) -> tuple[float, float, float]:
        return (self._coords)

    def get_distance_to(
        self,
        coords: tuple[float, float, float]
    ) -> float:

        x0: float
        x1: float
        y0: float
        y1: float
        z0: float
        z1: float

        x0, y0, z0 = self._coords
        x1, y1, z1 = coords

        distance = math.sqrt(
            (x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2
        )
        return (distance)


# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++


# --------------- cli interface ---------------


def get_player_pos() -> tuple[float, float, float]:

    control: bool
    usr_coords: tuple[float, float, float]

    control = False
    usr_coords = origin_coords

    while (not control):
        control, usr_coords = get_player_pos_iteration()

    return (usr_coords)


def get_player_pos_iteration() -> tuple[bool, tuple[float, float, float]]:

    usr_inp: str
    dim: int
    i: int
    usr_inp_filtered: list[str]
    usr_inp_parsed: list[float]
    usr_coords: tuple[float, float, float]

    dim = 3
    i = 0

    usr_inp = input(input_prompt_str)
    usr_inp_filtered = usr_inp.split(dil)
    usr_inp_filtered = [el.strip() for el in usr_inp_filtered if el.strip()]
    usr_inp_parsed = []
    usr_coords = origin_coords

    if (usr_inp.count(dil) != 2):
        print(invalid_syntax_str)
        return ((False, origin_coords))

    while (i < dim):
        try:
            usr_inp_parsed += [float(usr_inp_filtered[i])]
        except IndexError:
            print(invalid_syntax_str)
            return ((False, usr_coords))
        except ValueError:
            print(
                error_convert_str %
                (usr_inp_filtered[i], usr_inp_filtered[i])
            )
            return ((False, usr_coords))
        i += 1

    usr_coords = (usr_inp_parsed[0], usr_inp_parsed[1], usr_inp_parsed[2])

    return ((True, usr_coords))


# --------------- main ---------------


def main() -> None:

    pos_origin: Pos
    pos_1: Pos
    pos_2: Pos

    print(intro_str, '\n')

    pos_origin = Pos(origin_coords)

    print(first_coords_str)
    try:
        pos_1 = Pos(get_player_pos())
    except KeyboardInterrupt:
        print(error_keyboard_interrupt_str)
        return
    print(coords_display_str % pos_1.get_coords())
    print(
        distance_to_center_str %
        pos_1.get_distance_to(pos_origin.get_coords())
    )
    print('')

    print(second_coords_str)
    try:
        pos_2 = Pos(get_player_pos())
    except KeyboardInterrupt:
        print(error_keyboard_interrupt_str)
        return
    print(coords_display_str % pos_2.get_coords())
    print(
        distance_between_str %
        pos_2.get_distance_to(pos_1.get_coords())
    )

# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
