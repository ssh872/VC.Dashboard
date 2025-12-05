# vc-ai

Auto-updating dashboard tracking VC firm investments and deal patterns.

VC Investment Tracking Dashboard

WEEK 1 — Foundations + Data Model (Architecture, DB, VC List)

Goal: Establish the project bones: data model, VC list, database, and repo structure.

Deliverables

Project repo initialized (GitHub)

Directory structure:

/ingestion
/transform
/dashboard
/config
/analytics


Database created (Postgres or Supabase)

Core tables created:

raw_vcs

raw_investments

raw_companies

dim_vc

dim_company

fact_investment

ERD diagram added to README

VC tracking list defined (10–20 firms)

Tasks

Draft ERD & architecture diagram

Research 2–3 data sources (Crunchbase API, RSS feeds, VC blog scraping)

Create VC seed list (YAML or CSV)

Set up Postgres instance

Create initial tables

End-of-week demo:

Show the schema, VC list, and data model diagram.

Repo is clean and well-structured.

WEEK 2 — Ingestion Pipeline (APIs + Scrapers)

Goal: Pull real data from external sources into raw_investments.

Deliverables

Working ingestion script:

Fetches investments per VC from API and/or scraping

Logs ingestion events

Inserts data into the raw_* tables

Handles duplicate raw rows via unique ingestion key

Tasks

Build API connector

Build VC website/blog scraper (fallback source)

Normalize ingest outputs to a common schema (VC, company, round, date, amount)

Insert into raw_investments

Add ingestion logs (simple logging file or table)

Run first “full ingest” across your VC list

End-of-week demo:

You can show:

Raw investments appearing in DB

Log output (e.g., “Sequoia: 22 new investments ingested”)

This is where the project feels real—data is flowing.

WEEK 3 — Cleaning, Normalization, & Master Entities

Goal: Convert messy raw data into clean entities.

Deliverables

Company & VC normalization rules

Cleaned tables populated:

dim_company

fact_investment

Deduplication logic (e.g., fuzzy name match, canonical name rules)

Standardized round mapping (Seed → SEED, Series A → A)

Tasks

Normalize VC names → map raw “Sequoia Capital China / Sequoia” to same VC

Normalize company names → remove suffixes, lowercase, domain extraction

Fuzzy matching for duplicate startups

Build a transformation job that:

Maps raw → dim tables

Creates/upserts investments into fact_investment

Add round-type standardization dictionary

Convert values (amounts) into consistent currency units if available

End-of-week demo:

Show the clean tables and how they differ from raw ones

Prove deduplication works with a few before/after examples

WEEK 4 — Enrichment + Metrics Layer (LLM Sector Tagging, Geography)

Goal: Turn clean data into “insights.”

Deliverables

Sector classification job (LLM or rule-based)

Location normalization (city, state, country)

Metrics tables or views:

vc_metrics_monthly

sector_mix_by_vc

co_investor_network

Materialized views or dbt-style SQL models

Tasks

Build company description fetcher (API → description text)

LLM classifier:

Input: description

Output: sector (AI, Bio, Infra, Consumer…)

Normalize locations

Build views:

Investments per month

Stage distribution

Sector allocation

Co-investor counts per VC

Add to README: explanation of metrics + definitions

End-of-week demo:

“Here is Sequoia’s sector breakdown.”

“Here are all co-investors for a16z this year.”

This is where it starts looking like a VC research tool.

WEEK 5 — Dashboard + UI Layer

Goal: Build the actual VC Portfolio Intelligence Dashboard.

Deliverables

Full dashboard with:

VC selector (multi-select)

Investments-over-time chart

Sector mix chart

Stage distribution chart

Deals table (sortable/filterable)

Map of portfolio companies

Comparison Mode:

Select 2–5 VCs → compare metrics

Tasks

Connect dashboard tool (Streamlit / Metabase / Looker Studio) to DB

Build visualizations:

Time-series

Bar/stacked-bar charts

Bubble or heatmap for sectors

Geo-map

Build VC comparison page

Add filters: sector, geography, date range

Polish UI (Aleo fonts, spacing, cards, color palette)

End-of-week demo:

Fully working dashboard you can click through live

This is your portfolio centerpiece

WEEK 6 — Automation, Alerts, Polish, Productionization

Goal: Convert your working dashboard into an auto-updating, production-grade system.

Deliverables

GitHub Actions / cron-based schedule:

Daily ingestion

Daily transformation

Weekly metrics recomputation

Email or Slack alert:

“Daily: New VC investments detected”

README updated with:

Architecture diagrams

Setup instructions

Screenshot GIFs of dashboard

Optional: Deploy Streamlit app publicly

Tasks

Write scheduled workflows (GitHub Actions or Prefect Cloud)

Add error monitoring + retries

Add alerting workflow

Add caching or incremental ingestion (only update new data)

Clean up and finalize documentation

Deploy if desired

End-of-week demo (final “launch”):

Fully automated pipeline

Dashboard updates itself

Clear README

Shareable public prototype

Optional Stretch Weeks (Super High Signal)
Week 7 — Graph Analytics

Build a network graph of co-investors using NetworkX or D3

Add “most central VC” metrics

Week 8 — Predictive Modeling

Build:

“Hot Sector Pulse Index”

“VC Deployment Momentum Score”

“Probability a VC will invest in sector X”

Week 9 — Company Similarity Engine

Use embeddings to cluster startups by product/type

Add a “similar companies” lookup to the dashboard