word = "CAESAR"
key = "P"


def caesar_cipher(word: str, key: str) -> str:
    secret = ""
    if key.isupper():
        shift_value = (ord(key) - 65) % 26
    else:
        shift_value = (ord(key) - 97) % 26

    for i in range(len(word)):
        letter = word[i]

        if letter.isupper():
            letter = chr((ord(letter) - 65 + shift_value) % 26 + 65)
        elif letter.islower():
            letter = chr((ord(letter) - 97 + shift_value) % 26 + 97)
        secret += letter
    return secret


if __name__ == "__main__":
    print(caesar_cipher(word, key))
