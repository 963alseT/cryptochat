from encryption import fernet_encrypt
from cryptography.fernet import Fernet

key = Fernet.generate_key()

msg = "Hello World"
cipher = fernet_encrypt(msg, key)

print(cipher)
