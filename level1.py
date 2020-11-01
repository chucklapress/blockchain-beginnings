import hashlib
#print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)


hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())

mystring = input('Enter String to hash: ')
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())

hash_object = hashlib.sha256(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

newstring = input('Enter string to sha256 hash: ')
new_hash_object = hashlib.sha256(newstring.encode())
print(new_hash_object.hexdigest())
