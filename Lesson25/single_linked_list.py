class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data) -> bool:
        new_node = Node(data)
        current_node = self.head
        if not self.head:
            self.head = new_node
        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        self.size += 1
        return True

    def prepend(self, data) -> bool:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        return True

    def insert_at_index(self, data, index) -> bool:
        if index == 0:
            self.prepend(data)
            self.size += 1
            return True

        if index == self.size:
            self.append(data)
            self.size += 1
            return True

        if 0 < index < self.size:
            new_node = Node(data)
            current_node = self.head
            curr_index = 0
            while current_node:
                if curr_index == index - 1:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    self.size += 1
                    return True
                current_node = current_node.next
                curr_index += 1
        return False

    def delete_at_index(self, index):
        if index == 0:
            return self.remove_start()
        if index == self.size - 1:
            return self.remove_end()
        if 0 < index < self.size - 1:
            current_node = self.head
            curr_index = 0
            while current_node:
                if index - 1 == curr_index:
                    popped = current_node.next.data
                    current_node.next = current_node.next.next
                    self.size -= 1
                    return popped
                current_node = current_node.next
                curr_index += 1
        return None

    def remove_end(self):
        if not self.head:
            return None
        if not self.head.next:
            popped = self.head.data
            self.size -= 1
            self.head = None
            return popped
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        popped = current_node.data
        current_node.next = None
        self.size -= 1
        return popped

    def remove_start(self):
        if not self.head:
            return None
        popped = self.head.data
        self.head = self.head.next
        self.size -= 1
        return popped

    def print_list(self):
        current_node = self.head
        if self.size > 0:
            while current_node:
                print(current_node.data)
                current_node = current_node.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(8)
    ll.append(12)
    ll.insert_at_index(13, 2)

    # ll.pop()
    ll.print_list()
    # print(f"size: {ll.size}")
    # print(ll.delete_at_index(2))
    # print("============")
    # ll.print_list()
    ll.insert_at_index(5, 6)
    print("after insertion")
    ll.print_list()

