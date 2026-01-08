import sys
import math


def get_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def str_to_tuple(s: str):
    tp1 = s.split(",", 2)
    tab = []
    if len(tp1) != 3:
        raise ValueError("Expected 3 coordinates")
    i = 0
    while i < 3:
        tab.append(int(tp1[i]))
        i += 1
    return tuple(tab)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 ft_coordinate_system.py x,y,z")
        sys.exit(1)
    else:
        pos = (10, 20, 5)
        ref = (0, 0, 0)
        print("=== Game Coordinate System ===\n")
        print(f"Position created: {pos}")
        print(f"Distance between (0, 0, 0) and {pos}:", end=" ")
        print("{:.2f}\n".format(get_distance(pos, ref)))
        print(f"Parsing coordinates: \"{sys.argv[1]}\"")
    try:
        tp = str_to_tuple(sys.argv[1])
        print(f"Parsed position: {tp}")
        print(f"Distance between (0, 0, 0) and {tp}:", end=" ")
        print("{:.2f}\n".format(get_distance(tp, ref)))
        x, y, z = tp
        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
