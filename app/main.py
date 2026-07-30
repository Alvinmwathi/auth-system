from fastapi import FastAPI
from app.schemas.user import UserRegister, UserResponse
from app.security.hashing import hash_password

app = FastAPI()

@app.post("/register", response_model=UserResponse)
def register(user: UserRegister):
    hashed_password = hash_password(user.password)

    print(f"Email: {user.email}")
    print(f"Hashed Password: {hashed_password}")

    return UserResponse(email=user.email)