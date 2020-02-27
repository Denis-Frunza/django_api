import pytest
from movies.models import Movie

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


def test_get_single_movie_incorrect_id(client):
    response = client.get("api/v1/movies/foo")
    assert response.status_code == 404


@pytest.mark.django_db
def test_get_single_movie(client):
    movie = Movie.objects.create(title="The big Lebowski", genre="comody", year="1998")
    response = client.get(f"/api/v1/movies/{movie.id}/")
    assert response.status_code == 200
