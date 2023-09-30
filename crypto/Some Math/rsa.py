#!/usr/bin/python3

import gmpy
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import sympy

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')
    
def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')

#flag = b'flag{s0m30n3_uS3d_w34k_k4yS_f0r_RSA}'
flags = [b'flag{s0m30n3', b'_uS3d_w34k_k', b'4yS_f0r_RSA}']
ciphertext = []

p = getPrime(48) 
q = getPrime(48)
n = p*q
phi = (p - 1)*(q - 1)
e = 65537
d = pow(e,-1,phi)

print('P: '+ str(p))
print('Q: '+ str(q))
print('N: '+ str(n))
print('PHI: '+ str(phi))
print('E: '+ str(e))
print('D: '+ str(d))

for i in flags:
    ciphertext.append(pow(int_from_bytes(i),e,n))

pubkey = RSA.construct((int(n), int(e)))
privkey = RSA.construct((int(n), int(e), int(d), int(p), int(q)))

with open('pubkey.pem', 'w') as f:
	pKey = pubkey.exportKey().decode('utf-8')
	f.write(pKey)

with open('privkey.pem', 'w') as w:
	pKey = privkey.exportKey().decode('utf-8')
	w.write(pKey)

with open('flag.enc','w') as g:
	for i in range(len(ciphertext)):
		g.write('c'+str(i)+' = '+str(ciphertext[i])+'\n')

#pbf = open('privkey.pem', 'r').read()
#key = RSA.importKey(pbf)
