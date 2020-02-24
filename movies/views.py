from rest_framework import generics


from movies.models import Movie
from .serializers import MovieSerializer


class ListCreateMovieAPI(generics.ListCreateAPIView):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer


class SingleMovieAPiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
