from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import io
from model import generate  # assuming you have this logic separated

app = FastAPI(title="Captioning Service")

@app.post("/caption")
async def caption_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        caption = generate(image)
        return {"caption": caption}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
