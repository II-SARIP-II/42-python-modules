def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def basic_damage() -> int:
    return 10


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined_spell(*args, **kwargs):
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return (res1, res2)
    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified_spell(*args, **kwargs):
        result = base_spell(*args, **kwargs)
        return result * multiplier
    return amplified_spell


def conditional_caster(condition: callable, spell: callable) -> callable:
    def check_and_cast(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return check_and_cast


def spell_sequence(spells: list[callable]) -> callable:
    def cast_spells(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return cast_spells


def is_dragon(target: str) -> bool:
    return target == "Dragon"


if __name__ == "__main__":
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    # =================== COMBINER =================== #
    try:
        print("Testing spell combiner...")
        combined = spell_combiner(fireball, heal)
        res1, res2 = combined(test_targets[0])
        print(f"Combined spell result: {res1}, {res2}")
    except Exception as e:
        print(f"An error occured during your spells combination: {e}")
    # =================== AMPLIFIER =================== #
    try:
        print("\nTesting power amplifier...")
        mega_hit = power_amplifier(basic_damage, 3)
        original = basic_damage()
        amplified = mega_hit()
        print(f"Original: {original}, Amplified: {amplified}")
    except Exception as e:
        print(f"An error occured during your power amplifier: {e}")

    # =================== CONDITION =================== #
    try:
        print("\nTesting conditional caster...")
        dragon_only_fireball = conditional_caster(is_dragon, fireball)
        print(f"Casting on Dragon: {dragon_only_fireball('Dragon')}")
        print(f"Casting on Goblin: {dragon_only_fireball('Goblin')}")
    except Exception as e:
        print(f"An error occured during your conditional caster: {e}")

    # =================== SEQUENCE =================== #
    try:
        print("\nTesting spell sequence...")
        macro = spell_sequence([fireball, heal, fireball])
        results = macro("Wizard")
        print(f"Sequence results: {results}")
    except Exception as e:
        print(f"An error occured during your spell sequence: {e}")
