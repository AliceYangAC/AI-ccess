# Logic for deteching/adapting UI according to user needs
# services/accessibility.py
def detect(user_data):
    needs = []
    if user_data.get("screen_reader"):
        needs.append("voice_navigation")
    if user_data.get("zoom_level", 100) > 120:
        needs.append("high_contrast")
    if user_data.get("simplified_layout"):
        needs.append("minimal_layout")
    return {"needs": needs}

def adapt(data):
    ui = data["ui_state"]
    needs = data["needs"]

    if "high_contrast" in needs:
        ui["theme"] = "dark"
    if "minimal_layout" in needs:
        ui["layout"] = "simplified"
    if "voice_navigation" in needs:
        ui["navigation_mode"] = "voice"

    return {"adapted_ui": ui}
