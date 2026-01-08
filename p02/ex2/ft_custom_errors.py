class GardenError(Exception):
    """Base class for all garden-related exceptions."""
    pass


class PlantError(GardenError):
    """Exception raised for problems specifically related to plants."""
    pass


class WaterError(GardenError):
    """Exception raised for problems related to the watering system."""
    pass


def check_plant_health(state):
    """
    Checks the health status of a plant.
    Args:
        state (int): The health state (0 for wilting, 1 for healthy).
    Raises:
        PlantError: If the plant state indicates wilting.
    """
    if state == 0:
        raise PlantError("The tomato plant is wilting!")


def check_water_level(level):
    """
    Monitors the water levels in the reservoir.
    Args:
        level (int): Percentage of water remaining.
    Raises:
        WaterError: If the water level drops below 10%.
    """
    if level < 10:
        raise WaterError("Not enough water in the tank!")


def check_valid_age(age):
    """
    Validates the recorded age of a plant.
    Args:
        age (int): Age of the plant in days.
    Raises:
        PlantError: If the age is negative.
    """
    if age < 0:
        raise PlantError("Negative age not possible!")


def test_garden_exception():
    """
    Demonstrates the functionality of custom exceptions and inheritance.
    This test shows:
    1. Catching specific child exceptions.
    2. Catching multiple error types using the parent GardenError class.
    """
    plant = {
        "name": "Tomato",
        "age": -1,
        "state": 0,
        "water_level": 5
    }
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        check_plant_health(plant["state"])
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("Testing WaterError...")
    try:
        check_water_level(plant["water_level"])
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("Testing catching all garden errors...")
    try:
        check_plant_health(plant["state"])
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_water_level(plant["water_level"])
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_garden_exception()
