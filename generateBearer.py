import secrets
import string
import pyperclip

def generate_bearer_token(length=32):
    token_chars = string.ascii_letters + string.digits + '-._~+/='
    random_string = ''.join(secrets.choice(token_chars) for _ in range(length))
    return "Bearer " + random_string

# Generate random bearer token
random_token = generate_bearer_token()

# Copy token to clipboard
pyperclip.copy(random_token)
print(f"{random_token} has been copied to the clipboard.")
