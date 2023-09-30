import json
from base64 import b64encode,b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

data = b"flag{d3cRyp7_4_m3$$ag3_eNcRyPT3d_w1Th_AES_CBC}"
#key = get_random_bytes(16)
key = b"try_decrypt_text"
iv = b'\x00'*16
print(iv)
cipher = AES.new(key, AES.MODE_CBC, iv)
ct_bytes = cipher.encrypt(pad(data, AES.block_size))
#iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
iv= b64encode(iv).decode('utf-8')
print(iv)
result = json.dumps({'iv':iv, 'ciphertext':ct})
print(result)

test = "CBC{0}".format(ct)
print(test)

json_input = result

try:
    b64 = json.loads(json_input)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    print("The message was: ", pt)
except (ValueError, KeyError):
    print("Incorrect decryption")

# Ciphertext: CBC8I+e2bKiafRwAvYtD+g6F6Esl29bImEEVjm7Cq613M7QXrag41lUV+YjoxYG5+Co
# Key: try_decrypt_text