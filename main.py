from signing import sign_message
from verification import verify_message

while True:
    signature, message = sign_message(input("> "))
    verify_message(signature, message.encode())