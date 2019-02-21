#The following code generates a new RSA key pair (secret) and saves it into a file,
# protected by a password.
from Crypto.PublicKey import RSA

secret_code = "Unguessable"
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                              protection="scryptAndAES128-CBC")

file_out = open("rsa_key.bin", "wb")
file_out.write(encrypted_key)
file_out.close()
print(key.publickey().export_key())

#The following code reads the private RSA key back in,
# and then prints again the public key:

#secret_code = "Unguessable"
encoded_key = open("rsa_key.bin", "rb").read()
key = RSA.import_key(encoded_key, passphrase=secret_code)
print(key.export_key())
print(key.publickey().export_key())

print(key.size_in_bytes(), 'Bytes =', key.size_in_bits(), 'bits')
print(key.publickey().size_in_bytes(), 'Bytes =', key.publickey().size_in_bits(), 'bits')