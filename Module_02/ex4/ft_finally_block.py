#!/usr/bin/python3

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Garden Watering System ==="
outro_str = "Cleanup always happens, even with errors!"

temperature_err_default = "Unknown temperature error"
garten_err_default = "Unknown garden error"
plant_err_default = "Unknown plant error"
water_err_default = "Unknown water error"

testing_valid_str = "Testing valid plants..."
testing_invalid_str = "Testing invalid plants..."
opening_str = "Opening watering system"
closing_str = "Closing watering system"
watering_str = "Watering %s: [OK]"
error_str = "Invalid plant name to water: '%s'"
error_caught_str = "Caught PlantError: %s"
ending_str = ".. ending tests and returning to main"


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


def water_plant(plant_name):

    if plant_name != plant_name.capitalize():
        raise PlantError(error_str % plant_name)
    print(watering_str % plant_name)


def test_watering_system(plants_list, test_name):

    print(test_name)
    try:
        print(opening_str)
        for plant in plants_list:
            water_plant(plant)
    except PlantError as err:
        print(error_caught_str % err)
        print(ending_str)
        return
    finally:
        print(closing_str, '\n')


# --------------- main ---------------


def main():

    print(intro_str, '\n')
    test_watering_system(
        ["Tomato", "Lettuce", "Carrots"],
        testing_valid_str
    )
    test_watering_system(
        ["Tomato", "lettuce"],
        testing_invalid_str
    )
    print(outro_str)


# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
