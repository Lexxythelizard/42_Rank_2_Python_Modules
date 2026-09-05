#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import abc
import typing

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------

intro_str = "=== Code Nexus - Data Strem ==="

init_data_stream_str = "Initialize Data Stream..."

register_numeric_str = "Registering Numeric Processor"
register_other_str = "Registering other data processors"

first_batch_str = "Send first batch of data on stream: %s"
same_batch_str = "Send the same batch again"
consume_str = "Consume some elements from the data processors:"
consume_str += " Numeric %d, Text %d, Log %d"
extracting_str = ""

bonus_str = "--- additional tests ---"
bonus_store_add_ctrl_str = "new element should have idx 3"
bonus_store_empty_str = ""
bonus_store_empty_not_crash_str = "programm didn't crash :)"

bonus_log_multiple_values = ""
bonus_log_empty_values = ""

# ---------------------------- container ----------------------------


class StringContainer:

    nonnumeric_err_str = "NonNumericError: expected int() |"
    nonnumeric_err_str += " float() with base 10"
    nontext_err_str = "NonTextError: expected str()"
    nonlog_err_str = "NonNumericError: expected dict{str(): str()}"
    nonstream_err_str = "NonStreamError: expected list"

    nonproc_err_str = "NonProcessorError: expected DataProcessor"
    datastream_err_str = "DataStream error - Can't process element in stream"

    numeric_processor_str = "Numeric Processor"
    text_processor_str = "Text Processor"
    log_processor_str = "Log Processor"
    unknown_processor_str = "Unknown Processor"

    statistics_str = "%s: total %d items processed, remaining %d on processor"

    numeric_value_str = "Numeric value %d: %s"
    text_value_str = "Text value %d: %s"
    log_value_str = "Log entry %d: %s"

    datastream_statistic_str = "== DataStream statistics =="
    empty_statistic_str = "No processor found, no data"


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


class NonProcessorError(TypeError):

    """
    NonProcessorError
    """

    def __init__(
        self,
        message: str = StringContainer.nonproc_err_str
    ) -> None:
        self.message = message
        super().__init__(message)


class NonStreamError(TypeError):

    """
    NonStreamError
    """

    def __init__(
        self,
        message: str = StringContainer.nonstream_err_str
    ) -> None:
        self.message = message
        super().__init__(message)


class DataStreamError(TypeError):

    """
    DataStreamError
    """

    def __init__(
        self,
        message: str = StringContainer.datastream_err_str
    ) -> None:
        self.message = message
        super().__init__(message)


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

    def __len__(self) -> int:

        n: int

        try:
            n = len(self._store)
        except TypeError:
            n = 0
        finally:
            return (n)

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


# ---------------------------- abstr/par ----------------------------


class DataStream:

    """
    DOC
    """

    _processors: list[DataProcessor]
    _stats: list[typing.Any]

    class Stats:

        name: str
        processed: int
        stored: int

        def __init__(self, proc: DataProcessor) -> None:

            names: dict[type[DataProcessor], str]
            names = {
                NumericProcessor: StringContainer.numeric_processor_str,
                TextProcessor: StringContainer.text_processor_str,
                LogProcessor: StringContainer.log_processor_str
            }

            if (not isinstance(proc, DataProcessor)):
                raise NonProcessorError

            self.name = names.get(
                type(proc),
                StringContainer.unknown_processor_str)

            self.processed = 0
            self.stored = 0

    def __init__(self) -> None:
        self._processors = list()
        self._stats = []

    def register_processor(self, proc: DataProcessor) -> None:
        if (not isinstance(proc, DataProcessor)):
            raise NonProcessorError
        self._processors.append(proc)
        self._stats.append(self.Stats(proc))

    def process_stream(self, stream: list[typing.Any]) -> None:

        def process_data(data: typing.Any) -> None:

            idx = 0
            for processor in self._processors:
                if (processor.validate(data)):
                    processor.ingest(data)
                    self._stats[idx].processed += \
                        len(data) if isinstance(data, list) else 1
                    return
                idx += 1
                continue
            raise DataStreamError(
                message=f"{StringContainer.datastream_err_str}: {data}"
            )

        if (not isinstance(stream, list)):
            raise NonStreamError

        for data in stream:

            try:
                process_data(data)
            except DataStreamError as err:
                print(err)

    def print_processors_stats(self) -> None:

        print(StringContainer.datastream_statistic_str)

        if (not self._processors):
            print(StringContainer.empty_statistic_str)

        for idx, stat in enumerate(self._stats):
            stat.in_store = len(self._processors[idx])
            print(
                StringContainer.statistics_str %
                (stat.name, stat.processed, stat.in_store)
            )


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------

# def ...

# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:

    test_value: list[typing.Any]

    print(intro_str, '\n')

    print(init_data_stream_str)
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print('')
    print(register_numeric_str)
    data_stream.register_processor(NumericProcessor())
    print('')
    test_value = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]
    print(first_batch_str % test_value)
    data_stream.process_stream(test_value)
    data_stream.print_processors_stats()

    print('')
    print(register_other_str)
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())
    print(same_batch_str)
    data_stream.process_stream(test_value)
    data_stream.print_processors_stats()

    print('')
    print(consume_str % (3, 2, 1))
    for idx, consume in enumerate([3, 2, 1]):
        for i in range(consume):
            data_stream._processors[idx].output()
    data_stream.print_processors_stats()


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++


if __name__ == '__main__':

    main()
