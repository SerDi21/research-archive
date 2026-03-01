from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.search import search_publications

from app.schemas import PublicationSchema
from app.services.publication_service import (
    get_all_publications,
    get_publication,
    create_publication,
    update_publication,
    delete_publication
)

publications_bp = Blueprint("publications", __name__)
schema = PublicationSchema()
many_schema = PublicationSchema(many=True)

@publications_bp.route("/search")
def search():
    query = request.args.get("q")
    if not query:
        return {"error": "Missing query parameter"}, 400

    results = search_publications(query)
    return {"results": results}, 200

@publications_bp.route("/publications", methods=["GET"])
def list_publications():
    publications = get_all_publications()
    return many_schema.dump(publications), 200


@publications_bp.route("/publications/<int:publication_id>", methods=["GET"])
def retrieve_publication(publication_id):
    publication = get_publication(publication_id)
    return schema.dump(publication), 200


@publications_bp.route("/publications", methods=["POST"])
def create():
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return {"errors": err.messages}, 400

    publication = create_publication(data)
    return schema.dump(publication), 201


@publications_bp.route("/publications/<int:publication_id>", methods=["PUT"])
def update(publication_id):
    publication = get_publication(publication_id)

    try:
        data = schema.load(request.json, partial=True)
    except ValidationError as err:
        return {"errors": err.messages}, 400

    publication = update_publication(publication, data)
    return schema.dump(publication), 200


@publications_bp.route("/publications/<int:publication_id>", methods=["DELETE"])
def delete(publication_id):
    publication = get_publication(publication_id)
    delete_publication(publication)
    return "", 204