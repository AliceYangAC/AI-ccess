from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import io 

# Load model and processor once
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

async def generate(file):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        inputs = processor(images=image, return_tensors="pt")

        with torch.no_grad():
            out = model.generate(**inputs)
            caption = processor.decode(out[0], skip_special_tokens=True)

        return {"caption": caption}
    except Exception as e:
        return {"error": str(e)}
    
# Original synchronous version for reference
# def generate(media_info):
#     """
#     media_info: dict with key 'image_path' pointing to local image file
#     """
#     image_path = media_info.get("image_path")
#     if not image_path:
#         return {"error": "No image path provided"}

#     try:
#         image = Image.open(image_path).convert("RGB")
#         inputs = processor(images=image, return_tensors="pt")

#         with torch.no_grad():
#             out = model.generate(**inputs)
#             caption = processor.decode(out[0], skip_special_tokens=True)

#         return {"caption": caption}
#     except Exception as e:
#         return {"error": str(e)}
