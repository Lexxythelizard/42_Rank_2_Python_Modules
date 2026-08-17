#!/bin/usr/python3

# --- globals ---

inp_str_0 = "Days since last watering: "
out_str_0 = "Water the plants!"
out_str_1 = "Plants are fine."

fine_without_water_int = 2

# --- define ---


def ft_water_reminder():

    """
    ask for user input and response
    """

    if (int(input(inp_str_0)) > fine_without_water_int):
        print(out_str_0)
    else:
        print(out_str_1)
