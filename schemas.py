# schemas.py
from pydantic import BaseModel

class CaptionRequest(BaseModel):
    image_path: str
