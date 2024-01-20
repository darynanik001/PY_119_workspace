from collections.abc import Iterator, Iterable


class RangeIterator(Iterator):
    def __init__(self, start: int = 0, end: int = 0, step: int = 1):
        self.start = start
        self.end = end
        self.step = step

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration

        while self.start < self.end:
            self.start += self.step
            return self.start - self.step

    def __iter__(self):
        return self


class RangeIterable(Iterable):
    def __init__(self, start: int = 0, end: int = 0, step: int = 1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        while self.start < self.end:
            yield self.start
            self.start += self.step


if __name__ == '__main__':
    r1 = RangeIterator(3, 10, 3)

    for i in r1:
        print(i)

    print(list(range(3, 10, 3)))

    r2 = RangeIterable(3, 10, 3)
    print(list(r2))