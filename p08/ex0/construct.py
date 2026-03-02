import sys


def main() -> None:
    try:
        current = sys.executable
        base = sys.prefix
        env = base.replace("\\", "/").split("/")
        if sys.base_prefix == sys.prefix:
            print("MATRIX STATUS: You're still plugged in\n")
            print("Current Python:", current)
            print("Virtual Environment: None detected\n")
            print("WARNING: You're in the global environment!\n"
                  "The machines can see everything you install.\n"
                  "\nTo enter the construct, run:\n"
                  "python -m venv matrix_env\n"
                  "source matrix_env/bin/activate # On Unix\n"
                  "matrix_env\n"
                  "Scripts\n"
                  "activate     # on Windows\n")
        else:
            print("MATRIX STATUS: Welcome to the construct\n")
            print("Current Python:", current)
            print("Virtual Environment", env[-1])
            print("Environment Path:", base)
            print("\nSUCCESS: You're in an isolated environment!"
                  "Safe to install packages without affecting "
                  "the global system\n")
            print("Package installation path:")
            site_path = [p for p in sys.path if "site-packages" in p]
            if site_path:
                print(site_path[0])
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
