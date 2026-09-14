from django.conf import settings
from rest_framework import serializers
from sqids import Sqids

from urlapi.models import Url
from urlapi.shortener import shorten

sqids_enc_dec = Sqids(
    min_length=settings.SQIDS_MIN_LENGTH, alphabet=settings.SQIDS_ALPHABET
)


def encode_id(id_int: int):
    return sqids_enc_dec.encode([id_int])


def decode_id(id_str: str):
    return sqids_enc_dec.decode(id_str)[0]


class UrlSerializer(serializers.ModelSerializer[Url]):
    created: bool = False

    class Meta:
        model = Url
        fields = "__all__"

    def create(self, validated_data) -> Url:
        alias = shorten(validated_data["address"])
        validated_data.update({"alias": alias})
        instance, self.created = Url.objects.get_or_create(**validated_data)
        return instance
