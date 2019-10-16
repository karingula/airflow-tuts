from cryptography.fernet import Fernet
import os

FERNET_KEY = Fernet.generate_key().decode()
print(FERNET_KEY)
