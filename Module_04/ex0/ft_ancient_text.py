#!/usr/bin/python3

# +++++++++++++++++++++++++++ import +++++++++++++++++++++++++++

import sys
import io

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Cyber Archives Recovery ==="

error_str = "Error opening file '%s': %s"
success_str = "Accessing file '%s'"
content_str = "---\n\n%s\n---"

close_str = "File '%s' closed."

# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++

# no classes

# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++

# --------------- pass_arguments ---------------


def get_argc_argv() -> tuple[int, list[str]]:

    argv = sys.argv
    return (len(argv), argv)


# --------------- file_interface ---------------


def file_open(path: str) -> io.TextIOWrapper | None:

    try:
        f = open(path, 'r')
    except (FileNotFoundError, PermissionError) as err:
        print(error_str % (path, err))
        return None

    return (f)


def file_open_no_err(path: str) -> io.TextIOWrapper:

    return open(path, 'r')


def file_close(f: io.TextIOWrapper, path: str = '') -> None:

    f.close()
    if (path):
        print(close_str % path)


def file_to_str(f: io.TextIOWrapper) -> str:

    return (f.read())


# --------------- utils ---------------

# no utils

# --------------- main ---------------


def main() -> None:

    argc: int
    argv: list[str]
    i: int
    catch: io.TextIOWrapper | None
    f: io.TextIOWrapper
    content: str

    i = 1
    argc, argv = get_argc_argv()
    if (argc < 2):
        return
    while (i < argc):
        catch = file_open(argv[i])
        if (catch is None):
            i += 1
            continue
        f = file_open_no_err(argv[i])

        content = file_to_str(f)
        print(success_str % argv[i])
        print(content_str % content)
        file_close(f, argv[i])
        i += 1


# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
