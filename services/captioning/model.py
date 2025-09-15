from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import io 
from fastapi import UploadFile
import logging

logger = logging.getLogger(__name__)

# Load model and processor once
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

async def generate(file: UploadFile) -> dict:
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        inputs = processor(images=image, return_tensors="pt")

        with torch.no_grad():
            out = model.generate(**inputs)
            caption = processor.decode(out[0], skip_special_tokens=True)

        return {"caption": caption}
    except Exception as e:
        logger.exception("Caption generation failed")
        return {"error": str(e)}