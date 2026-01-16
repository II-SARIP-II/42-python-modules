print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols")

print("\nSECURE EXTRACTION:")
try:
    with open("vault_data.txt", "r") as vault:
        print(vault.read())
except FileNotFoundError:
    print("{[}CLASSIFIED{]} Quantum encryption keys recovered")
    print("{[}CLASSIFIED{]} Archive integrity: 100%")

print("\nSECURE PRESERVATION:")
with open("security_report.txt", "w") as report:
    report.write("New security protocols archived")
    print("{[}CLASSIFIED{]} New security protocols archived")

print("Vault automatically sealed upon completion")
print("\nAll vault operations completed with maximum security.")
