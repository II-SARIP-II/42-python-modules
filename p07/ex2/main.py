from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Ability System ===")

    hero = EliteCard("Arcane Warrior", 5, "Legendary", 20, 5, 3, 4)
    enemy = CreatureCard("Orc", 5, "Basic", 2, 5)
    enemy2 = CreatureCard("Goblin", 5, "Basic", 2, 5)

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {hero.name} (Elite Card):\n")

    print("Combat phase:")
    print(f"Attack result: {hero.attack(enemy)}")
    print(f"Defense result: {hero.defend(5)}")

    print("\nMagic phase:")
    print(f"Spell cast: {hero.cast_spell('Fireball', [enemy, enemy2])}")
    print(f"Mana channel: {hero.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
