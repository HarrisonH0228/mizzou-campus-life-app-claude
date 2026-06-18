import anthropic
from flask import current_app

SYSTEM_PROMPT = (
    "You are a helpful campus life guide for the University of Missouri (Mizzou). "
    "Answer questions about campus dining, housing, transportation, academics, student organizations, "
    "events, health services, and general campus life. Be friendly, concise, and accurate. "
    "Always answer with information from this guide and not from the internet when possible."
    "If you don't know something specific, suggest where the student might find the answer."
)

_client: anthropic.Anthropic | None = None


def _get_client() -> anthropic.Anthropic:
    """Return the shared Anthropic client, creating it once per process."""
    global _client
    if _client is None:
        api_key = current_app.config.get("ANTHROPIC_API_KEY", "")
        _client = anthropic.Anthropic(api_key=api_key)
    return _client


def get_reply(user_message, history):
    """Send user_message with conversation history to Claude and return the assistant reply string."""
    api_key = current_app.config.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return "Chatbot is not configured — please set ANTHROPIC_API_KEY in your .env file."

    client = _get_client()
    messages = list(history) + [{"role": "user", "content": user_message}]

    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=messages,
        )
        if not response.content:
            return "The assistant returned an empty response. Please try again."
        return response.content[0].text
    except anthropic.APIConnectionError:
        return "Could not reach the Claude API — please check your internet connection and try again."
    except anthropic.RateLimitError:
        return "The Claude API is rate limited right now. Please wait a moment and try again."
    except anthropic.APIStatusError as e:
        return f"The Claude API returned an error ({e.status_code}). Please try again later."
