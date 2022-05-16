import pyDes
from time import time

data = input("please enter the plain text for encryption:")
keystring = input("Enter 16/24 byte string for key generation:")
k = pyDes.triple_des(keystring,padmode=pyDes.PAD_PKCS5)
e = k.encrypt(data)
print("cipher text:%r" %e)
print("plain text:%r"%k.decrypt(e))




import pyDes
from time import time

data = input("please enter the plain text for encryption:")
keystring = input("Enter 8 byte string for key generation:")
k = pyDes.des(keystring,padmode=pyDes.PAD_PKCS5)
e = k.encrypt(data)
print("cipher text:%r" %e)
print("plain text:%r"%k.decrypt(e))

