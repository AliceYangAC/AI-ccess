# Logic for deteching/adapting UI according to user needs
# services/accessibility.py
def detect(user_data):
    needs = []
    if user_data.get("screen_reader"):
        needs.append("voice_navigation")
    if user_data.get("zoom_level", 100) > 120:
        needs.append("high_contrast")
    return {"needs": needs}
def adapt(data):
    ui = data["ui_state"]
    needs = data["needs"]
    if "high_contrast" in needs:
        ui["theme"] = "dark"
    if "simplified_layout" in needs:
        ui["layout"] = "minimal"
    return {"adapted_ui": ui}