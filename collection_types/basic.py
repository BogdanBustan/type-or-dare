from typing import List, Dict, Set, Tuple, Union

# Lists
numbers: List[int] = [1, 2, 3]
mixed_list: List[Union[int, str]] = [1, "two", 3]

# Dictionaries
user_ages: Dict[str, int] = {"Alice": 25, "Bob": 30}
nested_dict: Dict[str, Dict[str, int]] = {
    "team1": {"Alice": 25, "Bob": 30},
    "team2": {"Charlie": 35, "David": 28}
}

# Sets
unique_numbers: Set[int] = {1, 2, 3}

# Tuples
# Fixed size with specific types
coordinate: Tuple[int, int] = (10, 20)
# Variable size tuples
numbers_tuple: Tuple[int, ...] = (1, 2, 3, 4)
