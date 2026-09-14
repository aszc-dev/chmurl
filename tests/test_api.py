import pytest
from rest_framework.test import APIClient

from urlapi.models import Url
from urlapi.shortener import shorten

TEST_URLS = [
    (address, shorten(address))
    for address in [
        "https://chmurkopedia.szkolawchmurze.org/pl/articles/11042977-podstawowe-informacje-o-platformie",
        "https://www.django-rest-framework.org/api-guide/requests/#standard-httprequest-attributes",
    ]
]


@pytest.fixture(scope="session")
def client():
    return APIClient()


@pytest.mark.django_db
@pytest.mark.parametrize("address,alias", TEST_URLS)
def test_get_redirects_correctly(address, alias, client: APIClient):
    Url(alias=alias, address=address).save()

    response = client.get(f"/{alias}/")

    assert response.status_code == 302
    assert response["Location"] == address


@pytest.mark.django_db
@pytest.mark.parametrize("address,alias", TEST_URLS)
def test_post_creates(address, alias, client: APIClient):
    data = {"address": address}

    response = client.post("/", data)

    assert response.status_code == 201
    assert response.json()["address"] == address
    assert response.json()["alias"] == alias


@pytest.mark.django_db
def test_post_second_time(client: APIClient):
    address = "https://szkolawchmurze.org/"
    data = {"address": address}

    _ = client.post("/", data)
    _ = client.post("/", data)
    response = client.post("/", data)

    assert response.status_code == 200
    assert response.json()["address"] == address
    assert response.json()["alias"] == shorten(address)
    assert len(Url.objects.all()) == 1
