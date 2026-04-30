# 🎾 Tennis Data Ingestion Pipeline

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## 📋 Project Overview
This project implements a **robust data ingestion pipeline** designed to process and store historical tennis match data. The architecture leverages **Docker** for containerization and **PostgreSQL 18** for relational data storage, ensuring a scalable and reproducible environment for data engineering tasks.

> [!IMPORTANT]
> This project serves as the **foundational data layer** for a future MLOps pipeline designed to calculate **Expected Value (EV+)** and predict outcomes in tennis betting markets.

---

## ✨ Key Features
*   **Containerized Infrastructure:** Custom Docker environment orchestrating a PostgreSQL 18 instance.
*   **Data Transformation (ETL):** Python & Pandas for cleaning missing values, formatting date-time objects, and feature filtering.
*   **Automated Ingestion:** Streamlined ingestion script using SQLAlchemy for efficient CSV-to-SQL streaming.
*   **Data Validation:** Rigorous SQL testing to ensure data integrity and schema consistency.

---

## 🛠 Tech Stack
| Category | Technology |
| :--- | :--- |
| **Language** | Python (managed with `uv`) |
| **Database** | PostgreSQL 18 |
| **Containerization** | Docker & Docker Compose |
| **Libraries** | Pandas, SQLAlchemy, Psycopg2 |

---

## 🚀 How to Run the Project

### 1. Prerequisites
*   Install [Docker & Docker Compose](https://docs.docker.com/get-docker/).
*   Install [uv](https://github.com/astral-sh/uv) (Python package manager).

### 2. Database Setup
Launch the PostgreSQL engine in detached mode:
```bash
docker compose up -d pg_tenis
```

### 3. Environment configuration
Initialize the virtual environment and install dependencies:
```bash
# Using uv for near-instant installation
uv sync
```

### 4. Run the ingestion pipeline
Execute the Python script to clean and load the tennis data into the database:
```bash
uv run python ingest_data.py
```

### 5. Verify the data
To verify the records, launch pgAdmin:
```bash
docker compose up -d pgadmin
```

---

## 📊 Data Insights & Features
The pipeline processes comprehensive datasets to extract variables critical for **Expected Value (EV+)** analysis:

*   **📅 Match Metadata:** Tournament category (ATP 250, 500, Masters 1000, Grand Slams), surface type (Clay, Grass, Hard), and round progression.
*   **🎾 Performance Metrics:** Detailed in-game statistics including Aces, double faults, 1st serve win %, and break point conversion rates.
*   **💰 Market Odds:** Historical closing odds from various bookmakers, used to calculate the implied probability and find market inefficiencies.
*   **👤 Player Context:** Current ATP rankings, recent form (last 5 matches), and historical Head-to-Head (H2H) records.

---

## ⚙️ Technical Implementation Details

<details>
<summary><b>1. Advanced Data Cleaning</b></summary>
Implemented robust handling for inconsistent player name formats (e.g., "N. Djokovic" vs "Novak Djokovic"), normalization of tournament naming conventions, and automated filtering of <i>Walkovers</i> or incomplete matches that could bias the model.
</details>

<details>
<summary><b>2. Schema Optimization & Type Casting</b></summary>
Applied precise data typing in PostgreSQL to minimize storage footprint and maximize query speed. Categorical data (Surface, Tournament Level) is indexed for fast retrieval during large-scale historical backtesting.
</details>

<details>
<summary><b>3. Relational Database Design</b></summary>
The database is structured to support complex analytical queries, allowing the future MLOps pipeline to fetch time-series data with minimal latency.
</details>

---

## 🗺️ Future Roadmap (The MLOps Path)

| Stage | Focus | Status |
| :--- | :--- | :--- |
| **Stage 1** | **Data Ingestion:** ETL Pipeline & PostgreSQL Relational Storage. | 🟢 Completed |
| **Stage 2** | **Feature Engineering:** Creation of rolling averages and player Elo ratings. | 🟡 In Progress |
| **Stage 3** | **Model Training:** Implementing XGBoost/LightGBM for outcome probability. | ⚪ Planned |
| **Stage 4** | **Deployment:** Automated bot for real-time EV+ opportunity detection. | ⚪ Planned |

---
