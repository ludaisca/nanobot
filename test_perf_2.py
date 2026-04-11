import timeit

import re

# More optimal new version without regex
def new_camel_to_snake_2(name: str) -> str:
    if name.islower():
        return name
    return "".join(["_" + c.lower() if c.isupper() else c for c in name]).lstrip("_")

print("new_camel_to_snake_2:", timeit.timeit("new_camel_to_snake_2('thisIsATestOfCamelToSnake')", globals=globals(), number=100000))
