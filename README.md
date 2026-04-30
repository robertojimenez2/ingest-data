Project Overview
This project implements a robust data ingestion pipeline designed to process and store historical tennis match data. The architecture leverages Docker for containerization and PostgreSQL for relational data storage, ensuring a scalable and reproducible environment for data engineering tasks.

Key Features
Containerized Infrastructure: Developed a custom Docker environment to orchestrate a PostgreSQL 18 instance, providing a consistent database setup across different development environments.

Data Transformation (ETL): Utilized Python (Pandas) to perform data cleaning and preprocessing. This stage involves handling missing values, formatting date-time objects, and filtering relevant features for sports betting analysis and predictive modeling.

Automated Ingestion: Implemented a Python-based ingestion script using SQLAlchemy to efficiently stream cleaned data from CSV files into the SQL database.

Data Validation: Conducted rigorous testing via SQL queries to ensure data integrity, schema consistency, and successful record insertion.

Tech Stack
Language: Python (managed with uv)

Database: PostgreSQL

Containerization: Docker & Docker Compose

Libraries: Pandas, SQLAlchemy, Psycopg2

This project serves as the foundational data layer for a future MLOps pipeline designed to calculate Expected Value (EV+) and predict outcomes in tennis betting markets.

How to Run the Project
Follow these steps to set up the environment and run the ingestion pipeline:

1. Prerequisites
Ensure you have Docker and Docker Compose installed.

Install uv (Python package manager) for fast dependency handling.
docker compose up -d pg_tenis

3. Environment Configuration
Initialize the virtual environment and install the necessary dependencies:

# Using uv for faster installation
uv sync

4. Run the Ingestion Pipeline
Execute the Python script to clean and load the tennis data into the database:
uv run python ingest_data.py

5. Verify the Data
You can access pgAdmin at http://localhost:8085 to run SQL queries and verify the ingested records, or use any SQL client connected to localhost:5432.
Remember to up the container pgadmin
docker compose up -d pg_tenis

Data Insights & Features
The pipeline processes comprehensive tennis datasets, focusing on variables critical for Expected Value (EV+) calculations:

Match Metadata: Tournament level, surface type (Clay, Grass, Hard), and round information.

Performance Metrics: Aces, double faults, first-serve percentage, and break points saved/converted.

Market Odds: Historical betting odds from multiple bookmakers, essential for identifying market inefficiencies and calculating probability gaps.

Player Statistics: Current rankings, head-to-head records, and recent form indicators.

Technical Implementation Details
Data Cleaning: Handling of inconsistent player names, normalization of tournament categories, and treatment of "Walkovers" or retired matches.

Type Casting: Precise conversion of categorical data into efficient formats for PostgreSQL and ensuring time-series integrity for historical analysis.

Database Schema: Optimized for analytical queries, enabling fast retrieval of historical match outcomes to backtest betting strategies.

Future Roadmap (The MLOps Path)
This repository is the first stage of a larger ecosystem:

Stage 1 (Current): ETL Pipeline & Relational Storage.

Stage 2: Feature Engineering & Exploratory Data Analysis (EDA).

Stage 3: Model Training (XGBoost/LightGBM) for match outcome probability.

Stage 4: Deployment of an automated bot to identify EV+ opportunities in real-time.

2. Database Setup
Launch the PostgreSQL container in detached mode:
