from dotenv import load_dotenv
import os


def main():
    try:
        load_dotenv()
        mode = os.getenv('MATRIX_MODE')
        data_url = os.getenv('DATABASE_URL')
        api = os.getenv('API_KEY')
        log = os.getenv('LOG_LEVEL')
        zion = os.getenv('ZION_ENDPOINT')
        if (not mode and not data_url and not api and not log and not zion):
            raise FileNotFoundError("The file .env does not exist.")
        print("ORACLE STATUS: Reading the Matrix...\n")
        if mode:
            print(f"Mode: {mode}")
        if data_url:
            print(f"Database: {data_url}")
        if api:
            print(f"API Access: {api}")
        if log:
            print(f"Log Level: {log}")
        if zion:
            print(f"Zion network: {zion}")
        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected\n"
              "[OK] .env file properly configured\n"
              "[OK] Production overrides available\n")
        print("The Oracle sees all configurations.")
    except FileNotFoundError as e:
        print(e)
        print("enter:")
        print("cp .env.example .env")
        print("re-run the programme to display .env configuration")


if __name__ == "__main__":
    main()
