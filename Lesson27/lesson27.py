from typing import Optional


class Category:
    def __init__(self, name: str, parent: Optional["Category"] = None):
        self.name = name
        self._children = []
        self._parent = parent
        if self.parent is not None:
            self._parent._children.append(self)

    def __str__(self):
        return self.name

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children

    def add(self, category_tree) -> None:
        self._children.append(category_tree)

    def remove(self):
        if self._parent is None:
            self.name = None
        else:
            self._parent._children.remove(self)


def print_tree(category: Category, ident: int = 0):
    if category.name is None:
        raise ValueError(f"No category found")
    print('--' * ident, category)
    for child in category.children:
        print_tree(child, ident + 1)


if __name__ == '__main__':
    strings = Category("strings", parent=None)
    beats = Category("beats", parent=None)
    guitars = Category("guitars", parent=strings)
    violins = Category("violins", parent=strings)
    acoustics = Category("acoustics", parent=guitars)
    electrics = Category("electrics", parent=guitars)
    fenders = Category("fenders", parent=electrics)
    gibsons = Category("gibsons", parent=electrics)
    #acoustics.remove()
    print_tree(strings)
    drums = Category("drums", parent=electrics)
    # acoustics = Category("acoustics", parent=guitars)
    # electrics = Category("electrics", parent=guitars)
    # alt = Category("alt", parent=violins)
    # fenders = Category("fenders", parent=electrics)
    # gibsons = Category("gibsons", parent=electrics)
    # beats = Category("beats", parent=strings)
    # drums = Category("drums", parent=beats)
    # #print_tree(strings, 1)
    #
    piano = Category("piano", parent=None)
    keys = Category("keys", parent=piano)
    metronome = Category("metronome", parent=piano)
    drums.add(piano)
    print("Adding piano subtree")
    print_tree(strings, 1)