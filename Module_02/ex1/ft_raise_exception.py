#!/usr/bin/python3

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Garden Temperature Checker ==="
outro_str = "All tests completed - program didn't crash!"


# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++


class TemperatureError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)


# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++

# --------------- checker functions ---------------


def input_temperature(temperature: int | float):

    terminal_output_str = "Input data is '%s'"
    err_str = "Caught input_temperature error: %s"

    print(terminal_output_str % temperature)
    try:
        int(temperature)
    except ValueError as err:
        print(err_str % err)
        raise

    return (temperature)


def test_temperature(temperature: int):

    success_str = "Temperature is now %d°C"
    err_str = "Caught input_temperature error: %s"
    err_cold_str = "%d °C is too cold for plants (max %d°C)"
    err_hot_str = "%d °C is too hot for plants (min %d°C)"

    min_temp = 0
    max_temp = 40

    try:
        input_temperature(temperature)
        if (temperature < min_temp):
            raise TemperatureError(err_cold_str % (temperature, min_temp))
        if (temperature > max_temp):
            raise TemperatureError(err_hot_str % (temperature, max_temp))
        print(success_str % temperature)
    except ValueError:
        return
    except TemperatureError as err:
        print(err_str % err)


# --------------- main ---------------


def main():

    print(intro_str, '\n')
    test_temperature(25)
    print('')
    test_temperature('abc')
    print('')
    test_temperature(100)
    print('')
    test_temperature(-50)
    print('')
    print(outro_str)


# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
