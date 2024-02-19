from typing import Optional


class Category:
    def __init__(self, name: str, parent: Optional["Category"] = None):
        self.name = name
        self._parent = parent
        self._children = []
        if self._parent is not None:
            self._parent._children.append(self)

    def __str__(self):
        return f"node: {self.name}, children: {self._children}"


if __name__ == "__main__":
    strings = Category(name="strings", parent=None)
    guitars = Category(name="guitars", parent=strings)
    violin = Category(name="violin", parent=strings)
    print(str(violin))
    print(str(strings))
    print(str(guitars))
