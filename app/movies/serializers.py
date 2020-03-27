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

    def is_valid(self, raise_exception=False):
        request = self.context['request']
        movie_id = self.context['view']
        self.initial_data.update({'user': request.user.pk,
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
