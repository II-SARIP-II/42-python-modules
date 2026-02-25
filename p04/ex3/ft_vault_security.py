
def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("\nSECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as vault:
            print(vault.read())
    except FileNotFoundError:
        print("File not found")

    print("\nSECURE PRESERVATION:")
    try:
        with open("security_report.txt", "w") as report:
            report.write("[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
    except Exception as e:
        print(f"Error occured while writing: {e}")
    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
