from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 12)
    lightning = SpellCard("Lightning Bolt", 3, "Rare", "damage")
    crystal = ArtifactCard("Mana Crystal", 5, "Common", 5, "+1 health")
    deck = Deck()
    deck.add_card(dragon)
    deck.add_card(lightning)
    deck.add_card(crystal)
    print("Deck stats:", deck.get_deck_stats())
    print("\nDrawing and playing cards:")
    c: Card = deck.draw_card()
    if c.__class__.__name__ == "CreatureCard":
        type = "Creature"
    if c.__class__.__name__ == "SpellCard":
        type = "Spell"
    if c.__class__.__name__ == "ArtifactCard":
        type = "Artifact"
    print(f"\nDrew: {c.name} ({type})")
    print(f"Play result: {c.get_card_info()}")
    c: Card = deck.draw_card()
    if c.__class__.__name__ == "CreatureCard":
        type = "Creature"
    if c.__class__.__name__ == "SpellCard":
        type = "Spell"
    if c.__class__.__name__ == "ArtifactCard":
        type = "Artifact"
    print(f"\nDrew: {c.name} ({type})")
    print(f"Play result: {c.get_card_info()}")
    c: Card = deck.draw_card()
    if c.__class__.__name__ == "CreatureCard":
        type = "Creature"
    if c.__class__.__name__ == "SpellCard":
        type = "Spell"
    if c.__class__.__name__ == "ArtifactCard":
        type = "Artifact"
    print(f"\nDrew: {c.name} ({type})")
    print(f"Play result: {c.get_card_info()}")
    print("\nPolymorphism in action: Same interface, "
          "different card behaviors!")
