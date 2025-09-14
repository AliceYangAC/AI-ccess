from transformers import pipeline

# Load a zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define possible intents
INTENT_LABELS = [
    "navigate",
    "change_theme",
    "adjust_layout",
    "adjust_font_size",
    "enable_accessibility_mode",
    "submit_form",
    "request_help"
]

def interpret_command(text):
    result = classifier(text, INTENT_LABELS)
    intent = result["labels"][0]
    score = result["scores"][0]
    return {"intent": intent, "confidence": score}

def route_intent(intent):
    if intent == "navigate":
        return {"action": "navigate", "target": "dashboard"}
    elif intent == "change_theme":
        return {"action": "update_ui", "theme": "dark"}  # You can expand this later
    elif intent == "adjust_layout":
        return {"action": "update_ui", "layout": "compact"}
    elif intent == "adjust_font_size":
        return {"action": "update_ui", "font_size": "large"}
    elif intent == "enable_accessibility_mode":
        return {"action": "update_ui", "accessibility_mode": "screen_reader"}
    elif intent == "submit_form":
        return {"action": "submit_form"}
    elif intent == "request_help":
        return {"action": "show_help"}
    else:
        return {"action": "unknown"}
