from movies.serializers import MovieSerializer


def test_valid_serializer():
    valid_serializer_data = {
        "title": "Raiders of the Lost Ark",
        "genre": "Action",
        "year": "1981"
    }
