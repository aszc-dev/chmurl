from django.conf import settings
from sqids import Sqids

sqids_enc_dec = Sqids(
    min_length=settings.SQIDS_MIN_LENGTH, alphabet=settings.SQIDS_ALPHABET
)


def encode_id(id_int: int):
    return sqids_enc_dec.encode([id_int])


def decode_id(id_str: str):
    return sqids_enc_dec.decode(id_str)[0]
