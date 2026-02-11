import sys
from typing import Any


def run_analytics(data: dict[str, Any]) -> None:
    """
    Processes gaming data using list, dict, and set comprehensions.

    Args:
        data (dict[str, Any]): The raw game event data.
    """
    try:
        players = data.get('players', {})
        sessions = data.get('sessions', [])
        ach_list = data.get('achievements', [])

        print("=== Game Analytics Dashboard ===\n")

# ======================= List comprehension ======================= #
        high_scorers: list[str] = [
            name for name, info in players.items()
            if info.get('total_score', 0) > 2000
        ]
        doubled_scores: list[int] = [
            info.get('total_score', 0) * 2 for info in players.values()
        ]

        active_players: list[str] = sorted(list({
            s['player'] for s in sessions if not s.get('completed', False)
        }))

        print("=== List Comprehension Examples ===")
        print(f"High scorers (>2000): {high_scorers}")
        print(f"Scores doubled: {doubled_scores}")
        print(f"Active players: {active_players}")

# ======================= Dict comprehension ======================= #
        ps: dict[str, int] = {
            n: p.get('total_score', 0) for n, p in players.items()
        }

        categories: dict[str, int] = {
            'high': sum(1 for s in ps.values() if s >= 5000),
            'medium': sum(1 for s in ps.values() if 2000 <= s < 5000),
            'low': sum(1 for s in ps.values() if s < 2000)
        }

        ach_counts: dict[str, int] = {
            n: p.get('achievements_count', 0) for n, p in players.items()
        }

        print("\n=== Dict Comprehension Examples ===")
        print(f"Player scores: {ps}")
        print(f"Score categories: {categories}")
        print(f"Achievement counts: {ach_counts}")

# ======================= Set comprehension ======================= #
        unique_players: set[str] = {name for name in players}
        unique_achievements: set[str] = {ach for ach in ach_list}
        active_modes: set[str] = {s.get('mode', 'unknown') for s in sessions}

        print("\n=== Set Comprehension Examples ===")
        print(f"Unique players: {unique_players}")
        print(f"Unique achievements: {unique_achievements}")
        print(f"Active modes: {active_modes}")

        if ps:
            all_vals = list(ps.values())
            avg_score = sum(all_vals) / len(all_vals)
            top_p = max(ps, key=lambda k: ps[k])

            print("\n=== Combined Analysis ===")
            print(f"Total players: {len(unique_players)}")
            print(f"Total unique achievements: {len(unique_achievements)}")
            print(f"Average score: {avg_score:.1f}")
            print(f"Top performer: {top_p} ({ps[top_p]} points, "
                  f"{ach_counts.get(top_p, 0)} achievements)")

    except Exception as e:
        print(f"Analytics failure: {e}", file=sys.stderr)


