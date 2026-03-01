from app.models import Publication
from app.extensions import db
from app.search import index_publication


def get_all_publications():
    return Publication.query.all()


def get_publication(publication_id):
    return Publication.query.get_or_404(publication_id)


def create_publication(data):
    publication = Publication(**data)
    db.session.add(publication)
    db.session.commit()
    index_publication(publication)
    return publication


def update_publication(publication, data):
    for key, value in data.items():
        setattr(publication, key, value)

    db.session.commit()
    return publication


def delete_publication(publication):
    db.session.delete(publication)
    db.session.commit()