#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import abc
import typing

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------

intro_str = "=== Code Nexus - Data Processor ==="

testing_numeric_str = "Testing Numeric Processor..."
testing_text_str = "Testing Text Processor..."
testing_log_str = "Testing Log Processor..."

validate_str = "Trying to validate input '%s': %s"
ingest_no_valid_str = "Test invalid ingestion of %s '%s'"
ingest_no_valid_str += " without prior validation:"
processing_str = "Processing data: %s"
extracting_str = "Extracting %d values..."

bonus_str = "--- additional tests ---"
bonus_store_add_str = "there is stil one element in store of TextProcessor"
bonus_store_add_str += " instance, remember?\nlet's add another one."
bonus_store_add_ctrl_str = "new element should have idx 3"
bonus_store_add_ctrl_str += " because remaining has idx 2\n let's check:"
bonus_store_empty_str = "there are also two elements in store of"
bonus_store_empty_str += " NumericProcessor\n"
bonus_store_empty_str += "Let's check whats happens if we extract three:"
bonus_store_empty_not_crash_str = "programm didn't crash :)"

bonus_log_multiple_values = "Passing dicts with more then two items to"
bonus_log_multiple_values += " LogProcessor"
bonus_log_empty_values = "Passing dicts with empty str values to LogProcessor"

# ---------------------------- container ----------------------------


class StringContainer:

    nonnumeric_err_str = "NonNumericError: expected int() |"
    nonnumeric_err_str += " float() with base 10"
    nontext_err_str = "NonTextError: expected str()"
    nonlog_err_str = "NonNumericError: expected dict{str(): str()}"

    numeric_value_str = "Numeric value %d: %s"
    text_value_str = "Text value %d: %s"
    log_value_str = "Log entry %d: %s"


class DefaultValues:

    empty_store_item = (-1, '<empty>')
    damaged_store_item = (-2, '<ERROR> damaged store')


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++

# ---------------------------- error cls ----------------------------


class NonNumericError(ValueError):

    """
    NonNumericError
    """

    def __init__(self) -> None:
        self.message = StringContainer.nonnumeric_err_str
        super().__init__(StringContainer.nonnumeric_err_str)


class NonTextError(ValueError):

    """
    NonTextError
    """

    def __init__(self) -> None:
        self.message = StringContainer.nontext_err_str
        super().__init__(StringContainer.nontext_err_str)


class NonLogError(ValueError):

    """
    NonLogError
    """

    def __init__(self) -> None:
        self.message = StringContainer.nonlog_err_str
        super().__init__(StringContainer.nonlog_err_str)


# ---------------------------- abstr/par ----------------------------


class DataProcessor(abc.ABC):

    """
    Processes and stores values use
    .ingest() to process,
    .output() to get the earliest data
    .validate() to validate the data
    """

    _store: typing.Any

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def __init__(self) -> None:
        self._store = dict()

    def output(self) -> tuple[int, str]:

        item: tuple[int, str]

        try:
            item = (key := next(iter(self._store)), self._store.pop(key))
        except StopIteration:
            item = DefaultValues.empty_store_item
        except AttributeError:
            item = DefaultValues.damaged_store_item

        return (item)


# ---------------------------- child ----------------------------


class NumericProcessor(DataProcessor):

    """
    Processes and stores Numeric values such as float and int
    takes int() | float() as solitary values or list[int|float]
    raises NonNumericError if invalid data were ingest
    """

    def validate(self, data: typing.Any) -> bool:

        try:
            iter(data)
        except TypeError:
            data = [data]

        for el in data:
            if (not isinstance(el, (int, float))):
                return (False)
        return (True)

    def ingest(self, data: typing.Any) -> None:

        local_buffer: list[int | float]
        idx: int

        local_buffer = []
        try:
            iter(data)
        except TypeError:
            data = [data]

        for el in data:
            if (not isinstance(el, (int, float))):
                raise NonNumericError

            local_buffer.append(el)

        try:
            idx = next(reversed(self._store)) + 1
        except StopIteration:
            idx = 0

        while (local_buffer):
            self._store.update({idx: str(local_buffer.pop(0))})
            idx += 1


class TextProcessor(DataProcessor):

    """
    Processes and stores Text values such as str
    takes int() as solitary value or list[str]
    raises NonTextError if invalid data were ingest
    """

    def validate(self, data: typing.Any) -> bool:

        if (not isinstance(data, list)):
            data = [data]

        for el in data:
            if (not isinstance(el, str)):
                return (False)

        return (True)

    def ingest(self, data: typing.Any) -> None:

        local_buffer: list[str]
        idx: int

        local_buffer = []
        if (not isinstance(data, list)):
            data = [data]

        for el in data:
            if (not isinstance(el, str)):
                raise NonTextError

            local_buffer.append(el)

        try:
            idx = next(reversed(self._store)) + 1
        except StopIteration:
            idx = 0

        while (local_buffer):
            self._store.update({idx: local_buffer.pop(0)})
            idx += 1


