def test_create_publication_endpoint(client):
    response = client.post("/publications", json={
        "title": "Test",
        "abstract": "This is a sufficiently long abstract",
        "authors": "Sergio"
    })

    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Test"


def test_validation_error(client):
    response = client.post("/publications", json={
        "title": "Hi"
    })

    assert response.status_code == 400