from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ValidationError
from rest_framework.filters import BaseFilterBackend
from rest_framework.response import Response

from movies import custom_permissions

from .models import CustomUser, Movie, Review
from .serializers import (MovieSerializer, RegistrationSerializer,
                          ReviewSerializer)


class ListCreateMovieAPI(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (custom_permissions.PostPermissions,)

    def get_queryset(self):
        year = self.request.query_params.get('year', None)
        if year is not None:
            self.queryset.filter(year=year)
        else:
            return self.queryset.all()

    # class FilterBackend(BaseFilterBackend):
    #     def filter_queryset(self, request, queryset, view):
    #         return queryset.filter(**view.filter_params)
    #
    # filter_backends = (FilterBackend,)
    #
    # # @validate_exists(from_='GET', params=('year',))
    # # @validate_values(from='_GET', params={'year': lambda value: value in range(1, 2020 + 1)})
    # def list(self, request, *args, **kwargs):
    #     self.validate(request)
    #     return super().list(request, *args, **kwargs)
    #
    # def validate(self, request, *args, **kwargs):
    #     # TODO:
    #     self.filter_params = {}
    #
    #     if 'year' in request.GET:
    #         try:
    #             year = int(request.GET['year'])
    #         except ValueError:
    #             pass
    #         else:
    #             if year in range(1, 2020 + 1):
    #                 self.filter_params['year'] = request.GET['year']
    #                 return
    #
    #         raise ValidationError(detail='Error')


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
        user_comment = self.queryset.filter(movie_id=self.kwargs.get('movie_pk'), user_id=self.request.user.pk)
        if user_comment:
            raise ValueError('you cannot post more than one review')
        else:
            movie = get_object_or_404(Movie, pk=self.kwargs.get('movie_pk'))
            serializer.save(movie=movie)


class SingleReviewAPiView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (custom_permissions.PostPermissions,)

    def get_queryset(self):
        return self.queryset.filter(movie_id=self.kwargs.get('movie_pk'), pk=self.kwargs.get('pk'))  # TODO:optimize it


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
