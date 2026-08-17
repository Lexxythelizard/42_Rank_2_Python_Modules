#!/bin/usr/python3

# --- globals ---

inp_str_0 = "Days until harvest: "
out_str_0 = "%s seeds:%s%d%s"
out_str_1 = "Unknown unit type"

packets_str = "packets"
grams_str = "grams"
area_str = "area"

# --- dicts ---

units_types = [packets_str, grams_str, area_str]

out_str_units_types = {
    packets_str: "%s seeds: %d packets available",
    grams_str: "%s seeds: %d grams total",
    area_str: "%s seeds: covers %d square meters",
}

# --- define ---


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    """
    ask for user input and response
    """

    if (unit in units_types):
        print(
            out_str_units_types[unit] %
            (seed_type.capitalize(), quantity)
        )
    else:
        print(out_str_1)
