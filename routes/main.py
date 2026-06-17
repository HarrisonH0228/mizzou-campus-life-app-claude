from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    """Render the home page with category cards."""
    return render_template("index.html")


@main_bp.app_errorhandler(404)
def not_found(error):
    """Render a friendly 404 error page."""
    return render_template("error.html", code=404, message="Page not found."), 404


@main_bp.app_errorhandler(500)
def server_error(error):
    """Render a friendly 500 error page."""
    return render_template("error.html", code=500, message="Something went wrong on our end."), 500
