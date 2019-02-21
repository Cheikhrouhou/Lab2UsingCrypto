#The following code generates a new RSA key pair (secret) and saves it into a file,
# protected by a password.
#using DER format
from Crypto.PublicKey import RSA


key = RSA.generate(2048)

#write the private key in file
file_out = open("privkey.der", "wb")
file_out.write(key.export_key('DER'))
file_out.close()


#write the public key in file
file_out = open("pubkey.der", "wb")
file_out.write(key.publickey().export_key('DER'))
file_out.close()

print('Private key size is ', key.size_in_bytes(), 'Bytes =', key.size_in_bits(), 'bits')
print(key.export_key())
print('Public key size is ', key.publickey().size_in_bytes(), 'Bytes =', key.publickey().size_in_bits(), 'bits')
print(key.publickey().export_key())