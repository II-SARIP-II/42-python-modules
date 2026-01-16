def get_price(object: str, items: dict, number: int):
    if object in items:
        return (items[object][0]*number)
    print(f"{object} is not in objects dict()")


def get_category(object: str, items: dict):
    if object in items:
        return (items[object][1])
    print(f"{object} is not in objects dict()")


def get_rarity(object: str, items: dict):
    if object in items:
        return (items[object][2])
    print(f"{object} is not in objects dict()")


def print_inventory(player: str, items: dict, players: dict):
    if player in players:
        inventory = []
        inventory = players[player]
        print(f"\n=== {player}'s Inventory ===")
        for i in inventory:
            print(f"{i} ({get_category(i, items)}, {get_rarity(i, items)}): "
                  f"{inventory[i]}x @ {get_price(i, items, 1)} gold each = "
                  f"{get_price(i, items, inventory[i])} gold")
    else:
        print("This player do not exist")


def get_inventory_value(player: str, items: dict, players: dict):
    if player in players:
        inventory = []
        inventory = players[player]
        sum = 0
        for i in inventory:
            sum += get_price(i, items, inventory[i])
        return sum
    else:
        print("This player do not exist")


def get_items_number(player: str, players: dict):
    if player in players:
        inventory = players[player]
        total_items = sum(inventory.values())
        return f"Item count: {total_items} items"
    else:
        print("This player does not exist")


def get_items_categories(player: str, items: dict, players: dict):
    if player in players:
        inventory = players[player]
        categories_list = []
        for item_name, count in inventory.items():
            cat = get_category(item_name, items)
            categories_list.append(f"{cat}({count})")
        print("Categories: " + ", ".join(categories_list))
    else:
        print("This player does not exist")


def add_item_to_inventory(player: str, players: dict, add_item: str,
                          count_to_add: int):
    if player in players:
        inventory = players[player]
        if add_item in inventory:
            inventory[add_item] += count_to_add
        else:
            inventory.update({add_item: count_to_add})
    else:
        print("This player does not exist")


def remove_item_to_inventory(player: str, players: dict, item_name: str,
                             count_to_remove: int):
    if player in players:
        inventory = players[player]
        if item_name in inventory:
            inventory[item_name] -= count_to_remove
            if inventory[item_name] <= 0:
                del inventory[item_name]
        else:
            print(f"Cannot remove {item_name} from {player}")
    else:
        print("This player does not exist")


def exchange(p_buyer: str, p_giver: str, players: dict, item_name: str,
             item_nb: int):
    try:
        remove_item_to_inventory(p_giver, players, item_name, item_nb)
        add_item_to_inventory(p_buyer, players, item_name, item_nb)
        print(f"\n=== Transaction: {p_giver} gives {p_buyer} {item_nb} "
              f"{item_name}{'s' if item_nb > 1 else ''} ===")
        print("Transaction successful!")
        print("\n=== Updated Inventories ===")
        if item_name in players[p_giver]:
            print(f"{p_giver} {item_name}{'s' if item_nb > 1 else ''}"
                  f" {players[p_giver][item_name]}")
        else:
            print(f"No more {item_name} in {p_giver}'s inventory")
        print(f"{p_buyer} {item_name}{'s' if item_nb > 1 else ''}"
              f" {players[p_buyer][item_name]}")
    except ValueError as e:
        print(f"Value Error details: {e}")


def get_all_price(players: dict, items: dict):
    players_value = {}
    for player in players:
        count = 0
        for item in players[player]:
            count = get_price(item, items, players[player][item])
        players_value.update({player: count})
    return (players_value)


def get_richest(players: dict, items: dict):
    players_value = get_all_price(players, items)
    richest = max(players_value, key=players_value.get)
    return richest


def get_fullest(players: dict):
    counts = {name: get_items_number(name, players) for name in players}
    fullest_player = max(counts, key=counts.get)
    return (f"Most items: {fullest_player} "
            f"({counts[fullest_player]} items)")


def get_rarest(items: dict):
    item_tab = []
    for i in items:
        if get_rarity(i, items) == "rare" or get_rarity(i, items) == "unique":
            item_tab.append(i)
    return ("Rarest items: " + ', '.join(item_tab))


if __name__ == "__main__":
    items = {
        "sword": [500, "weapon", "rare"],
        "potion": [50, "consumable", "common"],
        "shield": [200, "armor", "uncommon"],
        "dragon eye": [3000, "talisman", "unique"],
        "magic_ring": [1500, "weapon", "rare"]
    }
    players = {
        "Alice": {"sword": 1, "potion": 5, "shield": 1},
        "Bob": {"dragon eye": 2},
    }
    print("=== Player Inventory System ===")
    print_inventory("Alice", items, players)
    print("")
    print(f"Inventory value: {get_inventory_value('Alice', items, players)}"
          " gold")
    print(get_items_number("Alice", players))
    get_items_categories("Alice", items, players)
    exchange("Bob", "Alice", players, "potion", 2)
    print("\n=== Inventory Analytics ===")
    print(f"Most valuable player: {get_richest(players, items)} ("
          f"{get_inventory_value(get_richest(players, items), items, players)}"
          f" gold)")
    print(get_fullest(players))
    print(get_rarest(items))
