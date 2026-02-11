import sys


def process_commands(args: list[str]) -> None:
    """
    Processes and displays command-line arguments.

    Args:
        args (list[str]): The list of command-line arguments (sys.argv).
    """
    try:
        print("=== Command Quest ===")
        arg_count: int = len(args)
        if arg_count == 1:
            print("No arguments provided!")
            print(f"Program name: {args[0]}")
            print(f"Total arguments: {arg_count}")
            return
        print(f"Program name: {args[0]}")
        print(f"Arguments received: {arg_count - 1}")

        for index, value in enumerate(args[1:], start=1):
            print(f"Argument {index}: {value}")
        print(f"Total arguments: {arg_count}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


def main() -> None:
    """Entry point of the script."""
    process_commands(sys.argv)


if __name__ == "__main__":
    main()
