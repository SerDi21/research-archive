from app.models.publication import Publication
from app.extensions import db
from app.services.search_service import index_publication
import logging

logger = logging.getLogger(__name__)

def get_all_publications():
    return Publication.query.all()


def get_publication(publication_id):
    return Publication.query.get_or_404(publication_id)


def create_publication(data):
    logger.info("Creating publication")
    publication = Publication(**data)
    db.session.add(publication)
    db.session.commit()
    index_publication(publication)
    logger.info(f"Publication created with ID {publication.id}")
    return publication


def update_publication(publication, data):
    for key, value in data.items():
        setattr(publication, key, value)

    db.session.commit()
    index_publication(publication)
    return publication


def delete_publication(publication):
    db.session.delete(publication)
    db.session.commit()