import alchemy
from typing import Callable

func = ["create_fire", "create_water",
        "create_earth", "create_air"]

print("\n=== Sacred Scroll Mastery ===\n")

for f in func:
    try:
        todo: Callable[[], str] = getattr(alchemy.elements, f)
        print(f"alchemy.elements.{f}(): {todo()}")
    except (NameError, AttributeError):
        print(f"alchemy.elements{f}(): AttributeError - not exposed")

print("\nTesting package-level access (controlled by __init__.py):")

for f in func:
    try:
        todoo: Callable[[], str] = getattr(alchemy, f)
        print(f"alchemy.{f}(): {todoo()}")
    except (NameError, AttributeError):
        print(f"alchemy.{f}(): AttributeError - not exposed")

print("\nPackage metadata:")
print("Version:", alchemy.__version__)
print("Author:", alchemy.__author__)
