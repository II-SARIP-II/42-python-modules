def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients as val
    validated: str = val(ingredients)
    if "INVALID" in validated:
        return f"Spell rejected: {spell_name} ({validated})"
    return f"Spell recorded: {spell_name} ({validated})"
