from typeguard import typechecked


# Example 1: Basic usage
@typechecked
def greet(name: str) -> str:
    return f"Hello, {name}!"


# This will work fine
print(greet("Alice"))

# This will raise a TypeError
# print(greet(123))

# Example 2: More complex types
from typing import List, Dict, Generator


@typechecked
def process_data(data: List[Dict[str, int]]) -> int:
    return sum(item['value'] for item in data)


# This will work fine
print(process_data([{'value': 1}, {'value': 2}, {'value': 3}]))


# This will raise a TypeError
# print(process_data([{'value': 'not an int'}]))

# Example 3: Using with classes
class Person:
    @typechecked
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def celebrate_birthday(self) -> None:
        self.age += 1


# This will work fine
person = Person("Bob", 30)
person.celebrate_birthday()


# This will raise a TypeError
# wrong_person = Person(123, "thirty")

# Example 4: Using with generator functions
@typechecked
def countdown(start: int) -> Generator[int, None, None]:
    while start > 0:
        yield start
        start -= 1


# This will work fine
for num in countdown(5):
    print(num)

# This will raise a TypeError
# for num in countdown("5"):
#     print(num)
