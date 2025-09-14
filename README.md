# 🧠 AI-ccess

**AI-powered accessibility microservice** that adapts user interfaces, interprets voice commands, generates image captions, and personalizes experiences for users with diverse needs.

---

## Features

- **Voice Command Interpretation**  
  Uses transformer-based NLP to classify spoken commands and trigger UI actions like theme switching, layout changes, and navigation.

- **Image Captioning**  
  Generates alt text for uploaded images using deep learning models to support screen readers and improve content accessibility.

---

## 🏗️ Project Structure

```
AI-CCESS/
├── flask_frontend/         # Flask-based UI
│   ├── app.py              # Frontend logic
│   ├── templates/          # HTML templates
│   └── static/             # CSS/JS assets
├── models/                 # ML models
│   ├── caption_model.py    # Image captioning
│   └── nlp_model.py        # Voice intent classification
├── services/               # Core microservices
│   ├── accessibility.py    # UI adaptation logic
│   ├── captioning.py       # Caption generation
│   └── feedback.py         # Feedback handling
├── schemas.py              # Data schemas
├── main.py                 # FastAPI backend
├── requirements.txt        # Dependencies
└── README.md               # You're reading it!
```

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/AliceYangAC/AI-ccess.git
cd AI-ccess
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv\Scripts\activate.ps1 # on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI backend

```bash
uvicorn main:app --reload
```

### 5. Run the Flask frontend

```bash
cd flask_frontend
python app.py
```

---

## Demo Pages

- `/` – Landing page
- `/captioning` – Upload images for caption generation
- `/voice` – Voice-controlled dashboard with layout adaptation
- `/ui-adapt` – Manually test UI adaptation logic (WIP)

---

## Powered By

- [Transformers](https://huggingface.co/transformers/) for NLP
- [FastAPI](https://fastapi.tiangolo.com/) for backend services
- [Flask](https://flask.palletsprojects.com/) for frontend
- [Bootstrap](https://getbootstrap.com/) for styling

---

## 📌 Future Enhancements

### Priority

- **UI Adaptation Engine**  
  Dynamically adjusts layout, font size, contrast, and navigation mode based on user preferences or detected accessibility needs.

- **Accessibility Detection**  
  Analyzes user settings (e.g., zoom level, screen reader usage) to infer accessibility requirements and adapt the interface accordingly.

- **Feedback Collection**  
  Captures user feedback to refine personalization and improve accessibility recommendations over time.

### Other Ideas

- Fine-tuned intent classifier for accessibility-specific commands
- Cloud-based speech-to-text integration (e.g., Whisper, Azure Speech)
- Multilingual voice support

---

## 📄 License

MIT License. See `LICENSE` file for details.