class LogProcessor(DataProcessor):

    """
    Processes and stores Log entries such as dict[str, str]
    takes dict[str, str] as solitary values or list[dict[str, str]]
    raises NonLogError if invalid data were ingest
    """

    def validate(self, data: typing.Any) -> bool:

        if (not isinstance(data, list)):
            data = [data]

        for el in data:

            if (not isinstance(el, dict)):
                return (False)

            for key, val in el.items():
                if (
                    not isinstance(key, str) or not isinstance(val, str)
                ):
                    return (False)

        return True

    def ingest(self, data: typing.Any) -> None:

        local_buffer: list[str]
        log_message: str
        idx: int

        local_buffer = []

        if (not isinstance(data, list)):
            data = [data]

        for el in data:
            if (not isinstance(el, dict)):
                raise NonLogError

            log_message = ""

            for key, val in el.items():
                if (
                    not isinstance(key, str) or not isinstance(val, str)
                ):
                    raise NonLogError

                log_message += ": " if log_message and val else ""
                log_message += val if val else ""

            local_buffer.append(log_message)

        try:
            idx = next(reversed(self._store)) + 1
        except StopIteration:
            idx = 0

        while (local_buffer):
            self._store.update({idx: local_buffer.pop(0)})
            idx += 1


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------

# def ...

# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:

    test_value: typing.Any
    ctrl: bool
    num_processor: NumericProcessor
    txt_processor: TextProcessor
    log_processor: LogProcessor

    print(intro_str, '\n')

    num_processor = NumericProcessor()
    txt_processor = TextProcessor()
    log_processor = LogProcessor()

    print(testing_numeric_str)
    test_value = 42
    ctrl = num_processor.validate(test_value)
    print(validate_str % (test_value, ctrl))
    test_value = "Hello"
    ctrl = num_processor.validate(test_value)
    print(validate_str % (test_value, ctrl))
    test_value = "foo"
    print(ingest_no_valid_str % (type(test_value), test_value))
    try:
        num_processor.ingest(test_value)
    except NonNumericError as err:
        print(err)
    test_value = [1, 2, 3, 4, 5]
    print(processing_str % test_value)
    try:
        num_processor.ingest(test_value)
    except NonNumericError as err:
        print(err)
    print(extracting_str % 3)
    for i in range(3):
        print(
            " ->", StringContainer.numeric_value_str % num_processor.output()
        )

    print('')
    print(testing_text_str)
    test_value = 42
    ctrl = txt_processor.validate(test_value)
    print(validate_str % (test_value, ctrl))
    test_value = ["Hello", "Nexus", "World"]
    print(processing_str % test_value)
    try:
        txt_processor.ingest(test_value)
    except NonTextError as err:
        print(err)
    print(extracting_str % 2)
    for i in range(2):
        print(
            " ->", StringContainer.text_value_str % txt_processor.output()
        )

    print('')
    print(testing_log_str)
    test_value = "Hello"
    ctrl = log_processor.validate(test_value)
    print(validate_str % (test_value, ctrl))
    test_value = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(processing_str % test_value)
    try:
        log_processor.ingest(test_value)
    except NonLogError as err:
        print(err)
    print(extracting_str % 2)
    for i in range(2):
        print(
            " ->", StringContainer.log_value_str % log_processor.output()
        )

    print('')
    print(bonus_str, '\n')
    print(bonus_store_add_str)
    test_value = "of Python"
    print(processing_str % test_value)
    txt_processor.ingest(test_value)
    print(bonus_store_add_ctrl_str)
    for i in range(2):
        print(
            " ->", StringContainer.text_value_str % txt_processor.output()
        )

    print('')
    print(bonus_store_empty_str)
    for i in range(3):
        print(
            " ->", StringContainer.numeric_value_str % num_processor.output()
        )
    print(bonus_store_empty_not_crash_str)

    print('')
    print(bonus_log_multiple_values)
    test_value = [
        {
            'log_level': 'ERROR',
            'log_message': 'Unauthorized access!!',
            'specification': 'someone tried to hack us'
        },
        {
            'log_level': 'IMPORTANT',
            'log_message': 'Server update',
            'specification': 'security update',
            'time_date': '2085-07-21-23-23-23'
        }
    ]
    print(processing_str % test_value)
    log_processor.ingest(test_value)
    print('\n', extracting_str % 2)
    for i in range(2):
        print(
            " ->", StringContainer.log_value_str % log_processor.output()
        )

    print('')
    print(bonus_log_empty_values)
    test_value = [
        {
            'log_level': 'BUG REPORT',
            'log_message': '',
            'specification': 'Empoye\'s session interrupted',
            'time_date': '',
            'Note': 'admin spilled coffe over technical divices'
        }
    ]
    print(processing_str % test_value)
    log_processor.ingest(test_value)
    print('\n', extracting_str % 2)
    for i in range(2):
        print(
            " ->", StringContainer.log_value_str % log_processor.output()
        )


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++


if __name__ == '__main__':

    main()
