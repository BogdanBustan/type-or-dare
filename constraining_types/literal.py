from typing import Literal

# Example 1: Direction type
def move(direction: Literal["up", "down", "left", "right"]) -> str:
    return f"Moving {direction}"

print(move("up"))     # OK
print(move("down"))   # OK
print(move("top"))  # Type error!

# Example 2: Status codes
def get_status(code: Literal[200, 404, 500]) -> str:
    status = {
        200: "OK",
        404: "Not Found",
        500: "Server Error"
    }
    return status[code]

print(get_status(200))  # Output: "OK"
print(get_status(302))  # Type error!