def main() -> None:
    """Entry point for the Final Boss quest."""
    events = [
        {
            'players': {
                'alice': {
                    'level': 41, 'total_score': 2824, 'sessions_played': 13,
                    'favorite_mode': 'ranked', 'achievements_count': 5
                },
                'bob': {
                    'level': 16, 'total_score': 4657, 'sessions_played': 27,
                    'favorite_mode': 'ranked', 'achievements_count': 2
                },
                'charlie': {
                    'level': 44, 'total_score': 9935, 'sessions_played': 21,
                    'favorite_mode': 'ranked', 'achievements_count': 7
                },
                'diana': {
                    'level': 3, 'total_score': 1488, 'sessions_played': 21,
                    'favorite_mode': 'casual', 'achievements_count': 4
                },
                'eve': {
                    'level': 33, 'total_score': 1434, 'sessions_played': 81,
                    'favorite_mode': 'casual', 'achievements_count': 7
                },
                'frank': {
                    'level': 15, 'total_score': 8359, 'sessions_played': 85,
                    'favorite_mode': 'competitive', 'achievements_count': 1
                }
            },
            'sessions': [
                {'player': 'bob', 'duration_minutes': 94, 'score': 1831,
                 'mode': 'competitive', 'completed': False},
                {'player': 'bob', 'duration_minutes': 32, 'score': 1478,
                 'mode': 'casual', 'completed': True},
                {'player': 'diana', 'duration_minutes': 17, 'score': 1570,
                 'mode': 'competitive', 'completed': False},
                {'player': 'alice', 'duration_minutes': 98, 'score': 1981,
                 'mode': 'ranked', 'completed': True},
                {'player': 'diana', 'duration_minutes': 15, 'score': 2361,
                 'mode': 'competitive', 'completed': False},
                {'player': 'eve', 'duration_minutes': 29, 'score': 2985,
                 'mode': 'casual', 'completed': True},
                {'player': 'frank', 'duration_minutes': 34, 'score': 1285,
                 'mode': 'casual', 'completed': True},
                {'player': 'alice', 'duration_minutes': 53, 'score': 1238,
                 'mode': 'competitive', 'completed': False},
                {'player': 'bob', 'duration_minutes': 52, 'score': 1555,
                 'mode': 'casual', 'completed': False},
                {'player': 'frank', 'duration_minutes': 92, 'score': 2754,
                 'mode': 'casual', 'completed': True},
                {'player': 'eve', 'duration_minutes': 98, 'score': 1102,
                 'mode': 'casual', 'completed': False},
                {'player': 'diana', 'duration_minutes': 39, 'score': 2721,
                 'mode': 'ranked', 'completed': True},
                {'player': 'frank', 'duration_minutes': 46, 'score': 329,
                 'mode': 'casual', 'completed': True},
                {'player': 'charlie', 'duration_minutes': 56, 'score': 1196,
                 'mode': 'casual', 'completed': True},
                {'player': 'eve', 'duration_minutes': 117, 'score': 1388,
                 'mode': 'casual', 'completed': False},
                {'player': 'diana', 'duration_minutes': 118, 'score': 2733,
                 'mode': 'competitive', 'completed': True},
                {'player': 'charlie', 'duration_minutes': 22, 'score': 1110,
                 'mode': 'ranked', 'completed': False},
                {'player': 'frank', 'duration_minutes': 79, 'score': 1854,
                 'mode': 'ranked', 'completed': False},
                {'player': 'charlie', 'duration_minutes': 33, 'score': 666,
                 'mode': 'ranked', 'completed': False},
                {'player': 'alice', 'duration_minutes': 101, 'score': 292,
                 'mode': 'casual', 'completed': True},
                {'player': 'frank', 'duration_minutes': 25, 'score': 2887,
                 'mode': 'competitive', 'completed': True},
                {'player': 'diana', 'duration_minutes': 53, 'score': 2540,
                 'mode': 'competitive', 'completed': False},
                {'player': 'eve', 'duration_minutes': 115, 'score': 147,
                 'mode': 'ranked', 'completed': True},
                {'player': 'frank', 'duration_minutes': 118, 'score': 2299,
                 'mode': 'competitive', 'completed': False},
                {'player': 'alice', 'duration_minutes': 42, 'score': 1880,
                 'mode': 'casual', 'completed': False},
                {'player': 'alice', 'duration_minutes': 97, 'score': 1178,
                 'mode': 'ranked', 'completed': True},
                {'player': 'eve', 'duration_minutes': 18, 'score': 2661,
                 'mode': 'competitive', 'completed': True},
                {'player': 'bob', 'duration_minutes': 52, 'score': 761,
                 'mode': 'ranked', 'completed': True},
                {'player': 'eve', 'duration_minutes': 46, 'score': 2101,
                 'mode': 'casual', 'completed': True},
                {'player': 'charlie', 'duration_minutes': 117, 'score': 1359,
                 'mode': 'casual', 'completed': True}
            ],
            'game_modes': ['casual', 'competitive', 'ranked'],
            'achievements': [
                'first_blood', 'level_master', 'speed_runner',
                'treasure_seeker', 'boss_hunter', 'pixel_perfect',
                'combo_king', 'explorer'
            ]
        }
    ]
    run_analytics(events[0])


if __name__ == "__main__":
    main()
