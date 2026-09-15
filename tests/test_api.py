import pytest
from rest_framework.test import APIClient

from urlapi.models import Url

# @pytest.fixture
# def init_db(db):

TEST_URLS = [
    "https://chmurkopedia.szkolawchmurze.org/pl/articles/11042977-podstawowe-informacje-o-platformie",
    "https://www.django-rest-framework.org/api-guide/requests/#standard-httprequest-attributes",
    "https://sqids.org/playground#alphabet=abdefghjkpqstuvwxyzADEFGHJKLMNPRSTUVWXYZ2345679&minLength=4&customBlocklist=&defaultBlocklist=true&tab=table&tabTZN=false&tabTCN=false&tabTMN=false&encodeInput=1%2C+2%2C+3&decodeInput=",
]

FIRST_IDS = ["f2Tj", "6UVW", "ygGg"]


@pytest.fixture(scope="session")
def client():
    return APIClient()


@pytest.fixture
def prefilled_db(db):
    for long_url in TEST_URLS:
        address = long_url
        Url(address=address).save()


@pytest.mark.django_db
def test_get_redirects_correctly(client: APIClient, prefilled_db):
    for i, expected_sqid in enumerate(FIRST_IDS):
        response = client.get(f"/{expected_sqid}/")

        assert response.status_code == 302
        assert response["Location"] == TEST_URLS[i]


@pytest.mark.django_db
def test_post_creates(client: APIClient):
    for address in TEST_URLS:
        data = {"address": address}

        response = client.post("/", data)

        assert response.status_code == 201
        assert response.json()["address"] == address


@pytest.mark.django_db
def test_post_multiple_times(client: APIClient, prefilled_db):
    for address in TEST_URLS:
        data = {"address": address}

        response = client.post("/", data)

        assert response.status_code == 200
        assert response.json()["address"] == address
        assert len(Url.objects.all()) == len(TEST_URLS)


@pytest.mark.django_db
def test_post_fails_non_url(client: APIClient):
    for address in TEST_URLS:
        malformed = address.replace(".", "-").replace("/", "-")
        data = {"address": malformed}

        response = client.post("/", data)

        assert response.status_code == 400
