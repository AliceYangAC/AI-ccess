# main.py

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import logging

app = FastAPI(title="AI-ccess Gateway")

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Microservice URLs (adjust ports if needed)
CAPTIONING_URL = "http://localhost:8001"
VOICE_INTENT_URL = "http://localhost:8002"

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Route: Image Captioning
@app.post("/caption")
async def caption_image(file: UploadFile = File(...)):
    try:
        files = {"file": (file.filename, await file.read(), file.content_type)}
        response = requests.post(f"{CAPTIONING_URL}/caption", files=files)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Captioning error: {e}")
        raise HTTPException(status_code=500, detail="Captioning service failed")

# Route: Voice Intent Classification
@app.post("/voice-intent")
def classify_voice(command: str = Form(...)):
    try:
        payload = {"text": command}
        response = requests.post(f"{VOICE_INTENT_URL}/classify", json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Voice intent error: {e}")
        raise HTTPException(status_code=500, detail="Voice intent service failed")
