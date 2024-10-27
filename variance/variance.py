from typing import Any, List, TypeVar, Generic

# Covariant type variable (out parameter)
T_co = TypeVar('T_co', covariant=True)
# Contravariant type variable (in parameter)
T_contra = TypeVar('T_contra', contravariant=True)


class Producer(Generic[T_co]):
    """
    Covariant producer - can return more specific types
    Dog -> Animal is allowed (output)
    """

    def __init__(self, value: T_co):
        self._value = value

    def get(self) -> T_co:
        return self._value


class Consumer(Generic[T_contra]):
    """
    Contravariant consumer - can accept more general types
    Animal -> Dog is allowed (input)
    """

    def process(self, value: T_contra) -> None:
        print(f"Processing {value}")


# Example class hierarchy
class Animal:
    def make_sound(self) -> str:
        return "Some sound"


class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof"


# Robustness principle example
def robust_function(input_obj: object) -> Any:
    """
    Conservative with inputs (object - accepts only basic operations)
    Liberal with outputs (Any - caller handles return flexibly)
    """
    if isinstance(input_obj, str):
        return input_obj.upper()
    elif isinstance(input_obj, (int, float)):
        return input_obj * 2
    else:
        return str(input_obj)


# Demonstrates covariance with return types
def process_animals() -> List[Animal]:
    # This is OK - Dogs are Animals (covariant)
    return [Dog(), Dog()]


# Demonstrates contravariance with parameter types
def feed_dogs(animals: List[Animal]) -> None:
    # This is OK - can handle any Animal (contravariant)
    for animal in animals:
        print(f"Feeding {animal.__class__.__name__}")


def demonstrate_variance() -> None:
    # Covariance example (outputs)
    dog_producer: Producer[Dog] = Producer(Dog())
    animal_producer: Producer[Animal] = dog_producer  # OK - covariant

    # Contravariance example (inputs)
    animal_consumer: Consumer[Animal] = Consumer[Animal]()
    dog_consumer: Consumer[Dog] = animal_consumer  # OK - contravariant

    # Robustness principle in action
    result = robust_function("test")  # Input must be valid object
    if isinstance(result, str):  # Output must be checked
        print(result.lower())


if __name__ == "__main__":
    demonstrate_variance()
