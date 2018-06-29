
# 33 bytes of random data, base64 encoded:
#
#     dd if=/dev/urandom bs=33 count=1 |base64
#

import sys
import jwt
import base64
import binascii
import time

secret_b64 = "c4hXGswhxX6yGxFHm1vIzVzcMubste/kPjE6Z4QiVirp"
secret = base64.b64decode(secret_b64)

jwt1 = jwt.encode({"iat": int(time.time())}, secret_b64)
jwt2 = jwt.encode({"iat": int(time.time())}, secret)

print("SECRET(b64): {}".format(secret_b64))
print("SECRET(hex): {}".format(binascii.b2a_hex(secret).decode()))

print("\nTOKEN1 (base64 secret): {}".format(jwt1.decode()))
print(jwt.decode(jwt1, secret_b64))

print("\nTOKEN2 (binary secret): {}".format(jwt2.decode()))
print(jwt.decode(jwt2, secret))

