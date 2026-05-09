```tree
Streaming Data Platform
        +
Feature Engineering System
        +
ML Training Pipeline
        +
Real-Time Prediction Engine
        +
Analytics Dashboard
```
## 1. High-Level System Architecture

```text
                ┌────────────────────┐
                │ Binance WebSocket  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Async Data Collector│
                │ Python + asyncio   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Kafka / Redpanda   │
                │ Streaming Bus      │
                └─────────┬──────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
┌──────────────┐ ┌────────────────┐ ┌─────────────────┐
│ Raw Storage  │ │ Spark Streaming│ │ Live Dashboard  │
│ Parquet/S3   │ │ Feature Engine │ │ Streamlit       │
└──────┬───────┘ └────────┬───────┘ └─────────────────┘
       │                  │
       ▼                  ▼
┌──────────────┐ ┌────────────────────┐
│ Historical DB│ │ Feature Store       │
│ ClickHouse   │ │ DuckDB/ClickHouse   │
└──────┬───────┘ └─────────┬──────────┘
       │                   │
       ▼                   ▼
┌────────────────────────────────────┐
│ ML Training Pipeline               │
│ XGBoost / LightGBM / LSTM          │
└─────────────────┬──────────────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Model Registry     │
        │ MLflow             │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Real-Time Inference│
        │ Prediction API     │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Trading Dashboard  │
        └────────────────────┘

```