from config.supabase_client import supabase_client

def ingest_firms():
    data = [
        {"id": "AH", "name": "Andreesen Horowitz", "website":"https://a16z.com/", "linkedin":"https://www.linkedin.com/company/a16z/", "city":"Menlo Park, CA"},
        {"id": "KV", "name": "Kholsa Ventures", "website":"https://www.khoslaventures.com/", "linkedin":"https://www.linkedin.com/company/khosla-ventures/", "city":"Menlo Park, CA"},
        {"id": "AC", "name": "Accel", "website":"https://www.accel.com/", "linkedin":"https://www.linkedin.com/company/accel-vc/", "city":"Palo Alto, CA"},
        {"id": "SQ", "name": "Sequoia Capital", "website":"https://sequoiacap.com/", "linkedin":"https://www.linkedin.com/company/sequoia/", "city":"Menlo Park, CA"},
        {"id": "VR", "name": "Venrock", "website":"https://www.venrock.com/", "linkedin":"https://www.linkedin.com/company/venrock/", "city":"Palo Alto, CA"},
        {"id": "SVA", "name": "SV Angel", "website":"https://svangel.com/", "linkedin":"https://www.linkedin.com/company/sv-angel/", "city":"San Francisco, CA"},
        {"id": "FRC", "name": "First Round Capital", "website":"https://www.firstround.com/", "linkedin":"https://www.linkedin.com/company/first-round-capital/", "city":"San Francisco, CA"},
        {"id": "NEA", "name": "New Enterprise Associates", "website":"https://www.nea.com/", "linkedin":"https://www.linkedin.com/company/new-enterprise-associates/", "city":"Menlo Park, CA"},
        {"id": "FF", "name": "Founders Fund", "website":"https://foundersfund.com/", "linkedin":"https://www.linkedin.com/company/the-founders-fund/", "city":"San Francisco, CA"},
        {"id": "HOF", "name": "HOF Capital", "website":"https://hofcapital.com/", "linkedin":"https://www.linkedin.com/company/hof-capital/", "city":"New York, NY"}
    ]