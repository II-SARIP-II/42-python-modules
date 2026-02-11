from ex0.CreatureCard import CreatureCard


def game() -> None:
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 15)
    goblin = CreatureCard("Goblin Warrior", 1, "Basic", 2, 6)

    print("CreatureCard Info:\n", dragon.get_card_info())
    print("\nPlaying Fire Dragon with 6 mana available:")
    mana: int = 6
    print("Playable", dragon.is_playable(mana))
    mana -= dragon.cost
    print("Play result:",
          dragon.play(dragon.get_card_info()))

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", dragon.attack_target(goblin))

    print("\nTesting insufficient mana (3 available):")
    print("Playable:", dragon.is_playable(mana))


if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===")
    game()
    print("\nAbstract pattern successfully demonstrated!")
