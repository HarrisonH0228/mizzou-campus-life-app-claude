from flask import Blueprint, render_template
from helpers.data_loader import load_json

map_bp = Blueprint("map", __name__)


@map_bp.route("/map")
def campus_map():
    """Render the interactive campus map page with landmark data."""
    data = load_json("map.json")
    return render_template("map.html", data=data)
