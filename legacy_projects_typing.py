import numpy as np


def create_array() -> np.ndarray:
    return np.array([1, 2, 3, 4])


def array_sum(arr: np.ndarray) -> float:
    return np.sum(arr)


if __name__ == "__main__":
    arr = create_array()
    print(f"Array: {arr}")
    print(f"Sum: {array_sum(arr)}")
