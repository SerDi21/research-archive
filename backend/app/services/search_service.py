from elasticsearch import Elasticsearch
import logging

logger = logging.getLogger(__name__)

es = Elasticsearch("http://elasticsearch:9200")

INDEX_NAME = "publications"

def ensure_index():
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME)
        logger.info("Created Elasticsearch index: publications")

def index_publication(publication):
    ensure_index()

    es.index(
        index="publications",
        id=publication.id,
        document={
            "title": publication.title,
            "abstract": publication.abstract,
            "authors": publication.authors,
            "keywords": publication.keywords
        }
    )


def search_publications(query):
    logger.info(f"Searching publications with query: {query}")
    
    response = es.search(
        index="publications",
        query={
            "multi_match": {
                "query": query,
                "fields": ["title", "abstract", "authors", "keywords"]
            }
        }
    )

    return [
        {"id": hit["_id"], **hit["_source"]}
        for hit in response["hits"]["hits"]
    ]