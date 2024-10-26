from functools import singledispatch
from datetime import datetime, date


@singledispatch
def format_data(arg):
    """Default handler for unknown types"""
    return f"Don't know how to handle type: {type(arg)}"


@format_data.register
def _(text: str):
    """Handler for string type"""
    return f"String (length {len(text)}): {text.upper()}"


@format_data.register
def _(number: int):
    """Handler for integer type"""
    return f"Integer: {number:+d}"  # Shows + for positive numbers


@format_data.register
def _(number: float):
    """Handler for float type"""
    return f"Float: {number:.2f}"


@format_data.register
def _(data: list):
    """Handler for list type"""
    return f"List with {len(data)} items: {', '.join(str(x) for x in data)}"


@format_data.register
def _(dt: datetime):
    """Handler for datetime type"""
    return f"DateTime: {dt.strftime('%Y-%m-%d %H:%M:%S')}"


@format_data.register
def _(d: date):
    """Handler for date type"""
    return f"Date: {d.strftime('%Y-%m-%d')}"


# Example usage
def demonstrate_format_data():
    # Test with different types
    test_cases = [
        "hello",
        42,
        3.14159,
        [1, 2, 3],
        datetime.now(),
        date.today(),
        complex(1, 2)  # Will use default handler
    ]

    print("Demonstrating single dispatch:\n")
    for item in test_cases:
        print(format_data(item))


if __name__ == "__main__":
    demonstrate_format_data()
