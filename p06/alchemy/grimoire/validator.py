def validate_ingredients(ingredients: str) -> str:
    elements: list[str] = ["fire", "water", "earth", "air"]
    if any(element in ingredients.lower() for element in elements):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
