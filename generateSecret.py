import secrets
import pyperclip


def generate_session_secret(length=32):
    return secrets.token_hex(length)


session_secret = generate_session_secret()

pyperclip.copy(session_secret)
print(f"{session_secret} has been copied to the clipboard.")
