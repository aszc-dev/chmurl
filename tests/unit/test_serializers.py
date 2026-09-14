import pytest

from urlapi.serializers import UrlSerializer


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
    assert len(serializer.data["id"]) == 4
