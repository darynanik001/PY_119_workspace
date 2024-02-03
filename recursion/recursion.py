#############################################
# All tasks should be solved using recursion
#############################################


from typing import Optional


def to_power(x: Optional[int | float], exp: int) -> Optional[int | float]:
    """
    Returns  x ^ exp
    Examples:
        to_power(2, 3) == 8 -> True
        to_power(3.5, 2) == 12.25 -> True
        to_power(2, -1) -> ValueError: This function works only with exp > 0.
    """
    if exp <= 0:
        raise ValueError("This function works only with exp > 0.")

    if exp == 1:
        return x

    return x * to_power(x, exp - 1)


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    """
    Checks if input string is Palindrome
    Examples:
        is_palindrome('mom') -> True
        is_palindrome('sassas') -> True
        is_palindrome('o') -> True
    """
    if index >= len(looking_str):  # "" palindrom as well
        return True
    if looking_str[len(looking_str) - 1] != looking_str[index]:
        return False
    index += 1
    return is_palindrome(looking_str[index: len(looking_str)], index)


def mult(a: int, n: int) -> int:
    """
    This function works only with positive integers
    Examples:
        mult(2, 4) == 8 -> True
        mult(2, 0) == 0 -> True
        mult(2, -4) -> ValueError("This function works only with positive integers")

    """
    if n < 0:
        raise ValueError("This function works only with positive integers")
    if n == 0:
        return 0
    elif n == 1:
        return a

    return a + mult(a, n - 1)


def reverse(input_str: str) -> str:
    """
    Function returns reversed input string
    Examples:
        reverse("hello") == "olleh" -> True
        reverse("o") == "o" -> True
    """

    if len(input_str) <= 1:
        return input_str

    res = reverse(input_str[1:]) + input_str[0]
    return res


def sum_of_digits(digit_string: str) -> int:
    """
    Examples:
        sum_of_digits('26') == 8 -> True
        sum_of_digits('278') == 17 -> True
        sum_of_digits('test') -> ValueError("input string must be digit string")
    """
    if digit_string.isalpha():
        raise ValueError("input string must be digit string")

    number = int(digit_string)
    if number // 10 == 0:
        return number

    return sum_of_digits(str(number // 10)) + int(digit_string) % 10


if __name__ == "__main__":
    # 1
    assert to_power(2, 3) == 8
    assert to_power(3.5, 2) == 12.25

    # 3
    assert mult(2, 4) == 8
    assert mult(2, 0) == 0

    print(is_palindrome("mom"))
    print(is_palindrome("sassas"))
    print(is_palindrome("o"))
    print(is_palindrome("hello"))
    print(is_palindrome(""))

    assert reverse("hello") == "olleh"
    assert reverse("o") == "o"

    #sum_of_digits("test")
    print(sum_of_digits("26"))
    print(sum_of_digits("278"))
    print(sum_of_digits("45678"))
