if __name__ == "__main__":
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    players = {
        "alice": alice,
        "bob": bob,
        "charlie": charlie
    }
    print("=== Achievement Tracker System ===\n")
    for player in players:
        print(f"Player {player} achievements: {players[player]}")
    print("\n=== Achievement Analytics ===")
    achievement = {'boss_slayer', 'collector', 'first_kill', 'level_10',
                   'perfectionist', 'speed_demon', 'treasure_hunter'}
    print(f"All unique achievements: {achievement}")
    print(f"Total unique achievements: {len(achievement)}\n")
    all_achievements = alice.union(bob, charlie)
    overlap_alice_bob = alice.intersection(bob)
    overlap_alice_charlie = alice.intersection(charlie)
    overlap_bob_charlie = bob.intersection(charlie)
    all_overlaps = overlap_alice_bob.union(overlap_alice_charlie,
                                           overlap_bob_charlie)
    rare_achievements = all_achievements.difference(all_overlaps)
    print(f"Common to all players: {alice.intersection(bob, charlie)}")
    if len(rare_achievements) == 0:
        print("No rare achievement!")
    else:
        print(f"Rare achievements (1 player): {rare_achievements}")
    print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")
