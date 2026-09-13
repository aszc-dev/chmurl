from django.db import models
from django.utils.http import MAX_URL_REDIRECT_LENGTH


class Url(models.Model):
    address: models.CharField = models.CharField(max_length=MAX_URL_REDIRECT_LENGTH)
    alias: models.CharField = models.CharField(max_length=20, blank=True)
