# from typing import List

def greet(name):  # type: (str) -> str
    return 'Hello, ' + name


from collections import namedtuple

# Mypy type definition for a Point
Point = namedtuple('Point', ['x', 'y'])  # type: (float, float)


def distance(p1, p2):  # type: (Point, Point) -> float
    """Calculate the distance between two points."""
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def midpoint(p1, p2):  # type: (Point, Point) -> Point
    """Calculate the midpoint between two points."""
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)


# def process_names(names):  # type: (List[str]) -> List[str]
#     result = []
#     for name in names:
#         result.append(name.upper())
#     return result


print(greet(1))
# print(process_names(["abc", "def"]))
