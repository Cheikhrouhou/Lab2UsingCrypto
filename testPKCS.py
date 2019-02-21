#As an example, a sender may encrypt a message in this way:

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

message = input('enter plaintext: ').encode()
h = SHA.new(message)

key = RSA.importKey(open('pubkey.der', 'rb').read())
cipher = PKCS1_v1_5.new(key)
ciphertext = cipher.encrypt(message+h.digest())

print ('cipertext:', ciphertext)