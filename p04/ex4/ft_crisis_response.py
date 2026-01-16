def crisis_handler(f):
    pre = "ROUTINE ACCESS" if f == "standard_archive.txt" else "CRISIS ALERT"
    print(f"{pre}: Attempting access to '{f}'...")
    try:
        with open(f, 'r') as vault:
            content = vault.read()
            print(f"SUCCESS: Archive recovered - {content}", end="")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly: {e}")
        print("STATUS: Crisis handled, system stable\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")
