from flask import Blueprint, render_template, request, jsonify
from helpers.claude_client import get_reply

chatbot_bp = Blueprint("chatbot", __name__)


@chatbot_bp.route("/chatbot")
def chatbot_page():
    """Render the full-page chatbot UI."""
    return render_template("chatbot.html")


@chatbot_bp.route("/chat", methods=["POST"])
def chat():
    """Accept a JSON payload with message + history, return Claude's reply."""
    body = request.get_json(silent=True)
    if not body or "message" not in body:
        return jsonify({"error": "Missing 'message' field."}), 400

    user_message = body["message"].strip()
    history = body.get("history", [])

    if not user_message:
        return jsonify({"error": "Message cannot be empty."}), 400

    reply = get_reply(user_message, history)
    return jsonify({"reply": reply})
