from dashboard.db.supabase_client import supabase
from dotenv import load_dotenv

load_dotenv()

def main():
    result = supabase.table("firms").select("*").limit(1).execute()
    print(result.data)

if __name__ == "__main__":
    main()