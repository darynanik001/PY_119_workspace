import re
import functools


def logger(func):
    """Prints a function with arguments passed to it"""

    def wrapper(*args, **kwargs):
        arguments = ", ".join(str(a) for a in args)
        print(f"{func.__name__} called with {arguments}")

    return wrapper


def stop_words(words: list):
    """Takes a list of stop words and replaces them with * inside the decorated function"""
    def stop_words_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            initial_slogan = func(*args, **kwargs)
            pattern = r"|".join([f"({stop_word})" for stop_word in words])
            return re.sub(pattern, "*", initial_slogan)

        return wrapper

    return stop_words_decorator


def arg_rules(max_length: int, type_: type, contains: list):
    """validates arguments passed to the function.
    A decorator should take 3 arguments:
    max_length: 15
    type_: str
    contains: [] - list of symbols that an argument should contain
    """
    def validate_args(func):
        @functools.wraps(func)
        def wrapper(name: str):
            if not isinstance(name, type_) or len(name) > max_length or not all(el in name for el in contains):
                return False
            return func(name)

        return wrapper

    return validate_args


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


# @stop_words(['pepsi', 'BMW'])
@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == "__main__":
    add(3, 6)
    square_all([2, 3, 4, 5, 6, 8])
    assert create_slogan('johndoe05@gmail.com') is False

    assert create_slogan('05years') is False

    assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
