def with_index(iterable, start=0):
    n = start
    for el in iterable:
        yield n, el
        n += 1


if __name__ == '__main__':
    ll = [x for x in range(10)]

    for i, el in with_index(ll, start=100):
        print(i, el)
