from beartype import beartype
# from beartype.typing import List, Dict, Generator
from typing import List, Dict, Generator


# Example 1: Basic usage
@beartype
def greet(name: str) -> str:
    return f"Hello, {name}!"


# This will work fine
print(greet("Alice"))


# This will raise a BeartypeCallHintParamViolation
# print(greet(123))

# Example 2: More complex types
@beartype
def process_data(data: List[Dict[str, int]]) -> int:
    return sum(item['value'] for item in data)


# This will work fine
print(process_data([{'value': 1}, {'value': 2}, {'value': 3}]))


# This will raise a BeartypeCallHintParamViolation
# print(process_data([{'value': 'not an int'}]))

# Example 3: Using with classes
class Person:
    @beartype
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @beartype
    def celebrate_birthday(self) -> None:
        self.age += 1


# This will work fine
person = Person("Bob", 30)
person.celebrate_birthday()


# This will raise a BeartypeCallHintParamViolation
# wrong_person = Person(123, "thirty")

# Example 4: Using with generator functions
@beartype
def countdown(start: int) -> Generator[int, None, None]:
    while start > 0:
        yield start
        start -= 1


# This will work fine
for num in countdown(5):
    print(num)

# This will raise a BeartypeCallHintParamViolation
# for num in countdown("5"):
#     print(num)
