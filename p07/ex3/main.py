from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():
    print("=== DataDeck Game Engine ===\n")
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine.configure_engine(factory, strategy)
    print("Configuring Fantasy Card Game...")
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    print("Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]")
    turn_results = engine.simulate_turn()
    print(f"\nTurn execution:\nStrategy: {turn_results['strategy']}\n"
          f"Actions: {turn_results['actions']}")

    print("\nGame Report:")
    print(engine.get_engine_status())
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved")


if __name__ == "__main__":
    main()
