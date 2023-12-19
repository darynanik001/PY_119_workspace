def oops():
    raise IndexError  # changing to KeyError will break the program


def task_1():
    try:
        oops()
    except IndexError as e:
        print("Catch IndexError")


def task_2():
    a = input("Input a: \n")
    b = input("Input b: ")

    try:
        res = int(a)**2 / int(b)
        return res
    except ZeroDivisionError as e:
        print("Cannot divide by zero")
        raise e
    except ValueError as e:
        print("Not numbers")
        raise e
    finally:
        print("task 2 executed")


if __name__ == "__main__":
    task_1()
    print(task_2())
