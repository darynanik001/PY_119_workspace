import random


def generate_random_list(a, b, size):
    nums = []
    temp_size = size
    while temp_size > 0:
        nums.append(random.randint(a, b))
        temp_size -= 1

    print(f"Random {size} numbers: {nums}")
    return nums


def get_greatest_number():
    """Task 1
       Write a Python program to get the largest number from a list of random numbers with the length of 10
       Constraints: use only while loop and random module to generate numbers"""
    nums = generate_random_list(-100, 100, 10)
    max_num = nums[0]
    index = 0
    nums_generated = 10

    while index < nums_generated:
        max_num = nums[index] if nums[index] > max_num else max_num
        index += 1

    return max_num


def get_exclusive_common_numbers_list():
    """Task 2
    Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing
    the common integers between the 2 initial lists without any duplicates.
    Constraints: use only while loop and random module to generate numbers"""
    l1 = generate_random_list(1, 10, 10)
    l2 = generate_random_list(1, 10, 10)
    l3 = list(set(l1) & set(l2))

    return l3


def extracting_numbers():
    """Task 3
       Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
       but not a multiple of 5, and store them in a separate list. Finally, print the list.
       Constraint: use only while loop for iteration"""
    my_list = []
    counter = 1

    while counter <= 100:
        my_list.append(counter)
        counter += 1

    result = []
    i = 0

    while i < 100:
        if my_list[i] % 7 == 0 and my_list[i] % 5 != 0:
            result.append(my_list[i])
        i += 1

    print(f"Extracted numbers: {result}")


if __name__ == '__main__':
    print(f"Max number: {get_greatest_number()}")
    print(f"Exclusive common numbers list: {get_exclusive_common_numbers_list()}")
    extracting_numbers()
