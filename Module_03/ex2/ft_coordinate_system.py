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

# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++


# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++


# --------------- process ---------------


def get_player_pos() -> tuple[float, float, float]:

    while True:
        input_str = input(input_prompt_str)
        coords_str = input_str.split(',')

        if len(coords_str) != 3:
            print(invalid_syntax_str)
            continue

        coords: list[float] = []
        error_occurred = False

        for coord_str in coords_str:
            try:
                coords.append(float(coord_str.strip()))
            except ValueError:
                problematic = coord_str.strip()
                print(error_convert_str % (problematic, problematic))
                error_occurred = True
                break

        if not error_occurred:
            return (coords[0], coords[1], coords[2])


# --------------- utils ---------------


def distance_to_origin(coords: tuple[float, float, float]) -> float:

    x, y, z = coords
    return math.sqrt(x**2 + y**2 + z**2)


def distance_between(coords1: tuple[float, float, float],
                     coords2: tuple[float, float, float]) -> float:

    x1, y1, z1 = coords1
    x2, y2, z2 = coords2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


# --------------- main ---------------


def main() -> None:

    first_coords: tuple[float, float, float]
    second_coords: tuple[float, float, float]
    distance_origin: float
    distance_coords: float

    print(intro_str)

    print(first_coords_str)
    first_coords = get_player_pos()
    print(got_tuple_str % (first_coords,))
    x, y, z = first_coords
    print(coords_display_str % (x, y, z))
    distance_origin = distance_to_origin(first_coords)
    print(distance_to_center_str % distance_origin)

    print(second_coords_str)
    second_coords = get_player_pos()
    distance_coords = distance_between(first_coords, second_coords)
    print(distance_between_str % distance_coords)


# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
