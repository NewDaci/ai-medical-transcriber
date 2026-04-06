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

### 1. Install dependencies

```
pip install fastapi uvicorn faster-whisper python-multipart
```

### 2. Run server

```
uvicorn app.main:app --reload
```

### 3. Open API docs

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
