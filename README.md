There might be a problem in pyjwt processing binary secrets, making it incompatible with other languages.

It accepts a bytes object as a secret; the assumption is this should then work without problem, but the resulting JWT is not cross language compatible (included are some tests from node.js to demonstrate).

I also tested with python-jose, but it just refuses to use a bytes object for a keys.  I don't know if the problem is in pyjwt or jsonwebtoken(node), but my guess is pyjwt.

There is a `test-1-generate-*` script for both node and python, and a `test-2-verify*` similarly.

1. Run the generate on python, and verify the jwt on python and it is okay.

2. Run the generate on node, and verify on python, it fails.

Setup with:

    pip3 install pyjwt
    npm install jsonwebtoken base-64

Output (python->python) -- this is as expected:

```
##########################################
# generate

$ python3 test-1-generate-from-pyjwt.py
SECRET(b64): c4hXGswhxX6yGxFHm1vIzVzcMubste/kPjE6Z4QiVirp
SECRET(hex): 7388571acc21c57eb21b11479b5bc8cd5cdc32e6ecb5efe43e313a678422562ae9

TOKEN1 (base64 secret): eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MzAyOTMyODd9.r3m2ZYcTUVIpkYVuyg7HcIbd1z9mU9FYfQx9T7w4PNg
{'iat': 1530293287}

TOKEN2 (binary secret): eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MzAyOTMyODd9.H6lOK_yQNthrjM3osNRMjIsHCSw8DOyLp_lffEAbXmE
{'iat': 1530293287}

##########################################
# verify using the base64 secret

$ python3 test-2-verify-from-pyjwt.py  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MzAyOTMyODd9.r3m2ZYcTUVIpkYVuyg7HcIbd1z9mU9FYfQx9T7w4PNg
SECRET(b64): c4hXGswhxX6yGxFHm1vIzVzcMubste/kPjE6Z4QiVirp
SECRET(hex): 7388571acc21c57eb21b11479b5bc8cd5cdc32e6ecb5efe43e313a678422562ae9
TOKEN: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MzAyOTMyODd9.r3m2ZYcTUVIpkYVuyg7HcIbd1z9mU9FYfQx9T7w4PNg
Decoding with base64 secret...
=> Success!
Decoding with binary secret...
=> ERROR: Signature verification failed

##########################################
# verify using the binary secret

$ python3 test-2-verify-from-pyjwt.py  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MzAyOTMyODd9.H6lOK_yQNthrjM3osNRMjIsHCSw8DOyLp_lffEAbXmE
SECRET(b64): c4hXGswhxX6yGxFHm1vIzVzcMubste/kPjE6Z4QiVirp
SECRET(hex): 7388571acc21c57eb21b11479b5bc8cd5cdc32e6ecb5efe43e313a678422562ae9
TOKEN: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MzAyOTMyODd9.H6lOK_yQNthrjM3osNRMjIsHCSw8DOyLp_lffEAbXmE
Decoding with base64 secret...
=> ERROR: Signature verification failed
Decoding with binary secret...
=> Success!
```

You can run the verify on node and it fails to verify the python jwt generated with a binary secret, even though python did verify this:

```
##########################################
# verify using the binary secret

$ node test-2-verify-from-node.js  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MzAyOTMyODd9.H6lOK_yQNthrjM3osNRMjIsHCSw8DOyLp_lffEAbXmE
SECRET(b64): c4hXGswhxX6yGxFHm1vIzVzcMubste/kPjE6Z4QiVirp
SECRET(hex): 7388571acc21c57eb21b11479b5bc8cd5cdc32e6ecb5efe43e313a678422562ae9
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MzAyOTMyODd9.H6lOK_yQNthrjM3osNRMjIsHCSw8DOyLp_lffEAbXmE
Decoding with base64 secret
=> Failure!
Decoding with binary secret
=> Failure!
```

Conversely, if you generate with node and try to verify with python it fails.

Node to node works.

