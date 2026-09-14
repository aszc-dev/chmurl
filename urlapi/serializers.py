from rest_framework import serializers

from urlapi.models import Url
from urlapi.shortener import shorten


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
