import sys
import math


def get_distance(p1: tuple, p2: tuple) -> float:
    try:
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    except Exception as e:
        print(f"Distance calculation error: {e}")
        return 0.0


def str_to_tuple(s: str) -> tuple:
    tp1 = s.split(",", 2)
    tab = []
    if len(tp1) != 3:
        raise ValueError("Expected 3 coordinates")
    i = 0
    while i < 3:
        tab.append(int(tp1[i]))
        i += 1
    return tuple(tab)


def run_quest(coordinate_string: str) -> None:
    """Executes the coordinate system demonstration."""
    print("=== Game Coordinate System ===")

    spawn_point: tuple[int, int, int] = (10, 20, 5)
    origin: tuple[int, int, int] = (0, 0, 0)

    print(f"Position created: {spawn_point}")
    dist = get_distance(spawn_point, origin)
    print(f"Distance between {origin}->{spawn_point}: {dist:.2f}\n")

    print(f"Parsing coordinates: \"{coordinate_string}\"")
    try:
        parsed_pos = str_to_tuple(coordinate_string)
        print(f"Parsed position: {parsed_pos}")

        dist_parsed = get_distance(parsed_pos, origin)
        print(f"Distance between {origin}->{parsed_pos}: {dist_parsed:.1f}\n")
        x, y, z = parsed_pos
        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


def main() -> None:
    """Main entry point."""
    if len(sys.argv) < 2:
        run_quest("3,4,0")
    else:
        run_quest(sys.argv[1])


if __name__ == "__main__":
    main()
