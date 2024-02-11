from queue import LifoQueue


def task_1(string: str):
    """Program that reads in a sequence of characters and prints them in reverse order, using your implementation of
    Stack."""
    st = LifoQueue(maxsize=len(string))

    for char in string:
        st.put(char)

    while not st.empty():
        print(st.get(), end="")


def task_2(string: str):
    """Program that reads in a sequence of characters, and determines whether it's parentheses,
    braces, and curly brackets are balanced."""
    stack = LifoQueue()
    if len(string) > 0:
        for char in string:
            if char in "({[":
                stack.put(char)

            if char == "]" and stack.get() != "[":
                return False

            if char == ")" and stack.get() != "(":
                return False

            if char == "}" and stack.get() != "{":
                return False

    if not stack.empty():
        return False
    return True


if __name__ == "__main__":
    task_1("Hello")
    print("\n")
    print(task_2("{([])}"))  # -> True
    print(task_2("{(]](}"))  # -> False
    print(task_2(""))  # -> True
    print(task_2("{(["))  # -> False
