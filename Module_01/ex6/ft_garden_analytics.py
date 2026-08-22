#!/usr/bin/python3

# ++++++++++++++++++++ globals ++++++++++++++++++++++

intro_str = "=== Garden statistics ==="
outro_str = "\n=== End of Program ==="

# --- generals ---

float_str = "float"
int_str = "integer"
str_str = "string"

update_success_str = "%s updated: %s %s"
update_rejected_str = "%s update rejected"
current_state_str = "Current state"

created_str = "%s created: "

empty_error_str = "%s Error, %s can't be empty"
negative_error_str = "%s Error, %s can't be negative"
type_error_str = "%s: Error, %s must be a %s"

# --- plant ---

plant_str = "Plant"

stats_str = "Stats"

default_name = "42 %s"
default_height = 42.00
default_age = 42
default_grow_rate = 0.042

unknown_plant_str = "Unknown plant"

# attributes

age_str = "Age"
height_str = "Height"
name_str = "Name"
grow_rate_str = "Grow rate"

height_suf = "cm"
age_suf = " days old"

# --- flower ---

flower_str = "Flower"

default_color = "red"

bloom_str = "[asking the %s to bloom]"
bloom_true_str = "%s is blooming beautifully!"
bloom_false_str = "%s has not bloomed yet"
color_str = "Color"

# --- tree ---

tree_str = "Tree"

default_diameter = 42

trunk_diameter_str = "Trunk diameter"
shadow_str = "[asking the %s to produce shade]"
shadow_true_str = "Tree %s now produces a shade of %.1fcm long "
shadow_true_str += "and %.1fcm wide."

# --- vegetable ---

vegetable_str = "Vegetable"

harvest_season_default = "the 13th month"
nutrional_value_default = 42

make_vegetable_str = "[make %s grow and age for %d days]"
harvest_season_str = "Harvest season"
nutritional_value_str = "Nutritional value"

# ++++++++++++++++++++ class ++++++++++++++++++++++


class Plant:

    """
    It's a plant, it can grow and age aaand well actually it could do more,
    but one step at a time.
    """

    _name: str
    _height: float
    _age: int
    _grow_rate: float

    def __new__(
        cls,
        name=default_name % plant_str,
        height=default_height,
        age=default_age,
        grow_rate=default_grow_rate
    ):

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
        self._age = age
        self._grow_rate = grow_rate
        self._stats = self.Statistics()

    class Statistics:

        _aged: int
        _grown: int
        _shown: int

        def __init__(self):

            self._aged = 0
            self._grown = 0
            self._shown = 0

        def increment_aged(self):
            self._aged += 1

        def increment_grown(self):
            self._grown += 1

        def increment_shown(self):
            self._shown += 1

        def get_aged(self):
            return (self._aged)

        def get_grown(self):
            return (self._grown)

        def get_shown(self):
            return (self._shown)

        def display(self):

            stats_str = "Stats: %d grow, %d age, %d show"

            print(
                stats_str %
                (self.get_grown(), self.get_aged(), self.get_shown())
            )

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:

        year = 365
        err_str = "Error: days must be an int"

        try:
            return (round(days) > year)
        except TypeError:
            print(err_str)
        return (False)

    @classmethod
    def create_unknown(cls):
        unknown_plant = cls.__new__(cls)
        unknown_plant.__init__(unknown_plant_str, 0, 0, 0)
        return (unknown_plant)

    def set_name(self, new: str):

        success_str = update_success_str % (self._name, name_str, "")
        err_str = empty_error_str % (self._name, str_str)

        if (not new):
            print(err_str)
            return
        self._name = new
        print(success_str)

    def set_age(self, new: int):

        success_str = update_success_str % (age_str, new, age_suf)
        err_str_0 = type_error_str % (self._name, age_str, int_str)
        err_str_0 += "\n" + update_rejected_str % age_str
        err_str_1 = negative_error_str % (self._name, age_str.lower())
        err_str_1 += "\n" + update_rejected_str % age_str

        if (not is_number(new)):
            print(err_str_0)
            return
        if (is_negative(new)):
            print(err_str_1)
            return
        self._age = new
        print(success_str)

    def set_height(self, new: float):

        success_str = update_success_str % (height_str, new, height_suf)
        err_str_0 = type_error_str % (self._name, height_str, float_str)
        err_str_0 += "\n" + update_rejected_str % height_str

        if (not is_number(new)):
            print(err_str_0)
            return

        err_str_1 = negative_error_str % (self._name, height_str.lower())
        err_str_1 += "\n" + update_rejected_str % height_str

        if (is_negative(new)):
            print(err_str_1)
            return

        self._height = new
        print(success_str)

    def set_grow_rate(self, new: float):

        success_str = update_success_str % (grow_rate_str, new, "")
        err_str_0 = type_error_str % (self._name, grow_rate_str, float_str)
        err_str_0 += "\n" + update_rejected_str % grow_rate_str

        if (not is_number(new)):
            print(err_str_0)
            return

        err_str_1 = negative_error_str % (self._name, grow_rate_str.lower())
        err_str_1 += "\n" + update_rejected_str % grow_rate_str

        if (is_negative(new)):
            print(err_str_1)
            return

        self._grow_rate = new
        print(success_str)

    def get_name(self):
        return (self._name)

    def get_age(self):
        return (self._age)

    def get_height(self):
        return (self._height)

    def age(self, add_days=1):
        self._stats.increment_aged()
        self._age += add_days

    def grow(self, add_cm=0):
        self._stats.increment_grown()
        if (add_cm <= 0):
            self._height += self._height * self._grow_rate
        else:
            self._height += add_cm

    def show(self):

        out = f"{self._name}: {round(self._height, 1)}{height_suf}, "
        out += f"{self._age}{age_suf}"

        self._stats.increment_shown()
        print(out)

    def display_stats(self):
        self._stats.display()


