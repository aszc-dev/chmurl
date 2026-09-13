import pytest
from rest_framework.test import APIClient

from urlapi.models import Url
from urlapi.shortener import shorten


@pytest.fixture(scope="session")
def client():
    return APIClient()


@pytest.mark.django_db
def test_get_redirects_correctly(client: APIClient):
    expected_address = "https://szkolawchmurze.org/"
    expected_alias = shorten(expected_address)
    Url(alias=expected_alias, address=expected_address).save()

    response = client.get(f"/{expected_alias}/")

    assert response.status_code == 302
    assert response["Location"] == expected_address


@pytest.mark.django_db
def test_post_creates(client: APIClient):
    data = {"address": "https://szkolawchmurze.org/"}

    response = client.post("/", data)

    assert response.status_code == 201
    assert response.json()["address"] == "https://szkolawchmurze.org/"
    assert response.json()["alias"] == shorten("https://szkolawchmurze.org/")
