import threading


counter = 0
rounds = 100000


class Counter(threading.Thread):

    def run(self):
        print(f"{self.name} started.")
        global counter, rounds
        for _ in range(rounds):
            counter += 1


if __name__ == "__main__":
    counter_1 = Counter()
    counter_2 = Counter()
    counter_1.start()
    counter_2.start()

    counter_1.join()
    print("conuter 1 thread finished.")
    counter_2.join()
    print("conuter 2 thread finished.")
    print(counter)
