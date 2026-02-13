def crisis_handler(filename: str) -> None:
    try:
        with open(filename, 'r') as vault:
            content = vault.read()
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            print(f"SUCCESS: Archive recovered - {content}", end="")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception as e:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print(f"RESPONSE: Unexpected system anomaly: {e}")
        print("STATUS: Crisis handled, system stable\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")
