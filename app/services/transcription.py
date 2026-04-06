from faster_whisper import WhisperModel

model = WhisperModel("base", compute_type="int8")  # lightweight

def transcribe_audio(file_path: str) -> str:
    segments, _ = model.transcribe(file_path)

    text = ""
    for segment in segments:
        text += segment.text + " "

    return text.strip()