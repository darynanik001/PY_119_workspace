import random


def guessing_game():
    """Task 1"""
    number_to_guess = random.randint(1, 10)

    while True:
        user_input = input("Guess number: ")
        try:
            num = int(user_input)
            if num == number_to_guess:
                print(f"You nailed it! {num} is a guessing number.")
                break
            elif num < number_to_guess:
                print(f"You entered: {num}. Your number is less than a guessing number. Please try again.")
            else:
                print(f"You entered: {num}. Your number is greater than a guessing number. Please try again.")
        except ValueError:
            print("Please enter a number.")


def birthday_greeting(name: str, age: int):
    """Task 2"""
    print(f"Hello {name}, on your next birthday you’ll be {age + 1} years")


def words_combination():
    """Words combinations using random module"""
    word = input("Enter word: ")
    combinations = ""
    size = len(word)
    words_count = 0

    while words_count != 5:
        chars = ""
        for _ in range(size):
            rand_index = random.randint(0, size - 1)
            chars += word[rand_index]
        combinations += f"{chars}, "
        words_count += 1
    combinations = combinations[:-2]

    print(f"Possible 5 combinations: {combinations}")


if __name__ == '__main__':
    # guessing_game()
    birthday_greeting("Daryna", 22)
    words_combination()
