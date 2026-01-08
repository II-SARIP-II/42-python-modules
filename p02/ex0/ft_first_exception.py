def check_temperature(temp_str):
    """
    Validates a temperature reading string for agricultural use.
    The function attempts to convert the input to an integer and checks
    if it falls within the safe biological range for plants (0°C - 40°C).
    Args:
        temp_str (str): The temperature reading received from a sensor.
    Returns:
        int/None: Returns the temperature if valid, or None if an error occurs.
    """
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    if 0 <= temp <= 40:
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    return None


def test_temperature_input():
    """
    Runs a suite of test cases against the check_temperature function
    to demonstrate robust error handling and data validation.
    """
    print("=== Garden Temperature Checker ===")
    print("\n")
    check_temperature("25")
    print("\n")
    check_temperature("abc")
    print("\n")
    check_temperature("100")
    print("\n")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
