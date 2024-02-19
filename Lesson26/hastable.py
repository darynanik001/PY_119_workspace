from typing import Any


class HashTableExample:

    def __init__(self):
        self.storage = [
            None, None, None, None, None,
            None, None, None, None, None,
        ]
        self._size = 0

    def add(self, item: Any):
        hash_value = self.get_hash(item)  # 0..9
        if self.storage[hash_value] is None:
            self.storage[hash_value] = item
        else:
            self.storage[hash_value] = [
                self.storage[hash_value],
                item,
            ]
        self._size += 1

    def find(self, item: Any) -> bool:
        hash_value = self.get_hash(item)  # 0..9
        if isinstance(self.storage[hash_value], list):
            return item in self.storage[hash_value]

        return self.storage[hash_value] == item

    @classmethod
    def get_hash(cls, item: Any) -> int:  # 0..9
        return len(str(item)) % 10

    def __len__(self) -> int:
        return self._size

    def __contains__(self, item: Any) -> bool:
        hash_value = self.get_hash(item)
        value = self.storage[hash_value]

        def _contains(data: Any) -> bool:
            if data is not None and item == data:
                return True
            if isinstance(data, list):
                for d in data:
                    if _contains(d):
                        return True

        return _contains(value)


if __name__ == "__main__":
    hte = HashTableExample()
    print(hte.storage)
    print(hte.find("Gimli"))  # None

    print("===")
    print(len(hte))
    hte.add("Aragorn")
    hte.add("Gimli")
    hte.add("Frodo")
    hte.add("Kamil")
    # print(len(hte))
    # print(hte.find("Gimli"))  # None

    print("Aragorn" in hte)
    print("Gimli" in hte)
    print("Frodo" in hte)
    print(None in hte)
    print("Kamil" in hte)
    print("None" in hte)