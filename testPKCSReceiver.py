#At the receiver side, decryption can be done using the private part of the RSA key:
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto import Random

key = RSA.importKey(open('privkey.der', 'rb').read())

dsize = SHA.digest_size
sentinel = Random.new().read(15+dsize)      # Let's assume that average data length is 15

cipher = PKCS1_v1_5.new(key)

#open file and extract ciphertext
ciphertext=open('ctext.txt', 'rb').read()
message = cipher.decrypt(ciphertext, sentinel)

#check if encryption is OK
digest = SHA.new(message[:-dsize]).digest()
print('Computed Digest is ', digest)
print('Received Digest is ', message[-dsize:])
if digest==message[-dsize:]:                # Note how we DO NOT look for the sentinel

    print ("Encryption was correct.")
else:
    print ("Encryption was not correct.")


print('The message after decryption is : ', message)
print('The message without digest is : ', message[:-dsize])


#save data to file
fout=open('ptext.txt', 'w')
fout.write(message[:-dsize].decode())
fout.close()