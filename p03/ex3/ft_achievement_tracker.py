import sys


def get_rare_achievements(players: dict[str, set[str]]) -> set[str]:
    """
    Identifies achievements held by only one player.

    Args:
        players (dict[str, set[str]]): A mapping of player names to their sets.

    Returns:
        set[str]: Achievements that appear exactly once.
    """
    all_counts: dict[str, int] = {}
    for achievements in players.values():
        for ach in achievements:
            all_counts[ach] = all_counts.get(ach, 0) + 1

    return {ach for ach, count in all_counts.items() if count == 1}


def run_achievement_system() -> None:
    """Main logic for the achievement tracking quest."""
    try:
        alice: set[str] = {'first_kill', 'level_10',
                           'treasure_hunter', 'speed_demon'}
        bob: set[str] = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
        charlie: set[str] = {'level_10', 'treasure_hunter', 'boss_slayer',
                             'speed_demon', 'perfectionist'}

        players: dict[str, set[str]] = {
            "alice": alice,
            "bob": bob,
            "charlie": charlie
        }

        print("=== Achievement Tracker System ===\n")
        for name, achievements in players.items():
            print(f"Player {name} achievements: {achievements}")

        print("\n=== Achievement Analytics ===")
        all_unique = alice | bob | charlie
        print(f"All unique achievements: {all_unique}")
        print(f"Total unique achievements: {len(all_unique)}\n")
        common = alice & bob & charlie
        print(f"Common to all players: {common}")
        rare = get_rare_achievements(players)
        if not rare:
            print("No rare achievements!")
        else:
            print(f"Rare achievements (1 player): {rare}")
        print(f"\nAlice vs Bob common: {alice & bob}")
        print(f"Alice unique: {alice - bob}")
        print(f"Bob unique: {bob - alice}")

    except Exception as e:
        print(f"An error occurred in the achievement system: {e}",
              file=sys.stderr)


def main() -> None:
    """Entry point."""
    run_achievement_system()


if __name__ == "__main__":
    main()
