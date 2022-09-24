import bcrypt
import hashlib

password = b"learningisfun"
salt = bcrypt.gensalt(14)
hash = bcrypt.hashpw(password, salt)
print(salt)
print(hash)

print(bcrypt.checkpw(password, hashed_password= b'$2b$14$EFOxm3q8UWH8ZzK1h.WTZeRcPyr8/X0vRfuL3/e9z7AKIMnocurBG'))
