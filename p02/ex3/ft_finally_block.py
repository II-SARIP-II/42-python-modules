class PlantError(Exception):
    '''Custom exception for errors related to plant management.'''
    pass


def water_plants(plant_list):
    '''
    Simulates the process of watering a list of plants.

    Args:
        plant_list (list): A list of plant names (strings).
                          Can contain None to simulate an error.

    Raises:
        PlantError: If a None value is encountered in the plant list.
    '''
    print("=== Garden Watering System ===")
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise PlantError("invalid plant!")
            print(f"Watering {plant}")
        print("Watering completed successfully!")
    except PlantError as e:
        print(f"Error: Cannot water None - {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    '''
    Tests the water_plants function with both valid and invalid data
    to demonstrate the try/except/finally flow.
    '''
    plant_list_good = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering...")
    water_plants(plant_list_good)

    print("\n" + "-"*30 + "\n")

    # 2. Watering with error
    plant_list_bad = ["tomato", None, "carrots"]
    print("Testing with error...")
    water_plants(plant_list_bad)
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
