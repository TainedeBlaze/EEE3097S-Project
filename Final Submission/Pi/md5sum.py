import hashlib
def file_as_bytes(file):
    with file:
        return file.read()

print (hashlib.md5(file_as_bytes(open("RSAkey.key", 'rb'))).hexdigest())
print (hashlib.md5(file_as_bytes(open("Publickey.key", 'rb'))).hexdigest())
