from collections.abc import Iterator


class CountDown(Iterator):
    def __init__(self, counter: int):
        self.counter = counter

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= 0:
            raise StopIteration
        else:
            self.counter -= 1
            return self.counter + 1


if __name__ == '__main__':
    counter = CountDown(10)

    for c in counter:
        print(c)
