import timeit

def old_camel_to_snake(name: str) -> str:
    result = []
    for i, char in enumerate(name):
        if char.isupper() and i > 0:
            result.append("_")
        result.append(char.lower())
    return "".join(result)

def old_snake_to_camel(name: str) -> str:
    components = name.split("_")
    return components[0] + "".join(x.title() for x in components[1:])

import re
_camel_to_snake_re = re.compile(r'(?<!^)(?=[A-Z])')

def new_camel_to_snake(name: str) -> str:
    if name.islower():
        return name
    return _camel_to_snake_re.sub("_", name).lower()

def new_snake_to_camel(name: str) -> str:
    if "_" not in name:
        return name
    components = name.split("_")
    return components[0] + "".join([x.title() for x in components[1:]])

print("old_camel_to_snake:", timeit.timeit("old_camel_to_snake('thisIsATestOfCamelToSnake')", globals=globals(), number=100000))
print("new_camel_to_snake:", timeit.timeit("new_camel_to_snake('thisIsATestOfCamelToSnake')", globals=globals(), number=100000))

print("old_snake_to_camel:", timeit.timeit("old_snake_to_camel('this_is_a_test_of_snake_to_camel')", globals=globals(), number=100000))
print("new_snake_to_camel:", timeit.timeit("new_snake_to_camel('this_is_a_test_of_snake_to_camel')", globals=globals(), number=100000))

# Also test fast path
print("old_camel_to_snake fast:", timeit.timeit("old_camel_to_snake('already_snake_case')", globals=globals(), number=100000))
print("new_camel_to_snake fast:", timeit.timeit("new_camel_to_snake('already_snake_case')", globals=globals(), number=100000))

print("old_snake_to_camel fast:", timeit.timeit("old_snake_to_camel('alreadyCamelCase')", globals=globals(), number=100000))
print("new_snake_to_camel fast:", timeit.timeit("new_snake_to_camel('alreadyCamelCase')", globals=globals(), number=100000))
