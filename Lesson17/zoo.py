

class Animal:

    @staticmethod
    def talk():
        print(f"I am an Animal.")


class Dog(Animal):
    @staticmethod
    def talk():
        print(f"I am an Dog.")


class Cat(Animal):
    @staticmethod
    def talk():
        print(f"I am an Cat.")


def animal_talk(animal: Animal):
    animal.talk()


if __name__ == "__main__":
    base_animal = Animal()
    cat = Cat()
    dog = Dog()
    animals = [base_animal, cat, dog]

    for animal in animals:
        animal_talk(animal)