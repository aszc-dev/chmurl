from binascii import crc32

import base62


def shorten(long_text: str) -> str:
    data = bytes(long_text, "utf-8")
    checksum = crc32(data)
    encoded = base62.encode(checksum)
    return str(encoded)
