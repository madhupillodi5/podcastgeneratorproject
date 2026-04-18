import secrets

print("JWT_SECRET =", secrets.token_hex(32))
print("FLASK_SECRET_KEY =", secrets.token_hex(24))