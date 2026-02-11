def validate_ingredients(ingredients: str) -> str:
    elements: list[str] = ["fire", "water", "earth", "air"]
    if all(element not in ingredients.lower() for element in elements):
        return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
