import timeit

import re

# Let's compare the regex with list comprehension again, but what about map?
_camel_to_snake_re = re.compile(r'(?<!^)(?=[A-Z])')
def new_camel_to_snake_regex(name: str) -> str:
    if name.islower():
        return name
    return _camel_to_snake_re.sub("_", name).lower()

print("regex:", timeit.timeit("new_camel_to_snake_regex('thisIsATestOfCamelToSnake')", globals=globals(), number=100000))
print("list_comp:", timeit.timeit("''.join(['_' + c.lower() if c.isupper() else c for c in 'thisIsATestOfCamelToSnake']).lstrip('_')", globals=globals(), number=100000))
