def main() -> None:
    filename = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {filename}")
    print("Connection established...")
    print("\nRECOVERED DATA:")
    try:
        f = open(filename, "r")
        print(f.read())
        f.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except IOError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
