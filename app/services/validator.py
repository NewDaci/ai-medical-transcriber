from openai import OpenAI

client = OpenAI()

def validate_output(transcript: str, conditions: list):
    try:
        prompt = f"""
        You are a medical assistant.

        Analyze the transcript and extracted conditions.

        Transcript:
        {transcript}

        Extracted Conditions:
        {conditions}

        Evaluate:
        1. Are the conditions correct?
        2. Are any important conditions missing?

        Return ONLY JSON:
        {{
            "confidence": "high/medium/low",
            "suggested_conditions": []
        }}
        """

        print("calling validation with prompt:")
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        content = response.choices[0].message.content

        return content

    except Exception as e:
        return {"confidence": "unknown", "error": str(e)}