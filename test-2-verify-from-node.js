
const base64 = require('base-64')
const jwt = require('jsonwebtoken')

//secret_b64 = "0sOtJuYnq5sMhTFUb7+5xRGlNE5q/WLcSmIGpZgxxo+i55/q84EehU1wR9rn0/ZmqA0QeJQ94DK7Q8O6JGP1lq5c"
secret_b64 = "c4hXGswhxX6yGxFHm1vIzVzcMubste/kPjE6Z4QiVirp"
secret = base64.decode(secret_b64)

function bin2hex (bin) {
  var i = 0, l = bin.length, chr, hex = ''
  for (i; i < l; ++i) { 
    chr = bin.charCodeAt(i).toString(16) 
    hex += chr.length < 2 ? '0' + chr : chr
  }
  return hex
}

console.log("SECRET(b64): " + secret_b64)
console.log("SECRET(hex): " + bin2hex(secret))

function decode (label, token, secret) {
    console.log("Decoding with " + label + " secret")
    try {
      out = jwt.verify(token, secret)
      if (out) {
        console.log("=> Success!")
        console.log(out)
        return
      }
    } catch (err) {
      console.log("=> Failure!")
      return
    }
    console.log("=> Failure!")
}

token = process.argv[2]
console.log(token)

decode("base64", token, secret_b64)
decode("binary", token, secret)
