import hashlib
import base58
import codecs
import ecdsa
import secrets
from ElypticalCurve import *
from utils import Sha256, RipeMD160, calculate_checksum


def converPrivateKeyToWIF(private_key, compressed = False):
    extended = b"\xef" + private_key
    if(compressed):
        extended = extended + b"\x01"
    checksum = calculate_checksum(extended)
    WIF_private_key_not_encoded = extended + checksum
    return base58.b58encode(WIF_private_key_not_encoded)


def generateAddress(private_key):
    generating_point = Point.get_generator_point()
    integer_private_key = int.from_bytes(private_key, "big")
    public_key = (generating_point * integer_private_key).to_bytes()
    hashed_value = RipeMD160(Sha256(public_key))
    extended_address = b"\x6f" + hashed_value
    checksumed_address = extended_address + calculate_checksum(extended_address)
    return public_key, base58.b58encode(checksumed_address)


def generateKeys():
    private_key = secrets.token_bytes(32)
    WIF_private_key = converPrivateKeyToWIF(private_key)
    public_key, address = generateAddress(private_key)
    return WIF_private_key, address

print(generateKeys())