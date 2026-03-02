import functools
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in ops:
        raise ValueError(f"Unknown magic: {operation}")

    return functools.reduce(ops[operation], spells)


def base_enchantment(power, element, target):
    return f"Casting {element} (Level {power}) on {target}!"


def partial_enchanter(base_enchantment: callable):
    fire_spell = functools.partial(base_enchantment, 50, "fire")
    ice_spell = functools.partial(base_enchantment, 50, "ice")
    lightning_spell = functools.partial(base_enchantment, 50, "lightning")

    return {
        'fire_enchant': fire_spell,
        'ice_enchant': ice_spell,
        'lightning_enchant': lightning_spell
    }


@functools.lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@functools.singledispatch
def spell_dispatcher(arg: Any):
    """The default behavior if the type isn't recognized."""
    return f"Unknown magic: {arg}"


@spell_dispatcher.register(int)
def _(power: int):
    """Handle damage spells (integers)."""
    return f"Casting Damage Spell: {power} HP reduction!"


@spell_dispatcher.register(str)
def _(name: str):
    """Handle enchantment spells (strings)."""
    return f"Casting Enchantment: {name}!"


@spell_dispatcher.register(list)
def _(spells: list):
    """Handle multi-cast spells (lists)."""
    count = len(spells)
    return f"Casting Multi-Cast: {count} spells triggered at once!"


if __name__ == "__main__":
    spell_powers = [22, 14, 11, 15, 50, 15]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [8, 12, 17]
    print("\n============= fibonacci =============")
    print("Fibonacci(15) :", memoized_fibonacci(15))
    print("Fibonacci(2) :", memoized_fibonacci(2))

    print("\n============= spell reducer =============")
    try:
        print("spell reducer :", spell_reducer(spell_powers, operations[0]))
    except Exception as e:
        print(e)

    print("\n============= partial enchanter =============")
    spell_book = partial_enchanter(base_enchantment)
    print(spell_book['fire_enchant']("Orc Warrior"))

    print("\n============= spell_dispacher =============")
    print(spell_dispatcher(100))
    print(spell_dispatcher("Invisibility"))
    print(spell_dispatcher([1, 2, 3]))
