def check_plant_health(plant_name, water_level, sunlight_hours):
    '''Checking Name, Water_level, Sunlight_hours and raising errors'''
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Error: Water level \
                         {water_level} is too hight (min 10)")
    if water_level < 1:
        raise ValueError(f"Error: Water level \
                         {water_level} is too low (min 2)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours \
                         {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours \
                         {sunlight_hours} is too hight (max 12)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    '''Creating test for check_plant_health'''
    plants = [
        ["Tomato", 5, 10],
        [None, 5, 10],
        ["Tomato", 0, 10],
        ["Tomato", 11, 10],
        ["Tomato", 5, 0],
        ["Tomato", 5, 13]
    ]
    i = 0
    while i < len(plants):
        try:
            check_plant_health(plants[i][0], plants[i][1], plants[i][2])
            i += 1
        except ValueError as e:
            print(e)
            i += 1
    print("All error raising tests completed")


test_plant_checks()
