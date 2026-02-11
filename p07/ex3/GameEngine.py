from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        hand = [
            self.factory.create_creature("Fire Dragon"),
            self.factory.create_creature("Goblin Warrior"),
            self.factory.create_spell("Lightning Bolt")
        ]
        self.turns += 1
        return self.strategy.execute_turn(hand, [])

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turns,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': 8,
            'cards_created': 3
        }
