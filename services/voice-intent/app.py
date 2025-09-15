from fastapi import FastAPI, File, UploadFile, Query
from fastapi.responses import JSONResponse
from fastapi import Body
from pydantic import BaseModel
from typing import List, Optional
from model import classify_text_batch

app = FastAPI(title="Voice Intent Service")

class CommandBatch(BaseModel):
    commands: List[str]

@app.post("/intent")
async def classify_intent(
    file: Optional[UploadFile] = File(None),
    payload: Optional[CommandBatch] = Body(None),
    threshold: float = Query(0.5, ge=0.0, le=1.0)
):
    try:
        if file:
            contents = await file.read()
            text = contents.decode("utf-8")
            lines = [line.strip() for line in text.splitlines() if line.strip()]
        elif payload:
            lines = payload.commands
        else:
            return JSONResponse(status_code=400, content={"error": "No input provided"})

        results = classify_text_batch(lines, threshold=threshold)
        return {"intents": results}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})