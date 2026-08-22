#!/usr/bin/python3

# --- globals ---

intro_str = "=== Plant Factory Output ==="
outro_str = "\n=== End of Program ==="

created_str = "Created: "

height_suf = "cm"
age_suf = " days old"

plant_str = "Plant"

default_name = "42 %s"
default_height = 42.00
default_age = 42
default_grow_rate = 0.042


# --- class ---


class Plant:

    """
    It's a plant, it can grow and age aaand well actually it could do more,
    but one step at a time.
    """

    name: str
    height: float
    age_days: int
    grow_rate: float

    def __new__(
        cls,
        name=default_name % plant_str,
        height=default_height,
        age=default_age,
        grow_rate=default_grow_rate
    ):
        print(created_str, end='')
        plant = object.__new__(cls)
        return (plant)

    def __init__(
        self,
        name=default_name % plant_str,
        height=default_height,
        age=default_age,
        grow_rate=default_grow_rate
    ):
        self.name = name
        self.height = height
        self.age_days = age
        self.grow_rate = grow_rate

    def age(self, add_days=1):
        self.age_days += add_days

    def grow(self):
        self.height += self.height * self.grow_rate

    def show(self):
        out = f"{self.name}, "
        out += f"{round(self.height, 1)}{height_suf}, "
        out += f"{self.age_days}{age_suf}"
        print(out)


# --- funcs ---

# code

# --- main ---

def main():

    print(intro_str)

    plant0 = Plant(
        name="Rose",
        height=25.0,
        age=30,
        grow_rate=0.05)
    plant0.show()

    plant1 = Plant(
        name="Oak",
        height=200.0,
        age=365,
        grow_rate=0.003)
    plant1.show()

    plant2 = Plant(
        name="Cactus",
        height=45.0,
        age=300,
        grow_rate=0.01)
    plant2.show()

    plant3 = Plant(
        name="Sunflower",
        height=80.0,
        age=90,
        grow_rate=0.01)
    plant3.show()

    plant4 = Plant(
        name="Fern",
        height=15.0,
        age=120,
        grow_rate=0.01)
    plant4.show()

    print(outro_str)


# --- run ---


if __name__ == '__main__':

    main()
