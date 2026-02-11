import sys


def analyze_scores(raw_args: list[str]) -> None:
    """
    Processes command-line arguments into scores and displays analytics.

    Args:
        raw_args (list[str]): The list of command-line arguments.
    """
    print("=== Player Score Analytics ===\n")

    if len(raw_args) <= 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    scores: list[int] = []
    for arg in raw_args[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Warning: '{arg}' is not a valid score and was skipped.")
    if not scores:
        print("Error: No valid numerical scores were processed.")
        return

    try:
        total_players: int = len(scores)
        total_score: int = sum(scores)
        avg_score: float = total_score / total_players
        high_score: int = max(scores)
        low_score: int = min(scores)

        print(f"Scores processed: {scores}")
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {avg_score:.1f}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {high_score - low_score}")

    except Exception as e:
        print(f"A calculation error occurred: {e}")


def main() -> None:
    """Entry point for the analytics quest."""
    analyze_scores(sys.argv)


if __name__ == "__main__":
    main()
