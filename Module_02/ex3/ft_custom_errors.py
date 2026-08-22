#!/usr/bin/python3

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Custom Garden Errors Demo ==="
outro_str = "All custom error types work correctly!"

temperature_err_default = "Unknown temperature error"
garten_err_default = "Unknown garden error"
plant_err_default = "Unknown plant error"
water_err_default = "Unknown water error"

testing_plant_str = "Testing PlantError..."
testing_water_str = "Testing WaterError..."
testing_all_str = "Testing catching all garden errors..."
caught_str = "Caught %s: %s"


# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++


class TemperatureError(Exception):

    def __init__(self, message=temperature_err_default):
        self.message = message
        super().__init__(message)


class GardenError(Exception):

    def __init__(self, message=garten_err_default):
        self.message = message
        super().__init__(message)


class PlantError(GardenError):

    def __init__(self, message=plant_err_default):
        self.message = message
        super().__init__(message)


class WaterError(GardenError):

    def __init__(self, message=water_err_default):
        self.message = message
        super().__init__(message)


# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++

# --------------- checker functions ---------------


def raise_plant_error():

    raise PlantError("The tomato plant is wilting!")


def raise_water_error():

    raise WaterError("Not enough water in the tank!")


def test_plant_error():

    print(testing_plant_str)
    try:
        raise_plant_error()
    except PlantError as err:
        print(caught_str % (err.__class__.__name__, err))


def test_water_error():

    print(testing_water_str)
    try:
        raise_water_error()
    except WaterError as err:
        print(caught_str % (err.__class__.__name__, err))


def test_garden_errors():

    print(testing_all_str)
    try:
        raise_plant_error()
    except GardenError as err:
        print(caught_str % (err.__class__.__name__, err))
    try:
        raise_water_error()
    except GardenError as err:
        print(caught_str % (err.__class__.__name__, err))


# --------------- main ---------------


def main():

    print(intro_str, '\n')
    test_plant_error()
    print('')
    test_water_error()
    print('')
    test_garden_errors()
    print('')
    print(outro_str)


# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
