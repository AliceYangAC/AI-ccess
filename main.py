# FastAPI app
from fastapi import FastAPI, UploadFile, File, Request
from services import accessibility, captioning, feedback
from models.nlp_model import interpret_command
from schemas import CaptionRequest  # 👈 Import your schema
app = FastAPI()
@app.post("/detect-accessibility")
async def detect_accessibility(request: Request):
    data = await request.json()
    return accessibility.detect(data)
@app.post("/adapt-ui")
async def adapt_ui(request: Request):
    data = await request.json()
    return accessibility.adapt(data)
@app.post("/voice-command")
async def voice_command(request: Request):
    data = await request.json()
    return interpret_command(data["command_text"])
@app.post("/generate-caption")
async def generate_caption(file: UploadFile = File(...)):
    return await captioning.generate(file)
# @app.post("/generate-caption")
# async def generate_caption(request: CaptionRequest):
#     return captioning.generate(request.dict())
# @app.post("/generate-caption")
# async def generate_caption(request: Request):
#     data = await request.json()
#     return captioning.generate(data)
@app.post("/feedback")
async def collect_feedback(request: Request):
    data = await request.json()
    return feedback.store(data)
