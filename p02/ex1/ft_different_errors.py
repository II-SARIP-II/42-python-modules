def garden_operations(value_str, zero, file, person):
    """
    Executes a series of operations prone to common Python exceptions.

    Args:
        value_str (str): A string to convert to an integer (ValueError).
        zero (int): A number to divide by (potential ZeroDivisionError).
        file (str): A filename to open (potential FileNotFoundError).
        person (str): A key to look up in the age dictionary (KeyError).
    """
    int(value_str)
    20 / zero
    open(file)
    age = {
        "Pâris": 21,
        "Karl Marx": 177,
        "Neymar": 33
    }
    return age[person]


def test_error_types():
    """
    Demonstrates how to catch specific built-in exceptions and multiple
    exceptions using try/except blocks.
    """
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        garden_operations("abc", 1, "ft_different_errors.py", "Neymar")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("10", 0, "ft_different_errors.py", "Neymar")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("10", 1, "missing.txt", "Neymar")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print("\nTesting KeyError...")
    try:
        garden_operations("10", 1, "ft_different_errors.py", "Antoine")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print("\nTesting multiple errors together...")
    try:
        garden_operations("abc", 0, "missing.txt", "Ghost")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
