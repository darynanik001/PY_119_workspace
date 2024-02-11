from single_linked_list import LinkedList


class MyQueue(LinkedList):

    def dequeue(self):
        return self.delete_at_index(0)

    def qsize(self):
        return self.size

    def enqueue(self, value):
        return self.append(value)

    def empty(self):
        return self.size == 0


if __name__ == "__main__":
    my_queue = MyQueue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)

    my_queue.print_list()
    print("===========")
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.print_list()
    print(my_queue.qsize())