from flask import Flask
from .extensions import db, migrate
from .config import Config
from .errors import register_error_handlers


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

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