from typing import Optional

# maybe_a_string: Optional[str] = "abcdef"  # This has a value
maybe_a_string: str = "abcdef"  # This has a value
print(maybe_a_string)

maybe_a_string = None  # This is the absence of a value
print(maybe_a_string)


def get_user_from_db(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "User 1"
    return None


user = get_user_from_db(1)
print(user.upper())

# if user:
#     print(user.upper())
# else:
#     print("User not found")