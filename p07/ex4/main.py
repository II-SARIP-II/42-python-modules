from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===")
    tournament = TournamentPlatform()
    print("\nRegistering Tournament Cards...\n")
    drg = TournamentCard("Fire Dragon", 8, "Rare", 12, 4, 6, "dragon_001")
    wiz = TournamentCard("Wizard", 8, "Rare", 5, 4, 6, "wizard_001")
    print(tournament.register_card(wiz))
    print(tournament.register_card(drg))
    print("Creating tournament match...")
    print(tournament.create_match("dragon_001", "wizard_001"))
    print("\nTournament Leaderboard:")
    lead: list = tournament.get_leaderboard()
    for p in lead:
        print(p)
    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
