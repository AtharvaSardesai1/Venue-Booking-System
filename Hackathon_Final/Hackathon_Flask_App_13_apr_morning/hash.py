import bcrypt

# Hash a password
password = b"mysecretpassword"
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

# Verify a password
entered_password = b"mysecretpassword"
if bcrypt.checkpw(entered_password, hashed_password):
    print("Password match!")
else:
    print("Password does not match!")
