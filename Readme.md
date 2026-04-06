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

## 📋 Test Results

### Test File 1: testfile1.mp3 (Chest Pain Case)

**Conditions Detected:** `chest pain`, `breathing`, `light-headed`

**Output:**
```json
{
  "transcript": "brought you in today? sure. i'm just having a lot of chest pain and so i thought i should get a checked out. okay. and before we start, could you remind me of your gender and age? sure. 39. i'm a male. okay. and so when did this chest pain start? it started last night, but it's becoming sharper. okay. and where is this pain located? it's located on the left side of my chest. okay. and so how long has it been going on for that if it started last night? so i guess it would be a couple of hours now, maybe eight. okay. has it been constant throughout that time or changing? i would say it's been pretty constant, yeah. okay. and how would you describe the pain? people will use words sometimes sharp burning, achy. i think it's pretty sharp, yeah. it's sharp. okay. anything that you have done tried since last night that's made the pain better? not laying down helps. okay. so do you find laying down makes the pain worse? yes, definitely. okay. do you find that the pain is radiating anywhere? no. okay. and is there anything else that makes the pain worse besides laying down? not that i've noticed. no. okay. so not taking a deep breath or anything that? maybe taking a deep breath. yeah. okay. and one of the pains started, could you tell you, could you think of anything that you were doing at the time? i mean, i was moving some furniture around, but that i've done that before. okay. so you didn't feel you hurt yourself when you were doing that? no. okay. and in regards to how severe the pain is on a scale of 1 to 10, 10 being the worst pain you've ever felt, how severe would you say the pain is? i'd say it's a 7 or 8. it's pretty bad. okay. and with the pain, do you have any other associated symptoms? i feel a little light-headed and i'm having some trouble breathing. okay. have you had any loss of consciousness? no. okay. have you been experiencing any racing of the heart? a little bit. yeah. okay. and have you been sweaty at all? just from the shirt, just from having issues breathing. okay. have you been having issues breathing since the pain started? yes. okay. and recently, have you had any periods of time where you have been immobilized or you haven't been able to move around a lot? no. no. okay. and have you been feeling sick at all? any infectious symptoms? no. okay. have you had any nausea or vomiting? no. any fever or chills? no. okay. how about any abdominal pain? no. any urinary problems? no. or bowel problems? okay. have you had a cough? no. okay. you haven't brought up any blood? no. have you had a wheeze with your difficulty breathing? no. not that i've heard. okay. any changes to the breath sounds at all? , any noisy breathing? no. well, i guess when i'm really having trouble breathing, yeah. okay. has anything this ever happened to you before? no. no. okay. and have you had any night sweats? no. all right. and then how about any rashes or skin changes? no rashes, but i guess my neck seems to be a little swollen. okay. do you have any neck pain? no. okay. have you had any accidents a car accident or anything where you really jerked your neck? no. okay. any trauma at all to the chest or or back? no. no. okay. so just in regards to past medical history, do you have any prior medical conditions? no. okay. any recent hospitalizations? no. okay. any prior surgeries? no. okay. do you take any medications regularly? are they prescribed or over the counter? no. all right. how about any allergies to medications? no. none. all right. any immunizations or are they up to date? they're all up to date. excellent. all right. and could you tell me a little bit about your living situation currently? sure. i live in an apartment by myself. yep. that's about it. okay. and how do you support yourself financially? i'm an accountant. okay. sounds a pretty stressful job or that it can be. do you smoke cigarettes? i do. okay. how much do you smoke? i smoke about a pack a day. okay. how long have you been smoking for? for the past 10 to 15 years. okay. and do you smoke cannabis? sometimes. how much marijuana would you smoke per week? per week? maybe about five milligrams, not that much. okay. and do you use any other recreational drugs cocaine, crystal meth? no. opioids? no. okay. have you used iv drugs before? no. okay. and do you drink alcohol? i do. okay. how much alcohol do you drink each week? about i have one or two drinks a day, so about 10 drinks a week. okay. and then briefly, could you tell me a little bit about your diet and exercise? sure. i try to eat healthy for dinner at least, but most of my lunches are i eat out. and then in terms of exercise, i try to exercise every other day. i run for about half an hour. okay. oh, that's great. i dream in working on the activity and the diets as well. so has anything this happened in your family before? no. okay. has anybody in the family had a heart attack before? actually, yes. my father had a heart attack when he was 45. okay. and anybody in the family have cholesterol problems? i think my father did. i see. okay. and how about anybody in the family have stroke? no strokes. okay. and then any cancers in the family? no. okay. was there anything else that you wanted to tell me about today that on history? no, i don't think so. i think you asked me everything.",
  "conditions": ["chest pain", "breathing", "light-headed"],
  "confidence": "high"
}
```

---

### Test File 2: testfile2.mp3 (Hand/Thumb Pain Case)

**Conditions Detected:** `osteoarthritis`, `tenosynovitis`

