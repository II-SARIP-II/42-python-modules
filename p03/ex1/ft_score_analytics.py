import sys

if __name__ == "__main__":
    tab: list[int] = []
    print("=== Player Score Analytics ===\n")
    i = 1
    if len(sys.argv) <= 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              "<score1> <score2> ...")
    else:
        while i < len(sys.argv):
            try:
                x = int(sys.argv[i])
                tab.append(x)
                i += 1
            except ValueError:
                print("Not a Number")
                i += 1
        print(f"Scores processed: {tab}")
        print(f"Total players: {len(tab)}")
        print(f"Total score: {sum(tab)}")
        print(f"Average score: {sum(tab)/len(tab)}")
        print(f"High score: {max(tab)}")
        print(f"Low score: {min(tab)}")
        print(f"Score range: {max(tab) - min(tab)}")
