from ex0.Card import Card


class AggressiveStrategy:
    def execute_turn(self, hand: list[Card], battlefield: list[Card]) -> dict:
        playable_cards = sorted(hand, key=lambda c: c.cost)
        played = [c for c in playable_cards[:2]]
        mana = sum(c.cost for c in playable_cards[:2])
        mana = 0
        played_name = []
        for card in played:
            mana += card.cost
            hand.remove(card)
            battlefield.append(card)
            played_name.append(card.name)
        return {
            'strategy': self.get_strategy_name(),
            'actions': {
                'cards_played': played_name,
                'mana_used': mana,
                'targets_attacked': self.prioritize_targets(battlefield),
                'damage_dealt': 6
            }
        }

    def get_strategy_name(self) -> str:
        return "AgressiveStrategy"

    def prioritize_targets(self, available_targets: list[Card]) -> list:
        targets = sorted(available_targets, key=lambda c: c.cost)
        targets_name = []
        for card in targets:
            targets_name.append(card.name)
        return targets_name
