
def main() -> None:
    filename = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    data_to_save = (
        "[ENTRY 001] New quantum algorithm discovered\n"
        "[ENTRY 002] Efficiency increased by 347%\n"
        "[ENTRY 003] Archived by Data Archivist trainee\n"
    )
    try:
        print("\nInitializing new storage unit: new_discovery.txt")
        f = open(filename, 'w', encoding="utf-8")
        print("Storage unit created successfully...\n\n"
              "Inscribing preservation data...")
        f.write(data_to_save)
        print(data_to_save)
        print("Data inscription complete. Storage unit sealed.\n")
        print(f"Archive {filename} ready for long-term preservation.\n")
        f.close()
    except IOError:
        print(f"Could not write in file: {filename}")


if __name__ == "__main__":
    main()
