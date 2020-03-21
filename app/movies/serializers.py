from rest_framework import serializers

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
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_date",
        )


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        read_only_fields = (
            "id",
            "date_joined",
        )
