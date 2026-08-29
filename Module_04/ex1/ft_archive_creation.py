#!/usr/bin/python3

# +++++++++++++++++++++++++++ import +++++++++++++++++++++++++++

import sys
import io

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Cyber Archives Recovery & Preservation ==="

error_str = "Error opening file '%s': "
success_str = "Accessing file '%s'"
transform_str = "Transform data:"
content_str = "---\n\n%s\n---"

inp_str = "Enter new file name (or empty): "
close_str = "File '%s' closed."

end_of_line_str = '#'

not_saved_str = "Not saving data."
saving_str = "Saving data to '%s'"
saved_str = "Data saved in file '%s'."

# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++

# no classes

# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++

# --------------- pass_arguments ---------------


def get_argc_argv() -> tuple[int, list[str]]:

    argv = sys.argv
    return (len(argv), argv)


# --------------- file_interface ---------------


def file_open(path: str) -> io.TextIOWrapper | None:

    f: io.TextIOWrapper

    try:
        f = open(path, 'r')
    except (FileNotFoundError, PermissionError) as err:
        print(error_str, err)
        return None

    return (f)


def file_open_no_err(path: str) -> io.TextIOWrapper:

    return open(path, 'r')


def file_create_open(path: str) -> io.TextIOWrapper:

    f: io.TextIOWrapper

    f = open(path, 'w')
    return (f)


def file_close(f: io.TextIOWrapper, path: str = '') -> None:

    f.close()
    if (path):
        print(close_str % path)


def file_to_str(f: io.TextIOWrapper) -> str:

    return (f.read())


def str_to_file(f: io.TextIOWrapper, content: str) -> None:

    f.write(content)


# --------------- utils ---------------


def str_add_to_end_of_line(s: str, sub_str: str) -> str:

    nl: str
    lines: list[str]

    nl = '\n'
    lines = [line + sub_str for line in s.split(nl) if line]
    return (nl.join(lines) + nl if lines else '')


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

        print(transform_str)
        content = str_add_to_end_of_line(content, end_of_line_str)
        print(content_str % content)

        new_file = input(inp_str)
        if (not new_file):
            print(not_saved_str)
            i += 1
            continue
        f = file_create_open(new_file)
        print(saving_str % new_file)
        str_to_file(f, content)
        f.close()
        print(saved_str % new_file)
        i += 1

# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
