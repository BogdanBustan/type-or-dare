from typing import Union, Optional


def process_id(id_number: Union[int, str]) -> str:
    if isinstance(id_number, int):
        return f"ID-{id_number:05d}"
    return f"ID-{id_number}"


print(process_id(42))  # Output: ID-00042
print(process_id("ABC"))  # Output: ID-ABC
print(process_id(1.0))  # Output: ID-1.0


def process_age(age: int) -> int | str:
    if age < 0:
        return "Invalid age"
    if age > 120:
        return "Too old"
    return age * 365  # days lived


print(process_age(25))  # Output: 9125
print(process_age(-5))  # Output: Invalid age
print(process_age(150))  # Output: Too old


def fetch_user_score(user_id: int) -> int | None:  # Same as Optional[int]
    scores = {1: 100, 2: 85}
    return scores.get(user_id)  # Returns None if user_id not found


def format_score(score: Optional[int]) -> str:
    if score is None:
        return "No score available"
    return f"Score: {score}"


# Example usage
user1_score = fetch_user_score(1)
print(format_score(user1_score))  # Output: "Score: 100"

user3_score = fetch_user_score(3)
print(format_score(user3_score))  # Output: "No score available"


# Optional[T] is just syntactic sugar for Union[T, None]
# These are equivalent:
def example1(x: Optional[str]) -> str: ...
def example2(x: str | None) -> str: ...
