from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView

from urlapi.models import Url
from urlapi.serializers import UrlSerializer


class UrlView(APIView):
    def get(self, _, short_url: str) -> HttpResponse:
        url = get_object_or_404(Url, alias=short_url)
        return HttpResponseRedirect(redirect_to=url.address)

    def post(self, request: Request) -> HttpResponse:
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            _ = serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
