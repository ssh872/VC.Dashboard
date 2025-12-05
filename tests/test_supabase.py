from supabase_client import supabase

def main():
    data = supabase.table("firms").select("*").limit(1).execute()
    print(data)

if __name__ == "__main__":
    main()