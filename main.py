from signing import sign_message
from verification import verify_message

while True:
    signed_message = sign_message(input("> "))
    verify_message(signed_message)