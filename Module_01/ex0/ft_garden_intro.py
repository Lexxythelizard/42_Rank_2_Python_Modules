#!/usr/bin/python3

# --- globals ---

intro_str = "=== Welcome to My Garden ==="
outro_str = "\n=== End of Program ==="

name_str = "Name: "
height_str = "Height: "
age_str = "Age: "

height_suf = "cm"
age_suf = " days"

# --- class ---


class Plant:

    """
    It's a plant
    """

    name: str
    height: int
    age: int

    def __init__(self, name="42 plant", height=42, age=42):
        self.name = name
        self.height = height
        self.age = age

    def print_stats(self):
        print(f"{name_str}{self.name}")
        print(f"{height_str}{self.height}{height_suf}")
        print(f"{age_str}{self.age}{age_suf}")

# ---run ---


if __name__ == '__main__':

    rose = Plant(
        name="Rose",
        height=25,
        age=30)
    print(intro_str)
    rose.print_stats()
    print(outro_str)
