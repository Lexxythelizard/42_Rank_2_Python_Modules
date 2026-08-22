#!/usr/bin/python3

# --- globals ---

intro_str = "=== Garden Security System ==="
outro_str = "\n=== End of Program ==="

age_str = "Age"
height_str = "Height"
name_str = "Name"
grow_rate_str = "Grow rate"

age_str_lower = "age"
height_str_lower = "height"
name_str_lower = "name"
grow_rate_str_lower = "grow rate"

created_str = "Plant created: "
negative_error_str = "Error, %s can't be negative"
type_error_str = "%s: Error, %s must be a %s"

height_suf = "cm"
age_suf = " days old"

float_str = "float"
int_str = "integer"
str_str = "string"

update_success_str = " updated: "
update_rejected_str = " update rejected"
current_state_str = "Current state"

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

    _name: str
    _height: float
    _age_days: int
    _grow_rate: float

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

        if (not is_number(height)):
            height = default_height

        if (not is_number(age)):
            age = default_age

        if (not is_number(grow_rate)):
            grow_rate = default_grow_rate

        if (not name):
            name = default_name % plant_str

        self._name = name
        self._height = height
        self._age_days = age
        self._grow_rate = grow_rate

    def set_name(self, new: str):

        if (new):
            self._name = new
            print(f"{name_str}{update_success_str}{self._name}")
        else:
            print(f"{self._name}: {negative_error_str}" % age_str_lower)
            print(f"{name_str}{update_rejected_str}")

    def set_age(self, new: int):

        if (not is_number(new)):
            print(
                type_error_str %
                (self._name, age_str_lower, int_str)
            )
            print(f"{age_str}{update_rejected_str}")
            return

        if (new >= 0):
            self._age = new
            print(f"{age_str}{update_success_str}{self._age}{age_suf}")
        else:
            print(f"{self._name}: {negative_error_str}" % age_str_lower)
            print(f"{age_str}{update_rejected_str}")

    def set_height(self, new: float):

        if (not is_number(new)):
            print(
                type_error_str %
                (self._name, height_str, float_str)
            )
            print(f"{height_str}{update_rejected_str}")
            return

        if (new >= 0.00):
            self._height = new
            print(f"{height_str}{update_success_str}", end='')
            print(f"{self._height}{height_suf}")
        else:
            print(f"{self._name}: {negative_error_str}" % height_str_lower)
            print(f"{height_str}{update_rejected_str}")

    def set_grow_rate(self, new: float):

        if (not is_number(new)):
            print(
                type_error_str %
                (self._name, grow_rate_str, float_str)
            )
            print(f"{grow_rate_str}{update_rejected_str}")
            return

        if (new >= 0.00):
            self._grow_rate = new
            print(f"{grow_rate_str}{update_success_str}", end='')
            print(f"{self._grow_rate}")
        else:
            print(
                 f"{self._name}: {negative_error_str}" %
                 height_str_lower
            )
            print(f"{grow_rate_str}{update_rejected_str}")

    def get_name(self):
        return (self._name)

    def get_age(self):
        return (self._age)

    def get_height(self):
        return (self._height)

    def do_age(self, add_days=1):
        self._age_days += add_days

    def do_grow(self):
        self._height += self.height * self.grow_rate

    def show(self):

        out = f"{self._name}, "
        out += f"{round(self._height, 1)}{height_suf}, "
        out += f"{self._age_days}{age_suf}"
        print(out)


# --- funcs ---


def plant_print_current_state(plant: Plant):

    print(
        f"{current_state_str}: %s: %f%s, %d%s",
        plant.get_name(),
        plant.get_height(),
        height_suf,
        plant.get_age(),
        age_suf)


# --- funcs ---

def is_number(var) -> bool:

    try:
        var >= 0.00
    except TypeError:
        return (False)

    return (var is not True)

# --- main ---


def main():

    print(intro_str)
    plant0 = Plant(
        name="Rose",
        height=15.0,
        age=10,
        grow_rate=0.05)
    plant0.show()

    print('')
    plant0.set_height(25.0)
    plant0.set_age(30)

    print('')
    plant0.set_height(-2)
    plant0.set_age(-2)

    print("\nCurrent state: ", end='')
    plant0.show()

    print(outro_str)

# --- run ---


if __name__ == '__main__':

    main()
