#!/bin/usr/python3

# --- globals ---

inp_str_0 = "Enter length: "
inp_str_1 = "Enter width: "
out_str_0 = "Plot area: %d"

# --- define ---


def ft_plot_area():

    """
    ask for user input and response
    """

    length = int(input(inp_str_0))
    width = int(input(inp_str_1))
    print(out_str_0 % (length * width))
