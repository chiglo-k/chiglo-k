import hashlib
import base64
from Cryptodome.Cipher import AES
import os

key = hashlib.sha3_256('123').digest()
text = 'ТестовыйБрут'
key_hash = AES.new(key, AES.MODE_CBC, )
