import pytest

from movies.models import Movie


@pytest.mark.django_db
def test_add_movie_invalid_json(client, authentication):
    response = client.post("/api/v1/movies/", {},
                           content_type="application/json",
                           HTTP_AUTHORIZATION=authentication,
                           )
    assert response.status_code == 400


@pytest.mark.django_db
def test_add_movie_invalid_json_keys(client, authentication):
    response = client.post(
        "/api/v1/movies/",
        {"title": "The Big Lebowski", "genre": "comedy", },
        content_type="application/json",
        HTTP_AUTHORIZATION=authentication,
    )
    assert response.status_code == 400


def test_get_single_movie_incorrect_id(client):
    response = client.get("/api/v1/movies/foo")
    assert response.status_code == 404


@pytest.mark.django_db
def test_get_single_movie(client):
    movie = Movie.objects.create(title="The big Lebowski", genre="comedy", year="1998")
    response = client.get(f"/api/v1/movies/{movie.id}/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_movie(client, authentication):
    response = client.post(
        "/api/v1/movies/",
        {"title": "The Big Lebowski", "genre": "comedy", "year": "1998", },
        content_type="application/json",
        HTTP_AUTHORIZATION=authentication
    )
    assert response.status_code == 201


@pytest.mark.django_db
def test_delete_movie(client):
    movie = Movie.objects.create(title="The big Lebowski", genre="comedy", year="1998")

    response = client.get(f"/api/v1/movies/{movie.id}/")
    assert response.status_code == 200

    response = client.delete(f"/api/v1/movies/{movie.id}/")
    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_movie_incorrect_id(client):
    response = client.get(f"/api/v1/movies/foo/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_movie(client):
    movie = Movie.objects.create(title="The big Lebowski", genre="comedy", year="1998")

    response = client.get(f"/api/v1/movies/{movie.id}/")
    assert response.status_code == 200

    client.put(
        f"/api/v1/movies/{movie.id}/",
        {"title": "The Big Lebowski", "genre": "comedy", "year": "1997", },
        content_type="application/json",
    )


@pytest.mark.django_db
def test_update_movie_incorrect_id(client):
    response = client.put("/api/v1/movies/foo/")

    assert response.status_code == 404
