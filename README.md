# TradeIntel

Project structure for the TradeIntel workspace.
# TradeIntel

An AI-powered financial intelligence platform that combines Machine Learning, Retrieval-Augmented Generation (RAG), Local Large Language Models (LLMs), Technical Analysis, and News Sentiment Analysis to provide explainable stock market predictions.

---

## Overview

TradeIntel is designed to assist investors by combining quantitative market analysis with generative AI. Instead of only predicting stock prices, the platform explains *why* a prediction was made using retrieved financial context, technical indicators, and recent news sentiment.

The application integrates machine learning models, financial APIs, vector databases, and local LLMs into a single end-to-end system.

---

## Features

- Machine Learning based stock price prediction
- Technical Indicator Analysis
- Financial News Retrieval
- News Sentiment Analysis
- Retrieval-Augmented Generation (RAG)
- Local LLM powered investment analysis
- Feature Importance Visualization
- AI-generated Buy/Hold/Sell Recommendation
- Risk Assessment
- Confidence Score Calculation
- Trading Range Prediction
- Interactive React Dashboard
- FastAPI REST API

---

## Technology Stack

### Frontend

- React
- Vite
- Axios
- CSS

### Backend

- FastAPI
- Python

### Machine Learning

- Scikit-Learn
- Random Forest Regressor
- Pandas
- NumPy

### AI

- LangChain
- Ollama
- Qwen2.5
- ChromaDB
- Sentence Transformers

### APIs

- Yahoo Finance
- Finnhub API

---

# Project Architecture

```
                User

                  │

                  ▼

          React Frontend

                  │

                  ▼

          FastAPI Backend

                  │

      ┌───────────┼─────────────┐
      │           │             │
      ▼           ▼             ▼

 Machine      News Service     RAG

 Learning          │             │
                   ▼             ▼

          Sentiment Analysis  ChromaDB

                     │
                     ▼

              Local LLM (Qwen)

                     │

                     ▼

           AI Investment Report
```

---

# Machine Learning Pipeline

1. Download historical stock data.
2. Generate technical indicators.
3. Load trained Random Forest model.
4. Predict next trading day return.
5. Estimate confidence.
6. Calculate trading range.
7. Determine technical signal.
8. Generate final recommendation.

---

# AI Pipeline

1. Retrieve latest financial news.
2. Perform sentiment analysis.
3. Load financial documents.
4. Store embeddings in ChromaDB.
5. Retrieve relevant context.
6. Send prediction + sentiment + retrieved context to Local LLM.
7. Generate explainable investment analysis.

---

# Technical Indicators Used

- SMA
- EMA
- RSI
- MACD
- Bollinger Bands
- ATR
- Volatility
- Volume Change
- Return Lag 1
- Return Lag 2
- Return Lag 3

---

# API Endpoints

## Prediction

```
GET /predict/{ticker}
```

Returns

- Stock Prediction
- Trading Range
- Confidence
- Recommendation
- News Sentiment
- Feature Importance

---

## AI Analysis

```
GET /analyze/{ticker}
```

Returns

- Prediction
- AI Analysis
- Retrieved Context
- LLM Recommendation
- Pros & Cons
- Risk Assessment

---

# Project Structure

```
TradeIntel/

├── backend/
│
│   ├── app/
│   │
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── core/
│   ├── agents/
│   │
│   ├── documents/
│   ├── vector_db/
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│
│   ├── src/
│   │
│   ├── components/
│   ├── pages/
│   ├── services/
│   │
│   ├── App.jsx
│   └── main.jsx
│
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/TradeIntel.git

cd TradeIntel
```

---

## Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file.

```
FINNHUB_API_KEY=YOUR_API_KEY
```

Run

```bash
python -m uvicorn main:app --reload
```

Backend runs on

```
http://localhost:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# Example Workflow

1. User enters a stock ticker.
2. Backend downloads latest market data.
3. Technical indicators are generated.
4. Machine Learning predicts future price.
5. News articles are retrieved.
6. Sentiment analysis is performed.
7. Financial documents are retrieved using RAG.
8. Local LLM generates an investment report.
9. Dashboard displays prediction, AI reasoning, and retrieved evidence.

---

# Sample Output

Prediction

- Current Price
- Target Price
- Expected Return
- Trading Range
- Confidence
- Risk

AI Analysis

- Summary
- Recommendation
- Reasoning
- Bullish Factors
- Bearish Factors

News

- Latest Financial Headlines
- Sentiment

Feature Importance

- Top Machine Learning Features

Retrieved Context

- Financial documents retrieved through RAG


---

# Author

**Nischay**

Computer Science Engineering Student

AI • Machine Learning • Generative AI • Full Stack Development

---

# License

This project is developed for educational and portfolio purposes.