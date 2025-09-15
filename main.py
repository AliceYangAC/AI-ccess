# FastAPI app
from fastapi import FastAPI, UploadFile, File, Request
from services import accessibility, captioning, feedback
from models.nlp_model import interpret_command
from schemas import CaptionRequest  # Import your schema
app = FastAPI()

@app.post("/detect-accessibility")
async def detect_accessibility(request: Request):
    data = await request.json()
    return accessibility.detect(data)
@app.post("/generate-caption")
async def generate_caption(file: UploadFile = File(...)):
    return await captioning.generate(file)
@app.post("/feedback")
async def collect_feedback(request: Request):
    data = await request.json()
    return feedback.store(data)
