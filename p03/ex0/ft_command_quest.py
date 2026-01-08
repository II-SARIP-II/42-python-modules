import sys

if __name__ == "__main__":
    print("=== Command Quest ===\n")
    i = 0
    while i < len(sys.argv):
        if i == 0:
            if len(sys.argv) > 1:
                print("Program name: ", end="")
                print(sys.argv[i])
                print(f"Arguments received: {len(sys.argv) - 1}")
            else:
                print("No arguments provided!")
                print("Program name: ", end="")
                print(sys.argv[i])
        else:
            print(f"Argument {i}: ", end="")
            print(sys.argv[i])
        i += 1
    print(f"Total arguments: {len(sys.argv)}")
