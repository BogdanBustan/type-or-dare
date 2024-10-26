from typing import TypeVar, Generic, List, Dict, Optional
from dataclasses import dataclass

# Basic Generic with both syntaxes
# -----------------------------------------

# Type variable declaration
T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')


# Old syntax (pre-Python 3.12)
class Box(Generic[T]):
    def __init__(self, item: T) -> None:
        self.item = item

    def get(self) -> T:
        return self.item


# New syntax (Python 3.12+)
class BoxNew[T]:
    def __init__(self, item: T) -> None:
        self.item = item

    def get(self) -> T:
        return self.item


# Usage is the same for both
string_box = Box[str]("Hello")
int_box = Box[int](42)


# Generic with Multiple Type Parameters
# -----------------------------------------

# Old syntax
class Pair(Generic[K, V]):
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value


# New syntax
class PairNew[K, V]:
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value


# Generic with Constraints
# -----------------------------------------
from typing import Sequence
from numbers import Number

# Constrained TypeVar
NumericT = TypeVar('NumericT', bound=Number)


# Old syntax
class Statistics(Generic[NumericT]):
    def __init__(self, data: Sequence[NumericT]):
        self.data = data

    def average(self) -> float:
        return sum(self.data) / len(self.data)


# New syntax
class StatisticsNew[NumericT: Number]:
    def __init__(self, data: Sequence[NumericT]):
        self.data = data

    def average(self) -> float:
        return sum(self.data) / len(self.data)


# Generic with Dataclasses
# -----------------------------------------

# Old syntax
@dataclass
class Container(Generic[T]):
    value: T
    metadata: Dict[str, str]


# New syntax
@dataclass
class ContainerNew[T]:
    value: T
    metadata: Dict[str, str]


# Generic Functions
# -----------------------------------------

# Old syntax
def first_element(lst: List[T]) -> Optional[T]:
    return lst[0] if lst else None


# New syntax
def first_element[T](lst: List[T]) -> Optional[T]:
    return lst[0] if lst else None


# More Complex Example: Generic Stack
# -----------------------------------------

# Old syntax
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> Optional[T]:
        return self._items.pop() if self._items else None

    def peek(self) -> Optional[T]:
        return self._items[-1] if self._items else None


# New syntax
class StackNew[T]:
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> Optional[T]:
        return self._items.pop() if self._items else None

    def peek(self) -> Optional[T]:
        return self._items[-1] if self._items else None


# Usage examples
def demonstrate_usage():
    # Using Stack
    int_stack = Stack[int]()
    int_stack.push(1)
    int_stack.push(2)

    str_stack = Stack[str]()
    str_stack.push("hello")
    str_stack.push("world")

    # Using Container
    int_container = Container[int](42, {"created": "today"})
    str_container = Container[str]("hello", {"language": "English"})

    # Using Pair
    name_age_pair = Pair[str, int]("Alice", 30)

    # Using Statistics
    stats = Statistics[float]([1.0, 2.0, 3.0, 4.0])
    avg = stats.average()

demonstrate_usage()