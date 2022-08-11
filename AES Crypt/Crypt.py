
# Начало шифрования
import hashlib
from Cryptodome.Cipher import AES

keyw = b'123'
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

text = 'HomeWork'

key = hashlib.sha256(keyw).digest()
text = pad(text)

cipher = AES.new(key, AES.MODE_CBC)
crypt_text = (cipher.encrypt(text.encode()))
print('\nCipher:', crypt_text.hex())
# Конец шифрования

###########
cipher_1 = crypt_text.hex()
cipher_text = bytes(cipher_1, encoding='utf16')
for new_pass in range(100, 130):
    key_b = str(new_pass)
    key = hashlib.sha256(bytes(key_b, encoding='utf16')).digest()
    BS = AES.block_size
    unpad = lambda s: s[:-ord(BS[len(s) - 1:])]
    iv = cipher_text[:BS]
    cipher_dec = AES.new(key, AES.MODE_CBC, iv)
    plain_text = (cipher_dec.decrypt(cipher_text.decode('utf16')))
    if plain_text == b'':
        continue
    print(f"\nFor key {new_pass}: {plain_text.hex()}")
###########
