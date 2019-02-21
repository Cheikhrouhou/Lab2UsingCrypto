from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

data=input('Ener data to encrypt:')

ciphertext: bytes
ciphertext, tag = cipher.encrypt_and_digest(data.encode())

print('cipertext:', ciphertext)

file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]

#decryption
nonce = cipher.nonce
cipher2 = AES.new(key, AES.MODE_EAX, nonce=nonce)
#cipher.update(nonce)

plaintext: bytes=cipher2.decrypt(ciphertext)

print('plaintext ', plaintext.decode())