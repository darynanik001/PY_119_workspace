from functools import reduce


def favourite_movie(name=""):
    """Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
    The function should then print "My favorite movie is named {name}"."""
    print(f"My favorite movie is named {name}")


def make_country(country_name="", capital=""):
    country_info = {
        "country_name": country_name,
        "capital": capital
    }
    print("Country: {0}, Capital: {1}".format(*country_info.values()))


def make_operation(operator, *args):
    """Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
    (to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) as the second parameter.
     Then return the sum or product of all the numbers in the arbitrary parameter."""
    if len(args) > 0:
        res = 0
        if operator == '+':
            res = reduce(lambda x, y: x + y, args)
        elif operator == '-':
            res = reduce(lambda x, y: x - y, args)
        elif operator == '*':
            res = reduce(lambda x, y: x * y, args)

        return res
    return 0


if __name__ == '__main__':
    favourite_movie("Prestige")
    make_country("Ukraine", "Kyiv")
    print(make_operation('+', 7, 7, 2))
    print(make_operation('-', 5, 5, -10, -20))
    print(make_operation('*', 7, 6))
