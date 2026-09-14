from rest_framework import serializers

from urlapi.id_converter import encode_id
from urlapi.models import Url


class UrlSerializer(serializers.ModelSerializer[Url]):
    created: bool = False

    class Meta:
        model = Url
        fields = "__all__"

    def to_representation(self, instance):
        return {"id": encode_id(instance.id), "address": instance.address}

    def create(self, validated_data) -> Url:
        instance, self.created = Url.objects.get_or_create(**validated_data)
        return instance
