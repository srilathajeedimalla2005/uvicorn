# Trade Opportunities API

## 🚀 Overview
FastAPI service that analyzes Indian market sectors and provides trade insights using AI.

## 🛠 Tech Stack
- FastAPI
- Python
- Gemini API

## 📌 Endpoint
GET /analyze/{sector}

## 🔑 Authentication
Header:
x-api-key: secret123

## ▶️ Run Locally
```bash
uvicorn app.main:app --reload