from typing import Any, List


def bad_process(x: Any) -> object:
    """
    BAD: Using Any for input allows unsafe operations,
    while object for output is too restrictive for callers
    """
    # Dangerous! We assume x has .upper() without checking
    return x.upper()  # This could crash!


def good_process(x: object) -> Any:
    """
    GOOD: object for input forces us to be careful,
    Any for output lets callers handle the result flexibly
    """
    # We must explicitly check before doing operations
    if isinstance(x, str):
        return x.upper()
    elif isinstance(x, (int, float)):
        return str(x)
    else:
        return str(x)


# Example usage showing why this is better
def process_items(items: List[object]) -> List[Any]:
    results = []

    for item in items:
        # Using 'object' forces us to be defensive in our code
        if isinstance(item, str):
            # We must prove to the type checker that operations are safe
            results.append(item.upper())
        elif isinstance(item, (int, float)):
            results.append(item * 2)  # type: ignore[arg-type]
        else:
            # Fallback for unknown types
            results.append(str(item))

    return results


# This is how callers should handle Any return types
def use_results(results: List[Any]) -> None:
    for result in results:
        # Caller's responsibility to check types before using
        if isinstance(result, str):
            print(f"String: {result}")
        elif isinstance(result, (int, float)):
            print(f"Number: {result}")
        else:
            print(f"Other: {str(result)}")


# Example usage
def main() -> None:
    items = ["hello", 42, 3.14, True]

    # Good pattern
    results = process_items(items)
    use_results(results)

    # Demonstrates why the good pattern is safer
    try:
        # This could crash because Any input doesn't force type checking
        bad_result = bad_process(42)  # Will raise AttributeError
    except AttributeError:
        print("Bad process crashed!")

    # This is safer because object input forces us to handle types
    good_result = good_process(42)
    print(f"Good process succeeded: {good_result}")


if __name__ == "__main__":
    main()
