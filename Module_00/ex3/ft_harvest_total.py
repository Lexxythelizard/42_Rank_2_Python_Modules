#!/bin/usr/python3

# --- globals ---

inp_str_0 = "Day %d harvest: "
out_str_0 = "Total harvest: %d"

# --- define ---


def ft_harvest_total():

    """
    ask for user input and response
    """

    days = 3

    day = 1
    harvest = 0

    while (day <= days):
        harvest += int(input(inp_str_0 % day))
        day += 1
    print(out_str_0 % harvest)
