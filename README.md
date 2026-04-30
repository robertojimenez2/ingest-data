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
