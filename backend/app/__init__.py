from flask import Flask
from .extensions import db, migrate
from .config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import Publication

    @app.route("/")
    def health_check():
        return {"status": "ok"}, 200

    return app