# Automated E-Commerce Data Pipeline

A fully automated data engineering pipeline that extracts product data from a live API, transforms it using Python/Pandas, and loads it into a cloud PostgreSQL database on a scheduled basis.

Built to solve a common business problem: **giving e-commerce teams a clean, queryable dataset every morning without manual intervention.**

---

## What This Does

| Step | Tool | Purpose |
|------|------|---------|
| **Extract** | Python + Requests | Pulls live product data from a REST API |
| **Transform** | Pandas | Flattens nested JSON, cleans types, removes noise |
| **Load** | SQLAlchemy + PostgreSQL | Pushes clean data to Neon.tech cloud database |
| **Automate** | GitHub Actions | Runs the full pipeline daily at 6:00 AM UTC |

---

## Tech Stack

- **Language:** Python 3.10
- **Data Manipulation:** Pandas
- **Database:** PostgreSQL (hosted on [Neon.tech](https://neon.tech))
- **ORM/Connection:** SQLAlchemy + psycopg2
- **Automation:** GitHub Actions (CI/CD)
- **API Source:** [FakeStore API](https://fakestoreapi.com/) (simulating real e-commerce data)

---

## Business Insights Delivered

This pipeline powers SQL views that answer key business questions:

- **Category Performance:** Which product categories have the highest engagement and pricing?
- **Product Health:** Identify underperforming products by rating and review volume.
- **Executive Summary:** Store-wide averages for price, ratings, and total reviews.

> *Sample insight from live data: Electronics drives the highest average price and customer engagement, while Jewelery commands a premium price but suffers from the lowest engagement — indicating a potential marketing opportunity.*

---

## How It Runs

This pipeline is scheduled via **GitHub Actions** to run automatically every day at 6:00 AM UTC. 

It can also be triggered manually:
1. Go to the **Actions** tab in this repository.
2. Select **Daily ETL Pipeline**.
3. Click **Run workflow**.

---

## Security

- Database credentials are stored as **GitHub Secrets** and are never exposed in the codebase.
- Connection strings are injected at runtime via environment variables.

---

## Future Enhancements

- [ ] Implement **UPSERT** logic to handle duplicate records across daily runs.
- [ ] Add data quality checks (null counts, outlier detection) before loading.
- [ ] Connect to a BI tool (Metabase / Tableau) for live dashboard reporting.
- [ ] Add email/Slack alerting if the pipeline fails.

---

*Built by Diovu Charles — Data Engineer specializing in automated ETL pipelines and cloud data solutions.*

## Architecture
