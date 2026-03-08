from app import create_app
from app.extensions import db
from app.models.publication import Publication
from app.services.search_service import index_publication
import time
from elasticsearch import Elasticsearch

es = Elasticsearch("http://elasticsearch:9200")

for _ in range(15):
    if es.ping():
        print("Elasticsearch ready")
        break
    print("Waiting for Elasticsearch...")
    time.sleep(2)

app = create_app()

with app.app_context():

    if Publication.query.count() > 0:
        print("Database already seeded")
        exit()

    publications = [
        Publication(
            title="Quantum Computing for Beginners",
            abstract="Introduction to quantum algorithms and qubits.",
            authors="Alice Smith",
            keywords="quantum, computing, physics",
            published=True
        ),
        Publication(
            title="Deep Learning for Particle Physics",
            abstract="Using neural networks to classify particle collisions.",
            authors="Bob Johnson",
            keywords="AI, physics, deep learning",
            published=True
        ),
        Publication(
            title="Distributed Systems in Scientific Research",
            abstract="Scalable infrastructure for large datasets.",
            authors="Carlos Martinez",
            keywords="distributed systems, computing",
            published=False
        ),
        Publication(
            title="Machine Learning in Astronomy",
            abstract="Detecting exoplanets using ML techniques.",
            authors="Diana Lee",
            keywords="astronomy, ML",
            published=True
        ),
        Publication(
            title="Data Archiving for Research Outputs",
            abstract="Strategies for long-term research data preservation.",
            authors="Eva Rossi",
            keywords="data archiving, research",
            published=False
        )
    ]

    db.session.add_all(publications)
    db.session.commit()

    for pub in publications:
        index_publication(pub)

    print("Database seeded successfully")