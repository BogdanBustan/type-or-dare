# Lists
numbers: list[int] = [1, 2, 3]
mixed_list: list[int | str] = [1, "two", 3]

# Dictionaries
user_ages: dict[str, int] = {"Alice": 25, "Bob": 30}
nested_dict: dict[str, dict[str, int]] = {
    "team1": {"Alice": 25, "Bob": 30},
    "team2": {"Charlie": 35, "David": 28}
}

# Sets
unique_numbers: set[int] = {1, 2, 3}

# Tuples
# Fixed size with specific types
coordinate: tuple[int, int] = (10, 20)
# Variable size tuples
numbers_tuple: tuple[int, ...] = (1, 2, 3, 4)
