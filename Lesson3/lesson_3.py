def task_1(string: str):
    if len(string) < 2:
        return ""
    return string[:2] + string[-2:]


def task_2(string: str):
    if string.isdigit() and len(string) == 10:
        return True
    return False


def task_3():
    while True:
        answer = input("23 + 15? ")

        try:
            if int(answer) == 23 + 15:
                print("That's correct! 23 + 15 = {23+15}.")
            else:
                print("Sorry you answer is incorrect. Please try again.")
        except ValueError:
            print("Please enter a number.")


def task_4():
    my_name = "daryna"

    if input("Enter your name: ").lower() == my_name:
        print("Exists. Successfully logged in.")
    else:
        print("This name does not exist.")


if __name__ == '__main__':
    sample_1 = "helloworld"
    sample_2 = "my"
    sample_3 = "x"
    print(task_1(sample_3))

    print(task_2("0979965586"))

    task_3()

    task_4()
