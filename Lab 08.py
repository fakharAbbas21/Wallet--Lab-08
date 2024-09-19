
import base58
import hashlib
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization


ecdse_privatekey = ec.generate_private_key(ec.SECP256K1())
ecdse_publickey = ecdse_privatekey.public_key()

publc_key_bytes = ecdse_publickey.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint
)
print(publc_key_bytes)

sha256_bytes = hashlib.sha256(publc_key_bytes).digest()
print("sha256_bytes", publc_key_bytes)

ripemd160_bytes = hashlib.new('ripemd160')
ripemd160_bytes.update(sha256_bytes)
ripemd160_bytes_digest = ripemd160_bytes.digest()

print("ripemd160_bytes_diges",ripemd160_bytes_digest)

network_bytes = b"\x00"
networks = network_bytes + ripemd160_bytes_digest
print( "network : " , networks)    
    
cheaksum_full = hashlib.sha256(hashlib.sha256(networks).digest()).digest()
cheaksum = networks[:4]

network_address = networks +cheaksum

bitcoin_address = base58.b58encode(network_address) 
bitcoin = base58.b58decode(bitcoin_address)  
print( "bitcoin_address" ,bitcoin)
    
    
    