#!/usr/bin/python3

# +++++++++++++++++++++++++++ import +++++++++++++++++++++++++++

import sys
import io

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Cyber Archives Recovery & Preservation ===\n"

stderr_prefix_str = "[STDERR]: "

error_str = "Error opening file '%s': %s\n"
success_str = "Accessing file '%s'\n"
transform_str = "Transform data:\n"
content_str = "---\n\n%s\n---\n"

inp_str = "Enter new file name (or empty): "
close_str = "File '%s' closed.\n"

end_of_line_str = '#'

not_saved_str = "Not saving data.\n"
saving_str = "Saving data to '%s'\n"
saved_str = "Data saved in file '%s'.\n"

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
        lxy_print_to_cli([error_str, path, str(err)], 2)
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
        lxy_print_to_cli([close_str, path])


def file_to_str(f: io.TextIOWrapper) -> str:

    return (f.read())


def str_to_file(f: io.TextIOWrapper, content: str) -> None:

    f.write(content)


# --------------- cli interface ---------------


def lxy_print_to_cli(
    to_print: list[str | int | float],
    fd: int = 1
) -> None:

    output: str

    output = list_merge_to_str(to_print)
    if (fd == 1):
        sys.stdout.write(output)
        sys.stdout.flush()
    elif (fd == 2):
        sys.stdout.write(stderr_prefix_str)
        sys.stdout.flush()
        sys.stderr.write(output)
        sys.stderr.flush()
    else:
        return


def lxy_input_from_cli(
    to_print: list[str | int | float] = []
) -> str:

    output: str
    inp: str

    output = ''
    if (to_print):
        output = list_merge_to_str(to_print)

    sys.stdout.write(output)
    sys.stdout.flush()
    inp = sys.stdin.readline()
    sys.stdin.flush()
    inp = inp[:-1]
    return (inp)


# --------------- utils ---------------


def str_add_to_end_of_line(s: str, sub_str: str) -> str:

    nl: str
    lines: list[str]

    nl = '\n'
    lines = [line + sub_str for line in s.split(nl) if line]
    return (nl.join(lines) + nl if lines else '')


def list_merge_to_str(to_merge: list[str | int | float]) -> str:

    merged: str
    to_merge_alt: list[str]

    merged = ''
    if (to_merge):
        merged = str(to_merge[0])
        to_merge = to_merge[1:]

    if (to_merge):
        try:
            merged = merged % tuple(to_merge)
        except TypeError:
            to_merge_alt = [str(element) for element in to_merge]
            merged = merged + ''.join(to_merge_alt)

    return (merged)


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
        lxy_print_to_cli([success_str, argv[i]])
        lxy_print_to_cli([content_str, content])
        file_close(f, argv[i])

        lxy_print_to_cli([transform_str])
        content = str_add_to_end_of_line(content, end_of_line_str)
        lxy_print_to_cli([content_str, content])

        new_file = lxy_input_from_cli([inp_str])
        if (not new_file):
            lxy_print_to_cli([not_saved_str])
            i += 1
            continue
        f = file_create_open(new_file)
        lxy_print_to_cli([saving_str, new_file])
        str_to_file(f, content)
        f.close()
        lxy_print_to_cli([saved_str, new_file])
        i += 1

# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
