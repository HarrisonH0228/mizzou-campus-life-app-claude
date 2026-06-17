import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def load_json(filename):
    """Load and return parsed JSON from data/<filename>. Raises FileNotFoundError if missing."""
    path = os.path.join(DATA_DIR, filename)
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Data file not found: {filename}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
