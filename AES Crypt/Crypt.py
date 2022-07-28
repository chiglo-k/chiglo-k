import crypt
import hashlib
import base64

import Cryptodome.Cipher.AES
from Cryptodome.Cipher import AES
import os

text = b'Brute'
key = b'123'
key_hash = AES.new(key, AES.MODE_CBC)
ciphertext, tag = key_hash.encrypt_and_digest(text)
print(ciphertext)
