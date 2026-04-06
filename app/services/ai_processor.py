from openai import OpenAI
import json

client = OpenAI()

def process_medical_text(raw_text: str):
    try:
        prompt = f"""
        You are a medical transcription assistant.

        Clean and process the following transcript:
        - Remove filler words (um, uh, etc.)
        - Improve readability
        - Correct medical terms
        - Extract medical conditions/symptoms

        Transcript:
        {raw_text}

        Return ONLY JSON in this format:
        {{
            "transcript": "...",
            "conditions": [],
            "confidence": "high/medium/low"
        }}
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        content = response.choices[0].message.content

        return json.loads(content)

    except Exception as e:
        return {
            "transcript": raw_text,
            "conditions": [],
            "confidence": "low",
            "error": str(e)
        }