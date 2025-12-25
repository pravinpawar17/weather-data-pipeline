# Weather Data Analytics Pipeline

## Overview
End-to-end automated data pipeline to ingest, process, and visualize live weather data.

## Architecture
AWS Lambda → Amazon S3 → Databricks (Bronze/Silver/Gold) → Power BI

## Tech Stack
- AWS Lambda, S3, EventBridge, CloudWatch
- Databricks, Delta Lake, PySpark
- SQL, Power BI

## Key Features
- Event-driven ingestion from OpenWeather API
- Medallion architecture (Bronze, Silver, Gold)
- Automated Databricks pipeline using file-arrival triggers
- Interactive Power BI dashboard

## Repository Structure

weather-data-pipeline/
├── lambda/
├── databricks/
├── sql/
├── dashboard/
├── architecture/


*************************


## How to Run
1. Deploy Lambda and schedule using EventBridge
2. Configure Databricks external location for S3
3. Run Databricks Job (auto-triggered on file arrival)
4. Connect Power BI to Databricks SQL
