from fastapi import FastAPI, UploadFile, File
import shutil
import os

from app.services.transcription import transcribe_audio
from app.services.cleaner import clean_text
from app.services.medical import correct_medical_terms
from app.services.validator import validate_output
import json
import uuid

from app.services.ai_processor import process_medical_text

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
        print("transcribed done")

        # save raw transcript file
        base_name = os.path.splitext(file.filename)[0]
        raw_filename = f"raw_{base_name}.txt"
        with open(raw_filename, "w") as raw_file:
            raw_file.write(raw_text)

        # Step 2: AI processing
        result = process_medical_text(raw_text)
        if "transcript" not in result:
            result = {
                "transcript": raw_text,
                "conditions": [],
                "confidence": "medium"
            }

        final_text = result["transcript"]
        conditions = result["conditions"]
        confidence = result["confidence"]
        

        # # step 2: cleaning
        # cleaned_text = clean_text(raw_text)

        # # step 3: medical correction
        # final_text, conditions = correct_medical_terms(cleaned_text)
        # validation = validate_output(final_text, conditions)

        # try:
        #     validation_json = json.loads(validation)
        #     confidence = validation_json.get("confidence", "medium")
        #     conditions = validation_json.get("suggested_conditions", conditions)
        # except:
        #     confidence = "medium"

        # cleanup
        os.remove(file_path)
        output_filename = f"output_{base_name}.txt"

        with open(output_filename, "w") as f:
            f.write(f"""
Transcript:
{final_text}

Conditions:
{', '.join(conditions)}

Confidence:
{confidence}
""")

        return {
            "transcript": final_text,
            "conditions": conditions,
            "confidence": confidence
        }

    except Exception as e:
        return {"error": str(e)}