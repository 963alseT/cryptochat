from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import utils
from signing import public_key

def verify_message(signature, message):
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
                )
        print("Signature is valid.")
    except Exception:
        print("Invalid signature")