import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("SECRET_KEY_HASHING")

def encrypt(data: str) -> str:
    if key is not None:
        cipher_suite = Fernet(key.encode())
        encrypted_text = cipher_suite.encrypt(data.encode('utf-8'))
        return encrypted_text.decode('utf-8')
    else:
        return "Error, key not found"

def decrypt(data: str) -> str:
    if key is not None:
        cipher_suite = Fernet(key.encode())
        encrypted_text = cipher_suite.decrypt(data.encode('utf-8'))
        return encrypted_text.decode('utf-8')
    else:
        return "Error, key not found"
