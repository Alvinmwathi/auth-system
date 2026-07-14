from app.security.hashing import hash_password, verify_password

password = "MyPassword123!"

hashed = hash_password(password)

print(f"Password: {password}")
print(f"Hashed: {hashed}")

print("\nTesting Correct Password:")
print(verify_password("MyPassword123!", hashed))

print("\nTesting Wrong Password:")
print(verify_password("WrongPassword", hashed))