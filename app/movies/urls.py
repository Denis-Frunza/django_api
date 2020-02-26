from django.urls import path

from . import views


urlpatterns = [
    path('movies/', views.ListCreateMovieAPI.as_view()),
    path('movies/<int:pk>/', views.SingleMovieAPiView.as_view()),

]
