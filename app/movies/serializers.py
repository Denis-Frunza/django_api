from django.core.validators import validate_email
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import CustomUser, Movie, Review


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_date",
            "updated_date",
        )


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_date",
        )

    def get_user(self, obj):
        return obj.user.username

    def validate_rating(self, value):
        if value not in range(1, 6):
            raise serializers.ValidationError('You can rate in range from 1 to 5.')

    def is_valid(self, raise_exception=False):
        request = self.context['request']
        movie_id = self.context['view']
        self.initial_data.update({'user': request.user.id,
                                  'movie': movie_id.kwargs.get('movie_pk')})
        return super().is_valid(raise_exception)


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        read_only_fields = (
            "id",
            "date_joined",
        )


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(username=email, password=password)
        if email and password:
            if validate_email(email):
                user_request = get_object_or_404(
                    CustomUser,
                    email=email,
                )
                email = user_request.email

            user = authenticate(email=email, password=password)

        attrs['user'] = user
        return attrs
