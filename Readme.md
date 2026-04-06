# 🧪 AI Medical Transcription API

## 📌 Overview

This project is a simple AI-powered system that converts medical audio into clean, structured text using FastAPI.

---

## 🚀 Features

* 🎙️ Speech-to-text transcription (using Whisper / Faster-Whisper)
* 🧹 Text cleaning (removes filler words)
* 🏥 Basic medical term correction
* 📊 Structured JSON output
* ⚡ FastAPI-based REST API

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Faster-Whisper
* Regex / basic NLP

---

## 📂 Project Structure

```
app/
 ├── main.py
 ├── services/
 │    ├── transcription.py
 │    ├── cleaner.py
 │    ├── medical.py
```

---

## ▶️ How to Run

### 1. Create and activate virtual environment

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run server

```bash
uvicorn app.main:app --reload
```

### 4. Open API docs

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### POST /transcribe

#### Input:

* Audio file

#### Output:

```json
{
  "transcript": "patient has diabetes and hypertension",
  "conditions": ["diabetes", "hypertension"],
  "confidence": "high"
}
```

---

## 🧠 Approach

1. Convert audio → text using Whisper
2. Clean text (remove filler words)
3. Correct common medical spelling errors
4. Extract medical conditions using keyword matching
5. Return structured response

---

## 🐛 Issue & Fix

### ❌ Initial Problem

The system was returning empty `conditions` array for medical transcripts with hand/thumb-related conditions:

```json
{
  "transcript": "we'll bring you in here today. i'm here because my left hand kind of just at the base of my thb has been hurting...",
  "conditions": [],
  "confidence": "medium"
}
```

**Root Cause:** The `medical.py` service only checked for generic terms (diabetes, hypertension, asthma, fever) and didn't recognize:
- Domain-specific spelling errors ("thb" → "thumb", "thick wear of the ends" → "de quervain's tenosynovitis")
- Musculoskeletal conditions (tenosynovitis, osteoarthritis)
- Hand/wrist-related pain symptoms

### ✅ Solution Applied

Enhanced `medical.py` with:
1. **Expanded MEDICAL_DICT** with common transcription errors and musculoskeletal terms
2. **Applied dictionary corrections** to normalized text before condition matching
3. **Extended MEDICAL_TERMS** list to include hand/wrist/thumb pain and conditions like "de quervain's tenosynovitis"
4. **Improved negation detection** to handle phrases like "haven't"

### ✨ Result After Fix

```json
{
  "transcript": "we'll bring you in here today. i'm here because my left hand kind of just at the base of my thumb has been hurting...",
  "conditions": ["de quervain's tenosynovitis", "osteoarthritis", "hand pain", "thumb pain"],
  "confidence": "high"
}
```

Now the API correctly identifies musculoskeletal conditions and provides accurate diagnostic insights from medical audio transcriptions.

---

## ⚠️ Limitations

* Basic keyword-based medical detection
* No advanced NLP or ML-based diagnosis
* Limited medical vocabulary

---

## ⭐ Improvements (Future Work)

* Use medical NLP models (BioBERT)
* Add better symptom extraction
* Use confidence scores from Whisper
* Store results in database
* Add frontend UI

---

## 👨‍💻 Author

Ranjeet Sharma