# ------------ child classes ------------


class Flower(Plant):

    """
    It is a pretty type of plant
    """

    _color: str
    _has_bloomed: bool

    def __new__(
        cls,
        name=default_name % flower_str,
        height=default_height,
        age=default_age,
        grow_rate=default_grow_rate,
        color=default_color
    ):

        flower = object.__new__(cls)
        return (flower)

    def __init__(
        self,
        name=default_name % flower_str,
        height=default_height,
        age=default_age,
        grow_rate=default_grow_rate,
        color=default_color
    ):

        super().__init__(name, height, age, grow_rate)
        self._color = color
        self._has_bloomed = False

    def set_color(self, new: str):

        self._color = new

    def get_color(self):
        return (self._color)

    def show(self):

        super().show()
        print(f"{color_str}: {self._color}")
        if self._has_bloomed:
            print(bloom_true_str % self._name)
        else:
            print(bloom_false_str % self._name)

    def bloom(self):

        self._has_bloomed = True


class Tree(Plant):

    """
    It is an impressive type of plant
    """

    _trunk_diameter: float

    def __new__(
        cls,
        name=default_name % tree_str,
        height=default_height,
        age=default_age,
        grow_rate=default_grow_rate,
        trunk_diameter=default_diameter
    ):

        tree = object.__new__(cls)
        return (tree)

    def __init__(
        self,
        name=default_name % tree_str,
        height=default_height,
        age=default_age,
        grow_rate=default_grow_rate,
        trunk_diameter=default_diameter
    ):

        super().__init__(name, height, age, grow_rate)
        self._trunk_diameter = trunk_diameter

    class Statistics(Plant.Statistics):

        def __init__(self):
            super().__init__()
            self._shaded = 0

        def increment_shaded(self):
            self._shaded += 1

        def get_shaded(self):
            return (self._shaded)

        def display(self):

            additional_stats_str = "%d shade"

            super().display()
            print(additional_stats_str % self.get_shaded())

    def set_trunk_diameter(self, new: float):
        self._trunk_diameter = new

    def get_trunk_diameter(self):
        return (self._trunk_diameter)

    def show(self):

        super().show()
        print(f"{trunk_diameter_str}: {self._trunk_diameter}{height_suf}")

    def produce_shade(self):

        self._stats.increment_shaded()
        print(
            shadow_true_str %
            (self._name, self._height, self._trunk_diameter)
        )


