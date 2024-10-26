from typing import Annotated
from dataclasses import dataclass

# Example 1: Basic value constraints
UserId = Annotated[int, "Must be positive"]
Age = Annotated[int, "Must be between 0 and 120"]

def register_user(user_id: UserId, age: Age) -> str:
    return f"Registered user {user_id} with age {age}"

# Example 2: Multiple metadata items
Password = Annotated[str, "Min 8 chars", "Must have number", "Must have uppercase"]

def change_password(new_password: Password) -> None:
    print(f"Password changed to {new_password}")

# Example 3: With custom validation metadata
@dataclass
class MinLength:
    min_length: int

Username = Annotated[str, MinLength(3)]

def create_user(username: Username) -> str:
    return f"Created user {username}"

# Example 4: Combining with other type hints
from typing import List
Vector = Annotated[List[float], "3D coordinate"]

def move_object(position: Vector) -> None:
    print(f"Moving to {position}")