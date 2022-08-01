import crypt
import hashlib
import base64
import random
import Cryptodome.Cipher.AES
from Cryptodome.Cipher import AES
import os
from hashlib import sha256
from ftplib import FTP

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

text = 'HomeWork'

key = hashlib.sha256(b'123').digest()
text = pad(text)
#iv = Random.new().read(BS)
cipher = AES.new(key, AES.MODE_CBC)
crypt_text = (cipher.encrypt(text.encode()))
print('\nCipher:', crypt_text.hex())


