from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
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
        serializer.is_valid(raise_exception=True)
        _ = serializer.save()
        status = HTTP_201_CREATED if serializer.created else HTTP_200_OK
        return Response(serializer.data, status=status)
