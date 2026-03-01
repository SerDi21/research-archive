from elasticsearch import Elasticsearch

es = Elasticsearch("http://elasticsearch:9200")


def index_publication(publication):
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
    response = es.search(
        index="publications",
        query={
            "multi_match": {
                "query": query,
                "fields": ["title", "abstract", "authors", "keywords"]
            }
        }
    )

    return [hit["_source"] for hit in response["hits"]["hits"]]