class Vegetable(Plant):

    """
    It is a tasty type of plant
    """

    _harvest_season: str
    _nutrional_value: int

    def __new__(
        cls,
        name=default_name % vegetable_str,
        height=default_height,
        age=default_age,
        grow_rate=default_grow_rate,
        harvest_season=harvest_season_default,
        nutrional_value=nutrional_value_default
    ):

        vegetable = object.__new__(cls)
        return (vegetable)

    def __init__(
        self,
        name=default_name % vegetable_str,
        height=default_height,
        age=default_age,
        grow_rate=default_grow_rate,
        harvest_season=harvest_season_default,
        nutrional_value=nutrional_value_default
    ):

        super().__init__(name, height, age, grow_rate)
        self._harvest_season = harvest_season
        self._nutrional_value = nutrional_value

    def set_harvest_season(self, new: str):
        self._harvest_season = new

    def get_harvest_season(self):
        return (self._harvest_season)

    def set_nutritional_value(self, new: int):
        self._nutrional_value = new

    def get_nutritional_value(self):
        return (self._nutrional_value)

    def show(self):

        super().show()
        print(f"{harvest_season_str}: {self._harvest_season}")
        print(f"{nutritional_value_str}: {self._nutrional_value}")

    def grow_and_age(self, days: int):

        print(make_vegetable_str % (self._name, days))
        for i in range(days):
            self.grow()
            self.age()
        self._nutrional_value += days


# ------------ child child classes ------------


class Seed(Flower):

    """
    just like Flower but contains Seeds, despite a seed can't bloom
    what ever... that's so unlogical :/
    """

    _seeds: int

    def __new__(
        cls,
        name=default_name % flower_str,
        height=default_height,
        age=default_age,
        grow_rate=default_grow_rate,
        color=default_color
    ):

        seed_flower = object.__new__(cls)
        return (seed_flower)

    def __init__(
        self,
        name=default_name % flower_str,
        height=default_height,
        age=default_age,
        grow_rate=default_grow_rate,
        color=default_color
    ):

        super().__init__(name, height, age, grow_rate, color)
        self._seeds = 0

    def get_seeds(self):
        return (self._seeds)

    def bloom(self):
        super().bloom()
        self._seeds += 42

    def show(self):
        new_atribute = "Seeds: %d"
        super().show()
        print(new_atribute % self.get_seeds())


# ++++++++++++++++++++ functions ++++++++++++++++++++++

# --- funcs ---


def plant_display_stats(plant: Plant):

    display_str = "[statistics for %s]"
    type_err_str = "Error, wrong type"
    try:
        print(display_str % plant.get_name())
        plant.display_stats()
    except TypeError:
        print(type_err_str)


# --- utils ---


def is_number(var) -> bool:

    try:
        var >= 0.00
    except TypeError:
        return (False)

    return (var is not True)


def is_negative(nbr: int | float) -> bool:

    if (nbr < 0):
        return (True)
    return (False)


# --- main ---


def main():

    print(intro_str)

    print("=== Check year-old")
    year_question_str = "Is %d days more than a year? -> %s"
    print(year_question_str % (30, Plant.is_older_than_a_year(30)))
    print(year_question_str % (400, Plant.is_older_than_a_year(400)))

    print("\n=== Flower")
    flower_request_str = "[asking the %s to grow and bloom]"
    flower0 = Flower(
        name="Rose",
        height=15.0,
        age=10,
        grow_rate=0.05,
        color="red")
    flower0.show()
    plant_display_stats(flower0)
    print(flower_request_str % flower0.get_name())
    flower0.grow()
    flower0.bloom()
    flower0.show()
    plant_display_stats(flower0)

    print("\n=== Tree")
    tree_request_str = "[asking the %s to produce shade]"
    tree0 = Tree(
        name="Oak",
        height=200.0,
        age=365,
        grow_rate=0.003,
        trunk_diameter=5.0)
    tree0.show()
    plant_display_stats(tree0)
    print(tree_request_str % tree0.get_name())
    tree0.produce_shade()
    plant_display_stats(tree0)

    print("\n=== Seed")
    seed_request_str = "[make %s grow, age and bloom]"
    print("under construction")
    seed0 = Seed(
        name="Sunflower",
        height=80.0,
        age=45,
        grow_rate=0.05,
        color="yellow"
    )
    seed0.show()
    print(seed_request_str % seed0.get_name())
    seed0.grow(30.0)
    seed0.age(20)
    seed0.bloom()
    seed0.show()
    plant_display_stats(seed0)

    print("\n=== Anonymus")
    unknown = Plant.create_unknown()
    unknown.show()
    plant_display_stats(unknown)

    print(outro_str)

# ++++++++++++++++++++ run ++++++++++++++++++++++


if __name__ == '__main__':

    main()
