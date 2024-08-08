from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def des_decrypt(ciphertext, key):
    cipher = DES.new(base64.b64decode(key), DES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(base64.b64decode(ciphertext)), DES.block_size)
    return decrypted.decode('utf-8')
