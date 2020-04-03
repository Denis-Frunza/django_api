


| Endpoint      |      HTTPMethod      | CRUD          |                    Result                      |
| ------------- |:--------------------:| -------------:|------------------------------------------------:                                     |
|/api/v1/movies    |        GET        | READ  | get all movies                                         |
|/api/v1/movies/:id|        GET        | READ  | get a single movie                                     |
|/api/v1/movies    |        POST       |CREATE | add a movie                                            |
|/api/v1/movies/:id|        PUT        |UPDATE | update a movie                                         |
|/api/v1/movies/:id|        DELETE     |DELETE | delete a movie                                         |
|/api/v1/movies/:id/review|  GET       |READ   | get all comments for movie                             |
|/api/v1/movies/:id/review/:id|  GET   |READ   | get a comment from a list of comments to that movie    |
|/api/v1/movies/:id/review|   POST     |CREATE | add a comment                                          |
|/api/v1/registration     |   POST     |CREATE | add user                                               |

Tools and Technologies

1. Python
2. Django
3. Docker
4. Postgresql
5. Pytest
6. Django REST Framework
7. WhiteNoise
8. Gunicorn
9. Coverage.py
10. flake8
11. Black
12. isort

TODO:
- [ ] Develop a RESTful API CRUD with Python using Django, and Django REST Framework library.
- [X] Containerize Django inside a Docker container
- [X] Test a Django app with Pytest
- [X] Run unit and integration tests with code coverage inside a Docker container
- [X] Create a Custom User Model in Django
- [X] Implement an API with Django REST Framework Views and Serializers
- [ ] Configure GitLab CI for continuous integration and deployment
- [X] Deploy Django, Gunicorn to Heroku with Docker
- [ ] Document a RESTful API with Swagger/OpenAPI and Core API
- [X] Check code for any code quality issues via a linter
- [ ] Parameterize test functions and mock functionality in tests with Pytest


Info

* Current version: 1.0.1
* Last updated: March 27th, 2020
* Author: Denis Frunza