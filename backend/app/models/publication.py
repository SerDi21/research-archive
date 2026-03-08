from datetime import datetime
from ..extensions import db


class Publication(db.Model):
    __tablename__ = "publications"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255), nullable=False)
    abstract = db.Column(db.Text, nullable=False)

    authors = db.Column(db.String(255), nullable=False)
    keywords = db.Column(db.String(255))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    published = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    def __repr__(self):
        return f"<Publication {self.title}>"