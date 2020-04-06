import pytest
from rest_framework.authtoken.models import Token


from movies.models import CustomUser


@pytest.fixture(scope="function")
def authentication():
    header_prefix = 'Token '
    key = 'abcd1234'
    username = 'john'
    email = 'lennon@thebeatles.com'
    password = 'password'

    user = CustomUser.objects.create_user(
        username, email, password
    )
    user.save()
    auth = header_prefix + key
    Token.objects.create(key=key, user=user)
    return auth
