# 🔍 TruthLens AI — Fake News Detection System

TruthLens AI is an AI-powered Fake News Detection web application that analyzes news articles and predicts whether the content is **FAKE** or **REAL**.

The system uses **Natural Language Processing (NLP)** and **Machine Learning** to convert news text into numerical features using **TF-IDF** and classify the article using a **Logistic Regression** model.

It also stores analysis results in a **SQLite database** and generates an **Excel analysis report**.

---

## 🚀 Project Overview

The spread of misleading information through online platforms makes it difficult to distinguish between reliable and fake news.

TruthLens AI provides a simple interface where users can:

- 📰 Enter a news article or headline
- 🤖 Analyze the content using Machine Learning
- 🔍 Predict whether the news is FAKE or REAL
- 📊 Display the prediction confidence
- 💾 Store analysis history in SQLite
- 📑 Generate an Excel report

---

## ✨ Features

- 🤖 AI-powered fake news classification
- 📰 News article and headline analysis
- 🧠 Natural Language Processing
- 📌 TF-IDF feature extraction
- 📊 Logistic Regression classification
- 🎯 98.95% test accuracy
- 📈 Prediction confidence score
- 💾 SQLite database storage
- 📑 Excel report generation
- ⚡ Flask REST API
- ⚛️ React frontend
- 🎨 Modern responsive interface
- 🔄 Frontend-backend integration

---

## 🧠 Machine Learning

### Machine Learning Pipeline

```text
News Article
     ↓
Text Cleaning
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression
     ↓
FAKE / REAL Prediction
     ↓
Confidence Score