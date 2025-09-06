# Feedback handler
feedback_db = []
def store(data):
    feedback_db.append(data)
    return {"status": "received", "total_feedback": len(feedback_db)}
