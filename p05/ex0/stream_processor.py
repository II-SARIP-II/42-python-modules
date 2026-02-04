from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid Numeric Data"
        data_len = len(data)
        data_s = sum(data)
        avg = data_s / data_len
        return self.format_output(f"{data_len} numeric values"
                                  f", sum={data_s}, avg={avg}")

    def validate(self, data: Any) -> bool:
        try:
            all(int(x) for x in data)
            return True
        except (TypeError, ValueError):
            return False

    def format_output(self, result: str) -> str:
        return ("Processed " + result)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid Text Data"
        return self.format_output(data)

    def validate(self, data: Any) -> bool:
        return type(data) is str

    def format_output(self, result: str) -> str:
        return (f"Processed text: {len(result)}"
                f" characters, {len(result.split())} words")


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid Log Data"
        return self.format_output(data)

    def validate(self, data: Any) -> bool:
        return type(data) is str

    def format_output(self, result: str) -> str:
        if "ERROR" in result:
            log_type = "ALERT"
        else:
            log_type = "INFO"
        return f"[{log_type}] {result}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    nume = NumericProcessor()
    txt = TextProcessor()
    logp = LogProcessor()
    my_list = [1, 2, 3, 4, 5]
    my_text = "Hello Nexus World"
    my_log = "ERROR: Connection timeout"

    print("Initializing Numeric Processor...")
    print(f"Processing data: {my_list}")
    if nume.validate(my_list):
        print("Validation: Numeric data verified")
    print("Output: " + nume.process(my_list), end="\n\n")

    print("Initializing Text Processor...")
    print(f"Processing data: {my_text}")
    if txt.validate(my_text):
        print("Validation: Text data verified")
    print("Output: " + txt.process(my_text), end="\n\n")

    print("Initializing Log Processor...")
    print(f"Processing data: {my_log}")
    if logp.validate(my_log):
        print("Validation: Log data verified")
    print("Output: " + logp.process(my_log))
    print("\nFoundation systems online. Nexus ready for advanced streams.\n")

    print("Processing multiple data types through same interface...")
    print("=== Polymorphic Processing Demo ===\n")
    lst = {nume: my_list, txt: my_text, logp: my_log}
    i = 1
    for p in lst:
        print(f"Result {i}: {p.process(lst[p])}")
        i += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")
