#!/usr/bin/python3

# +++++++++++++++++++++++++++ import +++++++++++++++++++++++++++

import sys

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- sniggle ---------------

separator = ':'
default_item = ('_spaceholder', 42)

# --------------- strings ---------------

intro_str = "=== Inventory System Analysis ==="
got_inventory_str = "Got inventory: %s"
item_list_str = "Item list: %s"
total_quantity_str = "Total quantity of the %d items: %d"
item_percentage_str = "Item %s represents %.1f%%"
most_abundant_str = "Item most abundant: %s with quantity %d"
least_abundant_str = "Item least abundant: %s with quantity %d"
updated_inventory_str = "Updated inventory: %s"

redundant_str = "Redundant item '%s' - discarding"
invalid_param_str = "Error - invalid parameter '%s'"
quantity_error_str = "Quantity error for 'key': %s"

# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++


class Inventory:

    inventory: dict[str, int]
    items: int
    total_quantity: int

    def __init__(self) -> None:
        self.inventory = {}
        self.items = 0
        self.total_quantity = 0

    def add_items(self, item_list: list[tuple[str, int]]) -> None:

        filtered: dict[str, int]
        name: str
        quantity: int

        filtered = {}

        for item in item_list:
            name, quantity = item
            if name not in filtered.keys():
                filtered.update({name: quantity})
            else:
                print(redundant_str % name)

        print(got_inventory_str % filtered)

        for new_item in filtered.keys():

            if new_item in self.inventory.keys():
                self.inventory[new_item] += filtered[new_item]

            else:
                self.inventory.update({new_item: filtered[new_item]})

        self.items = len(self.inventory.keys())
        self.total_quantity = sum(self.inventory.values())

    def get_inventory(self) -> dict[str, int]:
        return (self.inventory)

    def get_item_list(self) -> list[str]:

        item_list: list[str]

        item_list = [name for name in self.inventory.keys()]
        return (item_list)

    def get_item_distribution(self) -> list[tuple[str, float]]:

        distribution_list: list[tuple[str, float]]

        distribution_list = []

        for name in self.inventory.keys():

            distribution = float(self.inventory[name] / self.total_quantity)
            distribution_list += [(name, distribution)]

        return (distribution_list)

    def get_most_abundant_item(self) -> tuple[str, int]:

        max_quant: int
        most_abundant: tuple[str, int]

        max_quant = 0
        most_abundant = default_item
        for quant in self.inventory.values():
            max_quant = quant if quant > max_quant else max_quant

        for name in self.inventory.keys():
            if (self.inventory[name] == max_quant):
                most_abundant = (name, self.inventory[name])
                break

        return (most_abundant)

    def get_least_abundant_item(self) -> tuple[str, int]:

        min_quant: int
        least_abundant: tuple[str, int]

        min_quant = sum(self.inventory.values())
        least_abundant = default_item
        for quant in self.inventory.values():
            min_quant = quant if quant < min_quant else min_quant

        for name in self.inventory.keys():
            if (self.inventory[name] == min_quant):
                least_abundant = (name, self.inventory[name])
                break

        return (least_abundant)


# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++

# --------------- pass_arguments ---------------


def get_argc_argv() -> tuple[int, list[str]]:

    argv = sys.argv
    return (len(argv), argv)


# --------------- parse_arguments ---------------


def parse_arguments(valid_args: list[str]) -> list[tuple[str, int]]:

    separated: list[list[str]]
    parsed: list[tuple[str, int]]

    separated = [
        arg.split(separator) for arg in valid_args
    ]
    parsed = []

    for arg in separated:
        try:
            parsed += [(arg[0], int(arg[1]))]
        except ValueError as err:
            print(quantity_error_str % err)

    return (parsed)


def filter_arguments(args: list[str]) -> list[str]:

    valid_args = [
        arg for arg in args if is_arg_valid(arg)
    ]
    invalid_args = [
        arg for arg in args if not is_arg_valid(arg)
    ]

    for arg in invalid_args:
        print(invalid_param_str % arg)

    return (valid_args)


def is_arg_valid(arg: str) -> bool:

    if (not arg):
        return (False)
    if (arg.count(separator) != 1):
        return (False)
    if (arg.startswith(separator) or arg.endswith(separator)):
        return (False)
    return (True)


# --------------- main ---------------


def main() -> None:

    argv: list[str]
    argc: int

    valid_args: list[str]
    parsed_args: list[tuple[str, int]]
    item_destribution: list[tuple[str, float]]

    name: str
    quantity: int
    destribution: float

    inventory: Inventory

    print(intro_str)

    argc, argv = get_argc_argv()
    argv = argv[1:]

    valid_args = filter_arguments(argv)
    parsed_args = parse_arguments(valid_args)

    inventory = Inventory()
    inventory.add_items(parsed_args)

    print(item_list_str % inventory.get_item_list())
    print(total_quantity_str % (inventory.items, inventory.total_quantity))

    item_destribution = inventory.get_item_distribution()
    for item in item_destribution:
        name, destribution = item
        destribution = round(destribution * 100, 1)
        print(item_percentage_str % (name, destribution))

    if (inventory.items > 0):
        name, quantity = inventory.get_most_abundant_item()
        print(most_abundant_str % (name, quantity))

        name, quantity = inventory.get_least_abundant_item()
        print(least_abundant_str % (name, quantity))

    print(updated_inventory_str % inventory.get_inventory())

# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
