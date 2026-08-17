#!/bin/usr/python3

# --- globals ---

inp_str_0 = "Days until harvest: "
out_str_0 = "Day %d"
out_str_1 = "Harvest time!"

# --- define ---


def ft_count_harvest_iterative():

    """
    ask for user input and response
    """

    start = 1
    days = int(input(inp_str_0))

    for day in range(start, (days + 1)):
        print(out_str_0 % day)

    print(out_str_1)
