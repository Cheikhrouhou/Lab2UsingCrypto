import hashlib
m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
d=m.digest()

s=m.digest_size

b=m.block_size

print('d=', d)
print('s=', s)
print('b=', b)