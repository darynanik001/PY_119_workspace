import random


def generate_random_id(a, b):
    return random.randint(a, b)


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.__id = id_

        self.name = name

        self.company = company

        self.__workers = set()

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, worker):
        if not isinstance(worker, Worker):
            raise TypeError("Not a valid worker. Instance must have type Worker")

        self.__workers.add(worker)

    @property
    def id(self):
        return self.__id


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.__id = id_

        self.name = name

        self.company = company

        self.__boss = boss

    @property
    def id(self) -> int:
        return self.__id

    @property
    def boss(self) -> Boss:
        return self.__boss

    @boss.setter
    def boss(self, boss: Boss) -> None:
        if not isinstance(boss, Boss):
            raise TypeError("Not a valid boss. Instance must have type Boss")
        self.__boss = boss


if __name__ == "__main__":
    boss1 = Boss(
        id_=generate_random_id(1, 100),
        name="Piotr",
        company="Intel"
    )

    boss2 = Boss(
        id_=generate_random_id(1, 100),
        name="Adam",
        company="Apple"
    )

    worker1 = Worker(
        id_=generate_random_id(1, 100),
        name="Alina",
        company="Intel",
        boss=boss1
    )

    worker2 = Worker(
        id_=generate_random_id(1, 100),
        name="Karina",
        company="Intel",
        boss=boss1
    )

    boss1.workers = worker1
    boss1.workers = worker2
    boss1.workers = worker2

    print(boss1.workers)
