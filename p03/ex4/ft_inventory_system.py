import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    """Parses command-line arguments into an inventory dictionary."""
    inventory: dict[str, int] = {}
    for arg in args:
        try:
            name, count = arg.split(":")
            inventory[name] = int(count)
        except ValueError:
            print(f"Warning: Skipping invalid format '{arg}'")
    return inventory


def analyze_inventory(inv: dict[str, int]) -> None:
    """Performs advanced analytics on the inventory collection."""
    try:
        if not inv:
            print("Inventory is empty!")
            return
        total_items: int = sum(inv.values())
        unique_types: int = len(inv)
        print("=== Inventory System Analysis ===")
        print(f"Total items in inventory: {total_items}")
        print(f"Unique item types: {unique_types}")
        print("\n=== Current Inventory ===")
        sort_inv = dict(sorted(inv.items(), key=lambda x: x[1], reverse=True))

        for item, count in sort_inv.items():
            percentage: float = (count / total_items) * 100
            print(f"{item}: {count} units ({percentage:.1f}%)")

        most_item: str = max(inv, key=lambda k: inv[k])
        least_item: str = min(inv, key=lambda k: inv[k])

        print("\n=== Inventory Statistics ===")
        print(f"Most abundant: {most_item} ({inv[most_item]} units)")
        print(f"Least abundant: {least_item} ({inv[least_item]} units)")

        moderate = {k: v for k, v in inv.items() if v >= 5}
        scarce = {k: v for k, v in inv.items() if v < 5}

        print("\n=== Item Categories ===")
        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}")

        try:
            print("\n=== Management Suggestions ===")
            restock: list = [item for item, count in inv.items() if count < 2]
            print(f"Restock needed: {restock}")
        except Exception as e:
            print(f"Error generating suggestions: {e}")

        print("\n=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {list(inv.keys())}")
        print(f"Dictionary values: {list(inv.values())}")
        print(f"Sample lookup - 'sword' in inventory: {'sword' in inv}")

    except Exception as e:
        print(f"An error occurred during analysis: {e}")


def main() -> None:
    """Entry point for the inventory quest."""
    user_loot = sys.argv[1:]

    if not user_loot:
        print("Usage: python3 ft_inventory_system.py item:nb item:nb ...")
        user_loot = ["sword:1", "potion:5", "shield:2", "armor:3", "helmet:1"]

    inventory_data = parse_inventory(user_loot)
    analyze_inventory(inventory_data)


if __name__ == "__main__":
    main()
