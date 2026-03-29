from signing import sign_message
from verification import verify_message
from keygen import get_rsa_keys, get_fernet_key
from encryption import rsa_encrypt, rsa_decrypt, fernet_encrypt, fernet_decrypt

A_private, A_public = get_rsa_keys()
B_private, B_public = get_rsa_keys()

#User A

message = input("> ").encode()
print(f"Original message: {message.decode()}")
signature = sign_message(message, A_private)
fernet_key = get_fernet_key()
ciphertext = fernet_encrypt(message, fernet_key)
print(f"Encrypted message: {ciphertext}")
encrypted_key = rsa_encrypt(fernet_key, B_public)

#User B

decrypted_key = rsa_decrypt(encrypted_key, B_private)
decrypted_message = fernet_decrypt(ciphertext, decrypted_key)
print(f"Decrypted message: {decrypted_message.decode()}")
verification = verify_message(signature, decrypted_message, A_public)
if verification == True:
    print("Signature valid")
else:
    print("Invalid signature")