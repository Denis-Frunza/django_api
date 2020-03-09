from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer


class ListCreateMovieAPI(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SingleMovieAPiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ListCreateReviewAPI(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(movie_id=self.kwargs.get('movie_pk'))

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('movie_pk'))
        serializer.save(movie=movie)


class SingleReviewAPiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            movie_id=self.kwargs.get('movie_pk'),
            pk=self.kwargs.get('review_pk'),
            )
