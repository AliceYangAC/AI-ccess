from transformers import pipeline

classifier = pipeline("text-classification", model="distilbert-base-uncased", return_all_scores=True)

def classify_text_batch(texts, threshold=0.5):
    output = []
    for text in texts:
        scores = classifier(text)[0]
        filtered = [s for s in scores if s["score"] >= threshold]
        filtered.sort(key=lambda x: x["score"], reverse=True)
        output.append({"text": text, "intents": filtered})
    return output