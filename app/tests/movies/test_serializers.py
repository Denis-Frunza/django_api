from movies.serializers import MovieSerializer, ReviewSerializer


def test_valid_serializer():
    valid_serializer_data = {
        "title": "Raiders of the Lost Ark",
        "genre": "Action",
        "year": "1981",
    }
    serializer = MovieSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data


def test_invalid_movie_serializer():
    invalid_serializer_data = {
        "title": "Raiders of the Lost Ark",
        "genre": "Action",
    }
    serializer = MovieSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"year": ["This field is required."]}


# def test_invalid_rate_range_serializer():
#     invalid_serializer_data = {
#         "user": 1,
#         "movies": 4,
#         "comment": "test",
#         "rating": 6,
#     }
#     serializer = ReviewSerializer(data=invalid_serializer_data)
#     assert not serializer.is_valid()
#     assert serializer.validated_data == {}
#     assert serializer.data == invalid_serializer_data
#     print(serializer.errors)
#     assert serializer.errors == {"year": ["This field is required."]}
