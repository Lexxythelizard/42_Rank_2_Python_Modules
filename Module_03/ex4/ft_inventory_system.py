#!/usr/bin/python3

# +++++++++++++++++++++++++++ import +++++++++++++++++++++++++++

import sys

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

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
quantity_error_str = "Quantity error for '%s': "
quantity_error_str += "invalid literal for int() with base 10: '%s'"

# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++


class Inventory:

    def __init__(self) -> None:

        self.inventory: dict[str, int]

        self.inventory = {}

    def get_item_list(self) -> list[str]:

        items: list[str]

        items = list(self.inventory.keys())
        return items

    def get_total_quantity(self) -> int:

        total: int
        quantity: int

        total = 0
        for quantity in self.inventory.values():
            total = total + quantity

        return total

    def add_item(self, item_name: str, quantity: int) -> None:

        self.inventory.update({item_name: quantity})

    def get_inventory(self) -> dict[str, int]:

        return self.inventory


class InventoryAnalyzer:

    def __init__(self, inventory: Inventory) -> None:

        self.inventory: Inventory

        self.inventory = inventory

    def display_percentages(self) -> None:

        inv_dict: dict[str, int]
        total: int
        item_name: str
        quantity: int
        percentage: float

        inv_dict = self.inventory.get_inventory()
        total = self.inventory.get_total_quantity()

        if total == 0:
            return

        for item_name, quantity in inv_dict.items():
            percentage = (quantity / total) * 100
            print(item_percentage_str % (item_name, round(percentage, 1)))

    def get_most_abundant(self) -> tuple[str, int]:

        inv_dict: dict[str, int]
        most_item: str
        most_qty: int
        item_name: str
        quantity: int

        inv_dict = self.inventory.get_inventory()
        most_item = ""
        most_qty = 0

        for item_name, quantity in inv_dict.items():
            if quantity > most_qty:
                most_qty = quantity
                most_item = item_name

        return (most_item, most_qty)

    def get_least_abundant(self) -> tuple[str, int]:

        inv_dict: dict[str, int]
        least_item: str
        least_qty: int | float
        item_name: str
        quantity: int

        inv_dict = self.inventory.get_inventory()

        if len(inv_dict) == 0:
            return ("", 0)

        least_item = ""
        least_qty = float('inf')

        for item_name, quantity in inv_dict.items():
            if quantity < least_qty:
                least_qty = quantity
                least_item = item_name

        return (least_item, int(least_qty))


# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++

# --------------- parse_arguments ---------------


def parse_arguments(args: list[str], inventory: Inventory) -> None:

    i: int
    arg: str
    parts: list[str]
    item_name: str
    quantity_str: str
    quantity: int

    i = 1

    while i < len(args):
        arg = args[i]

        if ':' not in arg:
            print(invalid_param_str % arg)
            i += 1
            continue

        parts = arg.split(':')

        if len(parts) != 2:
            print(invalid_param_str % arg)
            i += 1
            continue

        item_name = parts[0]
        quantity_str = parts[1]

        if item_name in inventory.get_inventory():
            print(redundant_str % item_name)
            i += 1
            continue

        try:
            quantity = int(quantity_str)
            inventory.add_item(item_name, quantity)
        except ValueError:
            print(quantity_error_str % (item_name, quantity_str))

        i += 1


# --------------- main ---------------


def main() -> None:

    args: list[str]
    inventory: Inventory
    analyzer: InventoryAnalyzer
    items: list[str]
    total: int
    most_name: str
    most_qty: int
    least_name: str
    least_qty: int

    print(intro_str)

    args = sys.argv
    inventory = Inventory()
    parse_arguments(args, inventory)

    print(got_inventory_str % inventory.get_inventory())

    items = inventory.get_item_list()
    print(item_list_str % items)

    total = inventory.get_total_quantity()
    print(total_quantity_str % (len(items), total))

    analyzer = InventoryAnalyzer(inventory)
    analyzer.display_percentages()

    most_name, most_qty = analyzer.get_most_abundant()
    print(most_abundant_str % (most_name, most_qty))

    least_name, least_qty = analyzer.get_least_abundant()
    print(least_abundant_str % (least_name, least_qty))

    inventory.add_item('magic_item', 1)
    print(updated_inventory_str % inventory.get_inventory())


# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
