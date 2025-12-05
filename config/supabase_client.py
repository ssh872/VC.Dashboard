import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL: str = os.getenv("https://hipaaeyvcizhjsttfquu.supabase.co")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhpcGFhZXl2Y2l6aGpzdHRmcXV1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ5MDQzNDMsImV4cCI6MjA4MDQ4MDM0M30.ok7PtBJW6tNExjSi5ffgxyCnHchQmnZriE0qCsRQ3zg")

if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
    raise ValueError("Supabase URL or Service Role Key is not set in environment variables.")

supabase_client: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)