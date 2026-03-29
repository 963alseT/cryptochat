from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.fernet import Fernet

def get_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
        )
    public_key = private_key.public_key()
    return private_key, public_key

def get_fernet_key():
    key = Fernet.generate_key()
    return key