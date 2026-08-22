#!/usr/bin/python3

# --- globals ---

intro_str = "=== Garden Plant Growth ==="
outro_str = "\n=== End of Program ==="

grow_str = "Growth this week: "

height_suf = "cm"
age_suf = " days old"

day_head = "=== Day %d ==="

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

    def grow(self, add_cm=0):
        if (add_cm <= 0):
            self.height += self.height * self.grow_rate
        else:
            self.height += add_cm

    def show(self):
        out = f"{self.name}, "
        out += f"{round(self.height, 1)}{height_suf}, "
        out += f"{self.age_days}{age_suf}"
        print(out)


# --- funcs ---


def day_pass_by(plant: Plant, days: int, cm_per_day=0):

    for i in range(1, (days + 1)):
        plant.age(1)
        plant.grow(cm_per_day)
        print(day_head % i)
        plant.show()


def week_pass_by(plant: Plant, cm_per_day=0):

    plant.show()
    height_0 = plant.height
    day_pass_by(plant, 7, cm_per_day)
    print(f"{grow_str} {round((plant.height - height_0), 1)}{height_suf}")


# --- main ---


def main():

    plant0 = Plant(
        name="Rose",
        height=25.0,
        age=30,
        grow_rate=0.05)
    plant1 = Plant(
        name="Cactus",
        height=45.0,
        age=300,
        grow_rate=0.01)
    plant2 = Plant(
        name="Oak",
        height=980.0,
        age=1300,
        grow_rate=0.003)
    print(intro_str)
    week_pass_by(plant0, 0.8)
    print('')
    week_pass_by(plant1)
    print('')
    week_pass_by(plant2)
    print('')
    print(outro_str)


# --- run ---


if __name__ == '__main__':

    main()
