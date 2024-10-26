from typing import TypeVar, Protocol, Any
from dataclasses import dataclass

# ===== Old Style (Pre-3.12) =====
T = TypeVar('T', bound=float)
U = TypeVar('U')


def old_style_largest(numbers: list[T]) -> T:
    """Pre-3.12 style generic function using TypeVar"""
    return max(numbers)


# ===== New Style (3.12+) =====
def new_style_largest[T: float](numbers: list[T]) -> T:
    """Python 3.12+ style generic function using type parameters"""
    return max(numbers)


# Example with Protocol
class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...


# Generic class with multiple bounds
class SortedPair[T: Comparable, U: Comparable]:
    def __init__(self, first: T, second: U) -> None:
        self.first = first
        self.second = second

    def sort_first(self, items: list[T]) -> list[T]:
        return sorted(items)

    def sort_second(self, items: list[U]) -> list[U]:
        return sorted(items)


# Dataclass with generics
@dataclass
class Container[T]:
    value: T

    def get_value(self) -> T:
        return self.value


def main():
    # Using old style generics
    print("Old style examples:")
    result1 = old_style_largest([1.0, 2.0, 3.0])
    print(f"Largest (old style): {result1}")

    # Using new style generics
    print("\nNew style examples:")
    result2 = new_style_largest[float]([1.0, 2.0, 3.0])
    print(f"Largest (new style): {result2}")

    # Using generic class
    pair = SortedPair[int, str](42, "hello")
    sorted_nums = pair.sort_first([3, 1, 4, 1, 5])
    sorted_strs = pair.sort_second(["banana", "apple", "cherry"])
    print(f"\nSorted numbers: {sorted_nums}")
    print(f"Sorted strings: {sorted_strs}")

    # Using generic dataclass
    int_container = Container[int](42)
    str_container = Container[str]("Hello")
    print(f"\nInt container value: {int_container.get_value()}")
    print(f"String container value: {str_container.get_value()}")


if __name__ == "__main__":
    main()
