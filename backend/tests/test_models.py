from app.models import Publication
from app.extensions import db


def test_create_publication(app):
    publication = Publication(
        title="Test",
        abstract="Long enough abstract for testing",
        authors="Sergio"
    )

    db.session.add(publication)
    db.session.commit()

    assert publication.id is not None
    assert publication.published is False