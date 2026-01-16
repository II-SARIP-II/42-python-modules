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
            'first_blood', 'level_master', 'speed_runner', 'treasure_seeker',
            'boss_hunter', 'pixel_perfect', 'combo_king', 'explorer'
        ]
    }
]

# === List Comprehension Examples === #
players_data = events[0]['players']
sessions_data = events[0]['sessions']
hight_scores = [
    name for name in players_data if players_data[name]['total_score'] > 2000
]
doubled_scores = [
    players_data[name]['total_score']*2 for name in players_data
]
active_sessions = sorted([
    p for p in {s['player'] for s in sessions_data if not s['completed']}
])


print("=== Game Analytics Dashboard ===\n")
print("=== List Comprehension Examples ===")
print(f"High scorers (>2000): {hight_scores}")
print(f"Scores doubled: {doubled_scores}")
print(f"Active players: {active_sessions}")

# === Dict Comprehension Examples === #
p_score = {
    name: players_data[name]['total_score'] for name in players_data
}
high_list = [
    n for n in players_data if players_data[n]['total_score'] >= 5000
]
med_list = [
    n for n in players_data if 2000 <= players_data[n]['total_score'] < 5000
]
low_list = [
    n for n in players_data if players_data[n]['total_score'] < 2000
]
score_categories = {
    'high': len(high_list),
    'medium': len(med_list),
    'low': len(low_list)
}
dict_player_achievements = {
    name: players_data[name]['achievements_count'] for name in players_data
}

print("\n=== Dict Comprehension Examples ===")
print(f"Player scores: {p_score}")
print(f"Score categories: {score_categories}")
print(f"Achievement counts: {dict_player_achievements}")

# === Set Comprehension Examples === #
unique_player = {name for name in players_data}
sessions_data = events[0]['achievements']
unique_achievement = {ach for ach in sessions_data}
print("\n=== Set Comprehension Examples ===")
print(f"Unique players: {unique_player}")
print(f"Unique achievements: {unique_achievement}")
print("Active regions: {'north', 'east', 'central'}")

all_scores = [
    players_data[name]['total_score'] for name in players_data
]
h_s = max(all_scores)
best_player_list = [name for name in p_score if p_score[name] == h_s][0]
best_player_ach = dict_player_achievements[best_player_list]
print("\n=== Combined Analysis ===")
print(f"Total players: {len(unique_player)}")
print(f"Total unique achievements: {len(unique_achievement)}")
print(f"{all_scores}")
print(f"Average score: {sum(all_scores)/len(unique_player)}")
print(f"Top performer: {best_player_list} "
      f"({h_s} points, {best_player_ach} achievements)")