**Output:**
```json
{
  "transcript": "we'll bring you in here today. i'm here because my left hand kind of just at the base of my thumb has been hurting for the past two days and it seems to be getting worse and i'm left handed so it's really hard for me to write or do anything or i have to clench or grip things. okay, and how long has this been going on for? so for the past two days but it's got it's got bad yesterday. okay, and have you had any, if you were to describe the pain, where is it located exactly? it's just at the base of my thumb, where the fleshy part of your hand is. okay, yeah, yeah, yeah, so just just over there. okay, and what kind of pain is it, is it sharp or is it aching? it's a baseline, it's an achy pain but if i try to move it or try to write or you know use a computer or anything that, it becomes sharp. on a scale of 0 to 10, 10 being the worst pain you've felt in your life, how much would you rate it? i'd say a six. okay, and does this pain move anywhere else in your hand or does it just stay where you described? it just stays there. okay, and what kind of motions caused the most pain? i'd say , , trying to touch my pinky with my thumb, that hurts, just trying to rotate it hurts. okay, have you tried anything for the pain that has helped? no, i haven't really tried too much, i've just tried not to use it as much. i see, okay, and has this ever , have you ever had any injuries to this hand, any trauma, either recently or in the past? no, nothing that. okay, and is there any, do you do any kind of repetitive work that requires gripping or lifting with that hand, anything repetitive? so, i do a lot of work at the computer, and i guess i tend to type a lot with my left hand, so maybe that. okay, and sorry, i also take lots of notes, handwriting notes with my left hand. okay, so are you left-handed? yes. okay, all right, have you been diagnosed with any medical conditions in the past? no. no, so you're healthy? yes. do you take any medications on a regular basis? no, no. okay, any allergies to any medications? no, allergies. okay, any previous surgeries or hospitalizations? no. no, any family history of any medical conditions, whether it's musculoskeletal or over to logic, any conditions? no, nothing that. okay, any cancers in the family? i know there's, yeah, there's a lot of cancer in the family. there's colon cancer, breast cancer, or wearing in cancer. okay, and are they first degree relatives who have those cancers? no, first degree relatives, just aunts and uncles. okay, all right, and currently are you working right now or have you had any time all for or for any modified duties? so i'm still working online. i've just haven't been taking notes by hand anymore. i see. and has that helped at all? yeah, it has helped a little bit because i'm not moving my hand as much, so it helps with the pain. okay. have you taken any tylenol at all, anything for the pain? no, i haven't. all right, and currently right now, what is your living situation ? i live in an apartment by myself. okay, and do you currently smoke cigarettes? i used to smoke five years ago, and i only did that for a year or two, and it wasn't very much, but i don't smoke anymore. okay, that's good. any alcohol? i don't have a beer on the weekend. okay, any recreational drugs marijuana? , i will take an edible once a month. okay. and yeah, those were just some of the questions i had. and we're just going to do a few things for examining that area. so are you able to make a list? , i can, but it hurts. okay, and it hurts in that location that you mentioned? yes. okay, how about, , if you make a list about your thumb, does it still hurt, or is it just when you are moving the thumb? it's just when i'm moving the thumb. okay, and if you were able to, are you able to rotate your wrist? , yes, i can rotate my wrist. does that hurt at all? no. okay, , now i just want you to do this one test. it's called a single scene test. okay. so i want you to let your thumb press it up, , down against your palm. okay. and then hold your head. sorry, no, go ahead. yeah, and then after you do that, , , bring your fingers above your thumb or just cover your thumb. okay. kind of a fist, but your thumb is on the inside of your fingers. okay. and then, , bring your, , arm out. okay. and with your other hand, can you, , from above, push your wrist downwards. so your, , pinky finger is, , pointing to the, pointing to the ground. okay. yeah, and does that hurt at all? , when you, so this is just called an all-nerd deviation of your, , of your wrist. , does that hurt at all? yes, that is very painful. that's very painful. okay. all right. , and then you're also having pain and gripping and okay. so those are kind of all the things i want to ask. , it seems that you may be having something, , called a de quervain's, , , tenosynovitis. , it's caused by some repetitive motions that it can be due to gripping. , in terms of happens to, , new mothers who are left in their children as well as their care workers. it can also happen in other work environments. , so what we will first just need to do. , is we may need to just pull up something osteoarthritis. you are fairly young, but if there was ever an injury in the past, you can have an early osteoarthritis in the area. so we just want to get an x-ray. , but other than that, the way we kind of deal with this issue is usually conservatively and with the splint. , and it's splint for your thumb. that helps relieve some of these symptoms, , restrict some of your movements, reduces some of the swelling. and if it does get really bad, it's affecting your work and the conservative management could pain and the splint don't work. and if you get therapy, we do, , offer, , injecting corticosteroid injection into just right, look in the area that you mentioned, right below the thumb. , and that often has some symptoms as well. , but , first yeah, let's just do some conservative management and see if that helps. it's only been a few days. so hopefully, , we'll try first helps and then we can go on from there. okay, yeah, that sounds great. thank you. welcome to take care. you too.",
  "conditions": ["osteoarthritis", "tenosynovitis"],
  "confidence": "high"
}
```

**Note:** This is the test case that demonstrated the importance of the fix - it now correctly identifies musculoskeletal conditions that were previously missed.

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
