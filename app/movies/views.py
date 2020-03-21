from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from movies import custom_permissions

from .models import CustomUser, Movie, Review
from .serializers import (MovieSerializer, RegistrationSerializer,
                          ReviewSerializer)


class ListCreateMovieAPI(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (custom_permissions.PostPermissions,)


class SingleMovieAPiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ListCreateReviewAPI(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (custom_permissions.PostPermissions,)

    def get_queryset(self):
        return self.queryset.filter(movie_id=self.kwargs.get('movie_pk'))

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('movie_pk'))
        serializer.save(movie=movie)


class SingleReviewAPiView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(movie_id=self.kwargs.get('movie_pk'), pk=self.kwargs.get('review_pk'))


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class UserCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer

    # for user in CustomUser.objects.all():
    #     Token.objects.get_or_create(user=user)
