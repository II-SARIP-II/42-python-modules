from alchemy.grimoire

print("\n=== Circular Curse Breaking ===\n")

print("Testing ingredient validation:")
print(f"validate_ingredients(\"fire air\"): {val('fire air')}")
print(f"validate_ingredients(\"dragon scales\"): {val('dragon scales')}")

print("\nTesting spell recording with validation:")
print("record_spell(\"Fireball\", \"fire air\"): "
      f"{spell('Fireball', 'fire air')}")
print("record_spell(\"Dark Magic\", \"shadow\"): "
      f"{spell('Dark Magic', 'shadow')}")


print("\nTesting late import technique:")
print(f"record_spell(\"Lightning\", \"air\"): {spell('Lightning', 'air')}")

print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
