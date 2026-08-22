#!/usr/bin/python3

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Garden Temperature ==="
outro_str = "All tests completed - program didn't crash!"


# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++

# --------------- checker functions ---------------


def input_temperature(temperature: int | float):

    terminal_output_str = "Input data is '%s'"
    success_str = "Temperature is now %d°C"
    err_str = "Caught input_temperature error: %s"

    print(terminal_output_str % temperature)
    try:
        int(temperature)
        print(success_str % temperature)
    except ValueError as e:
        print(err_str % e)


# --------------- main ---------------


def main():

    print(intro_str, '\n')
    input_temperature(25)
    print('')
    input_temperature('abc')
    print('')
    print(outro_str)


# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
