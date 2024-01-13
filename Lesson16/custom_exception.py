
class CustomException(Exception):

    def __init__(self, msg):
        with open("logs.txt", "a") as f:
            f.write(f"[ERROR][{__file__}]: {msg}\n")


if __name__ == "__main__":
    raise CustomException("Custom Exception")
