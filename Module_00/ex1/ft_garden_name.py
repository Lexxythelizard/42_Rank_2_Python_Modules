#!/bin/usr/python3

# --- globals ---

inp_str_0 = "Enter garden name: "
out_str_0 = "Garden: "
out_str_1 = "Status: "

status = "Growing well!"

# --- define ---


def ft_garden_name():

    """
    ask for user input and response
    """

    garden_name = input(inp_str_0)
    print(f"{out_str_0}{garden_name}")
    print(f"{out_str_1}{status}")
