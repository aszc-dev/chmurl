import pytest
from pytest_django import Settings

from urlapi.serializers import UrlSerializer, decode_id, encode_id


@pytest.fixture
def fixed_settings(settings: Settings):
    settings.SQIDS_ALPHABET = "abdefghjkpqstuvwxyzADEFGHJKLMNPRSTUVWXYZ2345679"
    settings.SQIDS_MIN_LENGTH = 4

    return settings


def test_encode_id(fixed_settings: Settings):
    url_id = 3
    expected = "ygGg"

    encoded = encode_id(url_id)

    assert type(encoded) is str
    assert len(encoded) == 4
    assert encoded == expected


def test_decode_id(fixed_settings: Settings):
    encoded_id = "ygGg"
    expected = 3

    decoded = decode_id(encoded_id)

    assert decoded == expected


@pytest.mark.django_db
def test_serializer_converts():
    serializer = UrlSerializer(
        data={
            "address": "https://sqids.org/playground#alphabet=abdefghjkpqstuvwxyzADEFGHJKLMNPRSTUVWXYZ2345679&minLength=4&customBlocklist=&defaultBlocklist=true&tab=table&tabTZN=false&tabTCN=false&tabTMN=false&encodeInput=1%2C+2%2C+3&decodeInput="
        }
    )

    serializer.is_valid()
    url = serializer.save()

    assert url.id == 1  # stored id is still an int
    assert type(serializer.data["id"]) is str
    assert len(serializer.data) == 4
