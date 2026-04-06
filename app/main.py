from fastapi import FastAPI, UploadFile, File
import shutil
import os

from app.services.transcription import transcribe_audio
from app.services.cleaner import clean_text
from app.services.medical import correct_medical_terms

app = FastAPI()


@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    try:
        file_path = f"temp_{file.filename}"

        # save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # step 1: transcription
        raw_text = transcribe_audio(file_path)

        # step 2: cleaning
        cleaned_text = clean_text(raw_text)

        # step 3: medical correction
        final_text, conditions = correct_medical_terms(cleaned_text)

        # cleanup
        os.remove(file_path)

        return {
            "transcript": final_text,
            "conditions": conditions,
            "confidence": "high" if len(conditions) >= 2 else "medium"
        }

    except Exception as e:
        return {"error": str(e)}