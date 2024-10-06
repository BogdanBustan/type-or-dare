# Presentation order 1

# from __future__ import annotations  # PEP 563


def greeting(name: str) -> str:  # PEP 484
    hello: str = "Hello, "  # PEP 526
    return hello + name


def greeting_many(names: list[str]) -> list[str]:  # PEP 585
    return [greeting(name) for name in names]


def greet_or_number(value: str | int) -> str:  # PEP 604
    if isinstance(value, int):
        return f"Number: {value}"
    return greeting(value)


def weird_one(foo: print("I should not be here")) -> str:
    return "This is weird"


print("End of file")
