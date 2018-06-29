
# 33 bytes of random data, base64 encoded:
#
#     dd if=/dev/urandom bs=33 count=1 |base64
#

import sys
import jwt
import base64
import binascii

#secret_b64 = "0sOtJuYnq5sMhTFUb7+5xRGlNE5q/WLcSmIGpZgxxo+i55/q84EehU1wR9rn0/ZmqA0QeJQ94DK7Q8O6JGP1lq5c"
secret_b64 = "c4hXGswhxX6yGxFHm1vIzVzcMubste/kPjE6Z4QiVirp"

secret = base64.b64decode(secret_b64)

print("SECRET(b64): {}".format(secret_b64))
print("SECRET(hex): {}".format(binascii.b2a_hex(secret).decode()))

token = sys.argv[1]
print("TOKEN: {}".format(token))

def decode(label, token, secret):
    print("Decoding with {} secret...".format(label))
    try:
        jwt.decode(token, secret)
        print("=> Success!")
    except Exception as err:
        print("=> ERROR: {}".format(err))

decode("base64", token, secret_b64)
decode("binary", token, secret)
