from rest_framework import serializers

from urlapi.models import Url
from urlapi.shortener import shorten


class UrlSerializer(serializers.ModelSerializer[Url]):
    class Meta:
        model = Url
        fields = "__all__"

    def create(self, validated_data) -> Url:
        alias = shorten(validated_data["address"])
        validated_data.update({"alias": alias})
        return Url.objects.create(**validated_data)
