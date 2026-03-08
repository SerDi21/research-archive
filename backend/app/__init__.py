from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate
from .config import Config
from .errors.handlers import register_error_handlers
from app.utils.logging import configure_logging

def create_app(config_class=Config):
    app = Flask(__name__)
    configure_logging()
    app.config.from_object(config_class)

    CORS(app, origins=["http://localhost:5173"])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .routes.publications import publications_bp
    app.register_blueprint(publications_bp)

    # Register error handlers
    register_error_handlers(app)

    @app.route("/")
    def health_check():
        return {"status": "ok"}, 200

    return app