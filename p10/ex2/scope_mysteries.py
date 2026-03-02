from typing import Any


def mage_counter() -> callable:
    c = 0

    def count():
        nonlocal c
        c += 1
        return c
    return count


def spell_accumulator(initial_power=0) -> callable:
    total_power = initial_power

    def accumulator(amount: int):
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def echantment(item: str):
        return f"{enchantment_type} {item}"
    return echantment


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key: Any, value: Any):
        vault[key] = value

    def recall(key: Any):
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    initial_powers = [38, 38, 77]
    enchantment_types = ['Dark', 'Flaming', 'Windy']
    items_to_enchant = ['Staff', 'Wand', 'Cloak', 'Ring']

    # ======================= count ======================= #
    my_counter = mage_counter()
    print(f"Mage call 1: {my_counter()}")
    print(f"Mage call 2: {my_counter()}")
    print(f"Mage call 3: {my_counter()}")

    # ======================= accumulator ======================= #
    accumulation = spell_accumulator(initial_powers[0])
    print("Spell accumulation 1:", accumulation(0))
    print("Spell accumulation 1:", accumulation(initial_powers[1]))
    print("Spell accumulation 2:", accumulation(initial_powers[1]))

    # ======================= echantment ======================= #
    factory = enchantment_factory(enchantment_types[1])
    print("Sword enchanted:", factory(items_to_enchant[3]))
    factory = enchantment_factory(enchantment_types[0])
    print("Sword enchanted:", factory(items_to_enchant[1]))

    # ======================= memory_vault ======================= #
    memory = memory_vault()
    print("Memory vault:", memory["store"]("echo", "echoooo"))
    print("Memory vault:", memory["recall"]("echo"))
    print("Memory vault:", memory["recall"]("echa"))
