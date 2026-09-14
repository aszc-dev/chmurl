import pytest
from pytest_django import Settings


@pytest.fixture
def fixed_settings(settings: Settings):
    settings.SQIDS_ALPHABET = "abdefghjkpqstuvwxyzADEFGHJKLMNPRSTUVWXYZ2345679"
    settings.SQIDS_MIN_LENGTH = 4

    return settings
