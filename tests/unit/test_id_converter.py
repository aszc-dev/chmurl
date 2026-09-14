import pytest
from pytest_django import Settings

from urlapi.id_converter import decode_id, encode_id


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
