import json
import random

MAX_ATTEMPTS = 6


def get_content(path: str):
    data = []
    with open(path) as f:
        data.extend(json.load(f))
    return data


def get_random_word(data: list):
    return random.choice(data)


def generate_pattern(user_input: str, random_word: str):
    # Hello
    # lllll
    # ..!!.

    # Hello
    # llolo
    # ?..!!

    user_letters = list(user_input)
    word_letters = list(random_word)

    for i in range(len(word_letters)):
        if word_letters[i] == user_input[i]:
            user_letters[i] = "!"
            word_letters[i] = False

    for i, letter in enumerate(user_letters):
        if letter != "!":
            if word_letters[i] and letter in word_letters:
                user_letters[i] = "?"
                word_letters[word_letters.index(letter)] = False
            else:
                user_letters[i] = "."
    return "".join(user_letters)


if __name__ == "__main__":
    path = "C:\python-course\Game\words.json"
    content = get_content(path)
    secret = "Hello"

    while MAX_ATTEMPTS > 0:

        user_input = input("Enter word: ")

        if len(user_input) != 5 and user_input.isascii():
            print("Please try once again. You should enter 5 letters")
            continue

        if secret.lower() == user_input.lower():
            print(f"You nailed it! Guessing word {secret}")
            break

        MAX_ATTEMPTS -= 1
        print(f"Wrong word. Try once again. You have {MAX_ATTEMPTS} attempts\nHint: ")
        print(secret)
        print(generate_pattern(user_input, secret))
    else:
        print(f"You failed. Guessing word was {secret}")
