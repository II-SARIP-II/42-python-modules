import functools
import time
import random


def spell_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


@spell_timer
def casting_spell(name: str) -> bool:
    f"""{name} spell"""
    print(f"Throwing a {name} to the enemy")


def power_validator(min_power: int) -> callable:
    def decorator(func: callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            pwr = args[2] if len(args) > 2 else args[0]
            if pwr >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print("Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
                    else:
                        return ("Spell casting failed after "
                                f"{max_attempts} attempts")

        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("=========== Testing spell timer ===========")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\n=========== Testing MageGuild ===========")
    guild = MageGuild()
    print(guild.validate_mage_name("Gandalf"))
    print(guild.validate_mage_name("G1"))

    print("\n=========== Cast spell ===========")
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Echo", 6))

    print("\n=========== Testing retry ===========")

    @retry_spell(11)
    def waterball():
        if random.randint(0, 9) == 9:
            return "Success : waterball cast!"
        else:
            raise ValueError("not the good one")
    print(waterball())
