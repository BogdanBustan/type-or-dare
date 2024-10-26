from typing import Final, Tuple

# Simple constants
MAX_ATTEMPTS: Final = 3
DEFAULT_NAME: Final[str] = "user"
ALLOWED_ROLES: Final[Tuple[str, ...]] = ("admin", "user", "guest")

def process_user(name: str = DEFAULT_NAME, attempts: int = MAX_ATTEMPTS) -> None:
    print(f"Processing {name} with {attempts} attempts")

# Usage
process_user()  # Using defaults
process_user("alice", 2)

# These would be type errors:
# MAX_ATTEMPTS = 4  # Error: can't reassign Final
# DEFAULT_NAME = "admin"  # Error: can't reassign Final
# ALLOWED_ROLES.append("manager")  # Runtime error: shouldn't modify Final list