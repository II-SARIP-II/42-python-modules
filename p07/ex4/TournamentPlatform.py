from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: list[TournamentCard] = []
        self.matches = 0

    def register_card(self, card: TournamentCard) -> str:
        infos = card.get_rank_info()
        self.cards.append(card)
        return (f"{card.name} ({card.name})\n"
                " - Interfaces: [Card, Combatable, Rankable]\n"
                f" - Rating: {infos['rating']}\n"
                f" - Record: {infos['wins']}-{infos['losses']}\n")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        for c in self.cards:
            if c.id is card1_id:
                card1 = c
            if c.id is card2_id:
                card2 = c
        c1_score = card1.attack_value + card1.defence + card1.health
        c2_score = card2.attack_value + card2.defence + card2.health
        self.matches += 1
        if c1_score > c2_score:
            card1.update_wins(1)
            card2.update_losses(1)
            return {
                'winner': card1_id,
                'loser': card2_id,
                'winner_rating': card1.get_rank_info()['rating'],
                'loser_rating': card2.get_rank_info()['rating']
            }
        elif c2_score > c1_score:
            card2.update_wins(1)
            card1.update_losses(1)
            return {
                'winner': card2_id,
                'loser': card1_id,
                'winner_rating': card2.get_rank_info()['rating'],
                'loser_rating': card1.get_rank_info()['rating']
            }
        else:
            return {
                "equal": True
            }

    def get_leaderboard(self) -> list:
        playable_cards: list[TournamentCard] = sorted(
            self.cards,
            key=lambda c: c.get_rank_info()['rating'],
            reverse=True
        )
        leaderboard: list[str] = []
        for i, card in enumerate(playable_cards, start=1):
            info = card.get_rank_info()
            line: str = (
                f"{i}. {card.name} - Rating: "
                f"{info['rating']} "
                f"({info['wins']}-{info['losses']})"
            )
            leaderboard.append(line)
        return leaderboard

    def generate_tournament_report(self) -> dict:
        sum = 0
        for c in self.cards:
            sum += c.get_rank_info()['rating']
        return {
            'total_cards': len(self.cards),
            'matches_played': self.matches,
            'avg_rating': sum/len(self.cards),
            'platform_status': 'active'
        }
