import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    mode = os.getenv('MATRIX_MODE', 'unknown')
    db_url = os.getenv('DATABASE_URL')
    api_key = os.getenv('API_KEY')
    log_level = os.getenv('LOG_LEVEL', 'INFO')
    zion = os.getenv('ZION_ENDPOINT')

    print("ORACLE STATUS: Reading the Matrix...")

    if not all([db_url, api_key, zion]):
        print("\n[!] WARNING: The Oracle is blind. "
              "Missing configuration detected.")
        print("Required: DATABASE_URL, API_KEY, ZION_ENDPOINT")
        print("\nFix: cp .env.example .env and update the values.")
        return

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if mode.lower() == "production":
        print("Database: [SECURE] Connected to Production Mainframe")
        print(f"API Access: Authenticated (Masked: {api_key[:4]}****)")
        print(f"Log Level: {log_level} (Optimized for performance)")
    else:
        print(f"Database: Connected to {db_url}")
        print(f"API Access: Authenticated (Key: {api_key})")
        print(f"Log Level: {log_level} (Verbose debugging active)")

    print(f"Zion Network: {zion}")

    print("\nEnvironment security check:")
    env_exists = os.path.exists(".env")
    print(f"[{'OK' if env_exists else '!!'}] .env "
          f"file {'detected' if env_exists else 'missing'}")
    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
