import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, jsonify
import requests
import json
from models.nlp_model import interpret_command, route_intent


app = Flask(__name__)
API_BASE = "http://localhost:8000"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/captioning", methods=["GET", "POST"])
def captioning():
    caption = None
    if request.method == "POST":
        file = request.files["image"]
        res = requests.post(f"{API_BASE}/generate-caption", files={"file": file})
        caption = res.json().get("caption")
    return render_template("captioning.html", caption=caption)

@app.route("/voice", methods=["GET"])
def voice():
    return render_template("voice.html")

@app.route("/voice-intent", methods=["POST"])
def voice_intent():
    text = request.json["command_text"]
    result = interpret_command(text)
    return jsonify(route_intent(result["intent"]))

@app.route("/ui-adapt", methods=["GET", "POST"])
def ui_adapt():
    adapted = None
    if request.method == "POST":
        ui_state = json.loads(request.form["ui_state"])
        needs = json.loads(request.form["needs"])
        res = requests.post(f"{API_BASE}/adapt-ui", json={"ui_state": ui_state, "needs": needs})
        adapted = res.json().get("adapted_ui")
    return render_template("ui_adapt.html", adapted=adapted)

if __name__ == "__main__":
    app.run(debug=True)
