#!/usr/bin/python3

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Garden Error Types Demo ==="
outro_str = "All error types tested successfully!"


# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++

class TemperatureError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)


# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++

# --------------- checker functions ---------------


def garden_operations(operation_number):

    if operation_number == 0:
        result = int('abc')
    elif operation_number == 1:
        result = 10 / 0
    elif operation_number == 2:
        file = open('/non/existent/file')
        result = file
    elif operation_number == 3:
        result = "string" + 42
    else:
        result = None
    return (result)


def test_error_types():

    testing_str = "Testing operation %d..."
    caught_str = "Caught %s: %s"
    success_str = "Operation completed successfully"
    i = 0

    while (i <= 4):
        print(testing_str % i)
        try:
            garden_operations(i)
            print(success_str)
        except (
            ValueError, ZeroDivisionError, FileNotFoundError, TypeError
        ) as err:
            print(caught_str % (err.__class__.__name__, err))
        finally:
            i += 1


# NOTE:

"""
    type(<obj>) == <obj>.__class__

    ==> type(err).__name__ == err.__class__.__name__
"""


# --------------- main ---------------


def main():

    print(intro_str, '\n')
    test_error_types()
    print(outro_str)


# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
