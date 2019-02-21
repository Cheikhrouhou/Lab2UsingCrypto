from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
#RSA is part of the PKCS (public Key Cryptography Standard)

#generate the key and write in a file
key = RSA.generate (2048)
#print the public key
print ('key:', key)
print(key.publickey().export_key())

#save key in file for future use
f = open ('mykey.pem', 'wb')
f.write (key.export_key ('PEM'))
f.close ()

#use the already generated key
f = open ('mykey.pem', 'r')

#print the private key
#print(key.p) encoded_key, passphrase=secret_code
prkey = RSA.import_key(f.read ())
print(prkey.export_key())


#initialize a new cipher
cipher= PKCS1_OAEP.new(key)
#RSA.construct()
#read data
data = input ('Ener data to encrypt:')

#encrypt data

#first we need to convert data to bytes using encode() method
ciphertext: bytes
ciphertext= cipher.encrypt(data.encode())

print ('cipertext:', ciphertext)

#the decryption process
plaintext= cipher.decrypt(ciphertext)

print ('plaintext:', plaintext)