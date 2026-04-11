import timeit

def camel_to_snake(name: str) -> str:
    """Convert camelCase to snake_case."""
    # Fast path for already snake_case or simple strings
    if name.islower():
        return name

    result = []
    for i, char in enumerate(name):
        if char.isupper() and i > 0:
            result.append("_")
        result.append(char.lower())
    return "".join(result)


def new_camel_to_snake_2(name: str) -> str:
    if name.islower():
        return name
    return "".join(["_" + c.lower() if c.isupper() else c for c in name]).lstrip("_")

print("original_fast:", timeit.timeit("camel_to_snake('thisIsATestOfCamelToSnake')", globals=globals(), number=100000))
print("new_camel_to_snake_2:", timeit.timeit("new_camel_to_snake_2('thisIsATestOfCamelToSnake')", globals=globals(), number=100000))
