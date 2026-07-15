from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_data = {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
}

if __name__ == "__main__":
    user = User(**user_data)
    print(user)
    print(user.is_active)
