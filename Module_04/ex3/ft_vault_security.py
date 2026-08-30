#!/usr/bin/python3

# +++++++++++++++++++++++++++ import +++++++++++++++++++++++++++

# no imports

# +++++++++++++++++++++++++++ globals +++++++++++++++++++++++++++

# --------------- strings ---------------

intro_str = "=== Cyber Archives Security ==="

error_str = "Error opening file '%s': %s"
invalid_action_str = "invalid action: choose: 1 / 'read' or 2 / write"

not_saved_str = "Not saving data:"
not_saved_str += "data brobably broken or error occured earlier"
saved_str = "Content successfully written to file"

test_non_existent_str = "Using '%s' to read from a nonexistent file:"
test_forbidden_str = "Using '%s' to read from an inaccessible file:"
test_regular_str = "Using '%s' to read from a regular file:"
write_to_new_str = "Using '%s' to write previous content to a new file:"

non_existing_file = "./not/existing/file"
forbidden_file = "./etc/master.passwd"
regular_file = "archive.txt"
new_file = "sniggle.txt"

function_name = "secure_archive"

ctrl_read = ['1', 'read']
ctrl_write = ['2', 'write']

# +++++++++++++++++++++++++++ classes +++++++++++++++++++++++++++

# no classes

# +++++++++++++++++++++++++++ funcs +++++++++++++++++++++++++++

# --------------- file_interface ---------------


def secure_archive(
    path: str,
    action: str | int = 1,
    content: str = ''
) -> tuple[bool, str]:

    data: tuple[bool, str]

    if (str(action).lower() in ctrl_read):
        data = file_read_from(path)
    elif (str(action).lower() in ctrl_write):
        data = file_write_to(path, content)
    else:
        data = (False, invalid_action_str)

    return (data)


def file_read_from(path: str) -> tuple[bool, str]:

    data: tuple[bool, str]

    try:
        with open(path, 'r') as f:
            data = (True, f.read())
    except (FileNotFoundError, PermissionError) as err:
        data = (False, error_str % (path, err))

    return (data)


def file_write_to(path: str, content: str) -> tuple[bool, str]:

    data: tuple[bool, str]

    try:
        with open(path, 'w') as f:
            f.write(content)
        data = (True, saved_str)
    except (FileNotFoundError, PermissionError) as err:
        data = (False, error_str % (path, err))

    return (data)


# --------------- main ---------------


def main() -> None:

    control: bool
    content: str
    data: tuple[bool, str]

    print(intro_str, '\n')

    print(test_non_existent_str % function_name)
    data = secure_archive(non_existing_file)
    print(data, '\n')

    print(test_forbidden_str % function_name)
    data = secure_archive(forbidden_file)
    print(data, '\n')

    print(test_regular_str % function_name)
    data = secure_archive(regular_file)
    print(data, '\n')

    print(write_to_new_str % function_name)
    control, content = data
    if (control):
        data = secure_archive(
            path=new_file,
            action='write',
            content=content
        )
    else:
        data = (False, not_saved_str)
    print(data)


# +++++++++++++++++++++++++++ run +++++++++++++++++++++++++++


if __name__ == "__main__":

    main()
