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

FIRST_THREE_IDS = ["f2Tj", "6UVW", "ygGg"]


@pytest.fixture(scope="session")
def client():
    return APIClient()


@pytest.mark.django_db
def test_get_redirects_correctly(client: APIClient):
    for i, long_url in enumerate(TEST_URLS):
        expected_sqid = FIRST_THREE_IDS[i]
        address = long_url
        Url(address=address).save()

        response = client.get(f"/{expected_sqid}/")

        assert response.status_code == 302
        assert response["Location"] == address


@pytest.mark.django_db
@pytest.mark.parametrize("address", TEST_URLS)
def test_post_creates(address, client: APIClient):
    data = {"address": address}

    response = client.post("/", data)

    assert response.status_code == 201
    assert response.json()["address"] == address


@pytest.mark.django_db
def test_post_multiple_times(client: APIClient):
    address = "https://szkolawchmurze.org/"
    data = {"address": address}

    _ = client.post("/", data)
    _ = client.post("/", data)
    response = client.post("/", data)

    assert response.status_code == 200
    assert response.json()["address"] == address
    assert len(Url.objects.all()) == 1


@pytest.mark.django_db
def test_post_fails_non_url(client: APIClient):
    address = "not-an-actual-url"
    data = {"address": address}

    response = client.post("/", data)

    assert response.status_code == 400
