class GardenError(Exception):
    """Base class for garden exceptions"""
    pass


class PlantValidationError(GardenError):
    """Raised when plant data is invalid"""
    pass


class ResourceError(GardenError):
    """Raised when water or sun resources are out of bounds"""
    pass


class Plant:
    '''Plant Class : name, height, days, sunlight, water_level'''
    def __init__(self, name, height, days, sunlight, water_level):
        '''Creating Plant : name, height, days, sunlight, water_level'''
        self.name = name
        self.__height = height
        self.__days = days
        self.sunlight = sunlight
        self.water_level = water_level

    def get_info(self):
        '''Returning all infos'''
        return (f"{self.name}: (height: {self.__height}cm, water: "
                f"{self.water_level}, days : {self.__days}, "
                f"sun: {self.sunlight})")

    def grow(self):
        '''Increment __height'''
        self.__height += 1

    def age(self):
        '''Increment __days'''
        self.__days += 1

    def watering(self):
        '''Increment water_level'''
        self.water_level += 1

    def set_sunlight(self, sunlight):
        '''setting sunlight'''
        if 2 <= sunlight <= 12:
            self.sunlight = sunlight
        else:
            print("Invalid operation attempted: sunlight", sunlight,
                  "cm [REJECTED]\nSecurity: Value rejected (between 2 and 12)")

    def set_age(self, days):
        '''setting age'''
        if days >= 0:
            self.__days = days
        else:
            print("Invalid operation attempted: age", days,
                  "cm [REJECTED]\nSecurity: Negative age rejected")

    def set_height(self, height):
        '''setting height'''
        if height >= 0:
            self.__height = height
        else:
            print("Invalid operation attempted: height", height,
                  "cm [REJECTED]\nSecurity: Negative height rejected")

    def get_age(self):
        '''returning age'''
        return (self.__days)

    def get_height(self):
        '''returning height'''
        return (self.__height)


class GardenManager:
    '''GardenManager Class : plants[ ]'''
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        '''Verify plant name and append it to self.plants[ ]'''
        try:
            if not plant.name:
                raise PlantValidationError("Plant name cannot be empty!")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantValidationError as e:
            print(f"Error adding plant: {e}")

    def watering_system(self):
        '''Increment watering level from every plants in self.plants[ ]'''
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant.water_level > 10:
                    raise ResourceError(f"Water level {plant.water_level}"
                                        f"is too high for {plant.name}")
                plant.water_level += 1
                print(f"Watering {plant.name} - success")
        except ResourceError as e:
            print(f"Watering Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self):
        '''Verify Name, Sunlight, Water_level and raise error if needed'''
        print("Checking plant health...")
        for plant in self.plants:
            try:
                if plant.sunlight > 12:
                    raise ResourceError(f"{plant.name} sunlight too high!")
                if plant.sunlight < 2:
                    raise ResourceError(f"{plant.name} sunlight too low!")
                if plant.water_level < 1:
                    raise ResourceError(f"Water level {plant.water_level}"
                                        f"is too low for {plant.name}")
                if plant.water_level > 10:
                    raise ResourceError(f"Water level {plant.water_level}"
                                        f"is too high for {plant.name}")
                print(f"{plant.get_info()} - healthy")
            except ResourceError as e:
                print(f"Health Alert: {e}")


if __name__ == "__main__":
    print("=== Garden Management System ===")
    gm = GardenManager()
    print("")
    gm.add_plant(Plant("Tomato", 10, 5, 8, 5))
    gm.add_plant(Plant("", 5, 2, 5, 3))
    print("")
    gm.watering_system()
    print("")
    gm.check_health()
    print("")
    print("Garden management system test complete!")
