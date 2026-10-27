# Policy_Match_AI (GovSchemeAI)

> **Conversational Government Scheme Advisor using RAG, FAISS Semantic Search, and Large Language Models.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![FAISS](https://img.shields.io/badge/Vector%20Search-FAISS-green.svg)](https://github.com/facebookresearch/faiss)
[![Groq](https://img.shields.io/badge/LLM-Groq%20LLaMA--3.3--70B-orange.svg)](https://groq.com/)
[![Flutter](https://img.shields.io/badge/Frontend-Flutter-02569B.svg)](https://flutter.dev/)
[![NDCG@5](https://img.shields.io/badge/RAG%20Score-NDCG%405%200.8324-brightgreen.svg)]()

---

## 📌 Overview

**Policy_Match_AI** is an AI-powered conversational platform engineered to simplify access to government welfare schemes for Indian citizens. 

While the central and state governments offer thousands of assistance programs, citizens frequently miss out due to fragmented information, bureaucratic language, and complex eligibility criteria. **Policy_Match_AI** replaces rigid portal browsing with a natural, conversational advisor capable of understanding citizen queries, dynamically profiling user demographics, and recommending verified policies from a curated database of **3,368+ government schemes**.

Citizens can interact naturally through **text chat, real-time voice, or an interactive AI avatar** in their native language (**English, Hindi, Tamil, and Kannada**).

---

## 🌟 Key Features

- **Curated Knowledge Base (3,368+ Schemes):** Comprehensive dataset spanning Agriculture, Education, Women Welfare, Healthcare, MSME/Business, and Social Security.
- **Dense Semantic Retrieval:** Powered by `SentenceTransformer("all-MiniLM-L6-v2")` and **FAISS** vector search for high-speed, sub-millisecond similarity matching in 384-dimensional space.
- **Dynamic User Profiling:** Automatically extracts demographic constraints (*Age, Occupation, Income, State, Social Category, Gender*) using LLM extraction with regex fallback.
- **Hallucination-Free Generation:** Answers are synthesized using **Groq (`llama-3.3-70b-versatile`)**, strictly grounded in retrieved scheme facts.
- **Multi-Turn Context & Session Memory:** Maintains conversational history and detects follow-up questions (e.g., *"Am I eligible for the second one?"*).
- **Production-Ready REST API:** Built with **FastAPI** with CORS middleware, session lifecycle tracking, and auto-generated Swagger documentation.
- **Quantitative RAG Evaluation:** Evaluated with formal Information Retrieval metrics (**NDCG@5 = 0.8324**, **MRR = 0.8100**, **Hit Rate = 100%**).
- **Cross-Platform Mobile App (Flutter):** Fully featured client with multi-language localization, Speech-to-Text, Text-to-Speech, and an interactive video avatar interface.

---

## 🏗️ System Architecture

```text
Citizen Input (Text / Voice / Video Avatar)
                     │
                     ▼
        Flutter Mobile Application
                     │  HTTP / JSON
                     ▼
         FastAPI Backend (main.py)
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
Profile Extractor       Session / Dialogue Memory
(Age, Income, State)    (Multi-turn context tracking)
         │                       │
         └───────────┬───────────┘
                     ▼
      Query Formulation & Enrichment
                     │
                     ▼
     SentenceTransformer Embeddings
           (all-MiniLM-L6-v2)
                     │
                     ▼
        FAISS Semantic Vector Index
         (3,368 Schemes in RAM)
                     │
                     ▼
           Top-K Relevant Schemes
                     │
                     ▼
          Groq LLM (LLaMA 3.3 70B)
    (Grounded multi-lingual explanation)
                     │
                     ▼
      Personalized Scheme Guidance
```

---

## 📊 RAG Performance & Benchmark Evaluation

A formal Information Retrieval benchmark (`rag_evaluator.py`) was conducted across test queries with labeled ground-truth data:

| Metric | Score Achieved | Quality Threshold | Interpretation |
| :--- | :---: | :---: | :--- |
| **NDCG@5** | **`0.8324`** | $> 0.80$ (Excellent) | Scheme recommendations are **83.2% optimally ranked** by relevance. |
| **MRR** | **`0.8100`** | $> 0.70$ (High) | The first strictly relevant scheme appears on average at rank **1.2**. |
| **Precision@5** | **`0.8400`** | $> 0.75$ (Strong) | **84%** of all schemes in the top-5 recommendations are relevant. |
| **Recall** | **`0.7600`** | $> 0.70$ (Good) | Covers **76%** of all matching welfare programs in the database. |
| **Hit Rate** | **`100.0%`** | $100\%$ | Every tested user query successfully surfaced relevant schemes. |
| **Query Latency** | **`300 - 500 ms`** | Real-time | Rapid retrieval and generation powered by FAISS and Groq LPU. |

---

## 💡 How It Works: Semantic Search vs Keyword Matching

Traditional search fails when citizens describe their life situations without using official bureaucratic terms:

| What the Citizen Says | Keyword Search Result | Semantic Search Result (Our System) |
| :--- | :---: | :--- |
| *"My crops got ruined in the flood."* | ❌ **0 Matches** (Words "ruined" / "flood" missing) | ✅ **PM Fasal Bima Yojana** (Understands calamity crop insurance in vector space) |
| *"Help paying tuition for my daughter after 12th."* | ❌ **0 Matches** | ✅ **Pragati / Post-Matric Scholarship** (Identifies higher education aid) |
| *"Support for single mothers."* | ❌ **0 Matches** | ✅ **Indira Gandhi Widow & Destitute Women Pension** (Maps to assistance neighborhood) |

---

## 📁 Repository Structure

```text
GovSchemeAI/
├── data/
│   ├── cleaned_schemes.csv            # Cleaned scheme dataset (3,368+ records)
│   ├── schemes_with_text.csv          # Unified textual representations
│   ├── schemes_with_embeddings.csv    # Schemes mapped with embedding indices
│   └── candidate_ground_truth.csv     # Labeled benchmark ground-truth
├── models/
│   ├── scheme_index.faiss             # Pre-built FAISS dense vector index
│   └── embeddings.npy                 # 384-dimensional numpy vector arrays
├── src/
│   ├── app.py                         # Production GovernmentSchemeAssistant pipeline
│   ├── rag_engine.py                  # Optimized RAG engine with FAISS & cache
│   ├── profile_extractor.py           # Demographic extractor (Groq + Regex fallback)
│   ├── response_generator.py          # Grounded Groq response synthesizer
│   ├── conversation_manager.py        # Dialogue state & multi-turn memory
│   ├── utils.py                       # Follow-up intent detection helpers
│   ├── search.py                      # Standalone vector search module
│   ├── embedding.py                   # Embedding generation pipeline
│   ├── faiss_index.py                 # FAISS indexing build script
│   └── cleaning_*.py                  # Data cleaning and text merging scripts
├── testing/
│   ├── test_engine.py                 # RAG retrieval tests
│   ├── test_groq.py                   # Groq API integration test
│   ├── test_model.py                  # SentenceTransformer test
│   └── quick_test.py                  # End-to-end quick pipeline check
├── markdowns/
│   ├── BACKEND_GUIDE.md               # Backend architecture & deployment guide
│   ├── DELIVERY_SUMMARY.md            # Comprehensive project delivery recap
│   ├── QUICK_START.md                 # 5-minute setup and presentation talking points
│   └── GovSchemeAI_Complete_Project_Report.pdf  # Formal project report PDF
├── main.py                            # FastAPI server (/chat, /new-session)
├── rag_evaluator.py                   # Quantitative RAG evaluation runner
├── analyze_results.py                 # Evaluates best and worst query scores
├── build_ground_truth.py              # Ground-truth dataset builder
├── requirements.txt                   # Complete Python dependencies
├── .env.example                       # Environment variable templates
└── README.md
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Python 3.10+
- A free [Groq API Key](https://console.groq.com/)

### 2. Clone and Setup Environment

```bash
# Clone the repository
git clone https://github.com/naveenkumark2830-spec/Policy_Match_AI.git
cd Policy_Match_AI

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory (based on `.env.example`):

```bash
cp .env.example .env
```

Open `.env` and add your Groq API key:

```env
GROQ_API_KEY=gsk_your_groq_api_key_here
```

### 4. Run Interactive CLI Advisor

```bash
python -m src.app
```

### 5. Start the FastAPI Server

```bash
python main.py
# Or using uvicorn:
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Interactive Swagger documentation is available at:
**[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## 📡 API Reference

### 1. Create a New Session
* **Endpoint:** `GET /new-session`
* **Response:**
  ```json
  {
    "session_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
  ```

### 2. Send a Chat Message
* **Endpoint:** `POST /chat`
* **Request Body:**
  ```json
  {
    "session_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "message": "I am a small farmer in Karnataka with annual income of 1.5 lakh.",
    "language": "English"
  }
  ```
* **Supported Languages:** `"English"`, `"Hindi"`, `"Tamil"`, `"Kannada"`
* **Response:**
  ```json
  {
    "session_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "response": "Based on your profile, here are the top schemes for you: \n1. PM-KISAN..."
  }
  ```

---

## 🧪 Running RAG Benchmarks

To evaluate retrieval precision, NDCG, and reciprocal ranks against the ground-truth benchmark:

```bash
python rag_evaluator.py
```

To inspect performance across individual queries:

```bash
python analyze_results.py
```

---

## 📱 Mobile Client (Flutter)

The companion cross-platform mobile client (`govschemeai_app`) includes:
- **Multilingual UI:** One-tap switching between English, Hindi, Tamil, and Kannada.
- **Voice Screen:** Real-time speech input (`speech_to_text`) and natural spoken responses (`flutter_tts`) with audio pulse visualization.
- **Interactive AI Avatar:** Video call simulation with real-time camera feed (`camera`), animated talking avatar head, and synchronized captions.
- **Category Explorer:** Instant browsing for Farmers, Students, Women, Startups, Senior Citizens, and Employment.

---

## 👥 Authors & Academic Credits

- **Naveen Kumar K** (MSc Big Data Analytics, Reg No: `252BDA25`)
- **Dharnesh** (MSc Big Data Analytics, Reg No: `252BDA27`)
- **Prithvish William** (MSc Big Data Analytics, Reg No: `252BDA18`)

*Department of Big Data Analytics, St. Joseph's University, Bengaluru.*

---

## 📄 License & Disclaimer

This project is developed for educational and academic research purposes. Government scheme data is sourced from public portals. Always verify terms and deadlines on official state and central ministry websites before application.
