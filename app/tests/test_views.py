import pytest


@pytest.mark.django_db
def test_add_movie_invalid_json(client):
    response = client.post(
        "/api/v1/movies/",
        {},
        content_type="application/json"
    )
    assert response.status_code == 400

@pytest.mark.django_db
def test_add_movie_invalid_json_keys(client):
    response = client.post(
        "/api/v1/movies/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
        },
        content_type="application/json"
    )
