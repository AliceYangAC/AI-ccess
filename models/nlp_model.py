#FastAPI app
from transformers import pipeline
nlp = pipeline("text-classification", model="distilbert-base-uncased")
def interpret_command(text):
    result = nlp(text)
    label = result[0]["label"]
    if "navigate" in text.lower():
        return {"action": "navigate", "target": "dashboard"}
    return {"action": "unknown", "confidence": result[0]["score"]}
