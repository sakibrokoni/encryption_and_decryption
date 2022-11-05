import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = input("Enter the Password: ") 
password = password_provided.encode()  
salt = b'salt_'  
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))  
input_file = 'test.encrypted'
output_file = 'test.jpg'

with open(input_file, 'rb') as f:
    data = f.read() 

fernet = Fernet(key)
try:
    decrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(decrypted) 
except InvalidToken as e:
    print("Invalid Key - Unsuccessfully decrypted")