from django.urls import path

from . import views

urlpatterns = [
    path("movies/", views.ListCreateMovieAPI.as_view()),
    path("movies/<int:pk>/", views.SingleMovieAPiView.as_view()),
    path("movies/<int:movie_pk>/reviews/", views.ListCreateReviewAPI.as_view()),
    path("movies/<int:movie_pk>/reviews/<int:pk>", views.SingleReviewAPiView.as_view()),
    path("login/", views.CustomAuthToken.as_view()),
    path("registration/", views.UserCreateView.as_view()),
]
