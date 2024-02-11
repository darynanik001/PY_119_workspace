from queue import LifoQueue, Queue
from typing import Any


class MyStack(LifoQueue):
    def get_from_stack(self, e: Any):
        """Searches and returns first found element e from a stack"""
        temp_stack = LifoQueue(maxsize=self.maxsize)
        exists = False

        while not self.empty():
            temp_stack.put(self.get())

        while not temp_stack.empty():
            element = temp_stack.get()

            if element != e or element == e and exists:
                self.put(element)
            else:
                exists = True

        if not exists:
            raise ValueError(f"Element {e} does not exist.")

        return e


class MyQueue(Queue):

    def get_from_queue(self, e: Any):
        temp_queue = Queue(maxsize=self.maxsize)
        exists = False

        while not self.empty():
            temp_queue.put(self.get())

        while not temp_queue.empty():
            element = temp_queue.get()

            if element != e or element == e and exists:
                self.put(element)
            else:
                exists = True

        if not exists:
            raise ValueError(f"Element {e} does not exist.")

        return e


if __name__ == "__main__":
    print("==========Stack=========")
    my_stack = MyStack()
    my_stack.put(4)
    my_stack.put(5)
    my_stack.put(7)
    my_stack.put(4)
    my_stack.put(12)
    my_stack.get_from_stack(12)

    print("==========Queue=========")
    my_queue = MyQueue()
    my_queue.put(4)
    my_queue.put(5)
    my_queue.put(7)
    my_queue.put(4)
    my_queue.put(12)
    my_queue.get_from_queue(5)
    print(my_queue.get())  # 4
    print(my_queue.get())  # 7
    print(my_queue.get())  # 4
