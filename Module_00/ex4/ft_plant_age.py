#!/bin/usr/python3

# --- globals ---

inp_str_0 = "Enter plant age in days: "
out_str_0 = "Plant is ready to harvest!"
out_str_1 = "Plant needs more time to grow."

ready_to_harvest_int = 61

# --- define ---


def ft_plant_age():

    """
    ask for user input and response
    """

    if (int(input(inp_str_0)) >= ready_to_harvest_int):
        print(out_str_0)
    else:
        print(out_str_1)
