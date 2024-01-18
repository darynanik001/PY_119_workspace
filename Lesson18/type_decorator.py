import functools


class TypeDecorator:
    @staticmethod
    def to_str(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)
        return wrapper

    @staticmethod
    def to_int(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return int(result)
        return wrapper

    @staticmethod
    def to_float(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return float(result)
        return wrapper


@TypeDecorator.to_str
def example_str():
    return 42


@TypeDecorator.to_int
def example_int():
    return "123"


@TypeDecorator.to_float
def example_float():
    return "3.14"


# Test the decorated functions
result_str = example_str()
result_int = example_int()
result_float = example_float()

# Print the results
print(f"Result as str: {result_str}, type: {type(result_str)}")
print(f"Result as int: {result_int}, type: {type(result_int)}")
print(f"Result as float: {result_float}, type: {type(result_float)}")
