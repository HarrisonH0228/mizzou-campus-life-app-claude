from flask import Flask
from config import Config
from routes.main import main_bp
from routes.categories import categories_bp
from routes.chatbot import chatbot_bp
from routes.map import map_bp


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(main_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(chatbot_bp)
    app.register_blueprint(map_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=app.config["DEBUG"])
