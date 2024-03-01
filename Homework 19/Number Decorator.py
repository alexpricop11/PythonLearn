def validate_numeric(func):
    def wrapper(*args, **kwargs):
        rezult = func(*args, **kwargs)
        if not isinstance(rezult, (int, float)):
            raise ValueError(f"The result of {func.__name__} must be numeric, but got {type(rezult).__name__}")
        return rezult

    return wrapper


@validate_numeric
def add_numbers(a, b):
    return a + b


@validate_numeric
def multiply_numbers(a, b):
    return a * b


try:
    result = add_numbers(3, 4)
    print(f"add_numbers result: {result}")
except ValueError as ve:
    print(f"Error: {ve}")

try:
    result = multiply_numbers(2, 'a')
    print(f"multiply_numbers result: {result}")
except ValueError as ve:
    print(f"Error: {ve}")
