from single_linked_list import LinkedList


class Stack(LinkedList):

    def push(self, value):
        return self.append(value)

    def pop(self):
        return self.remove_end()

    def peek(self):
        if not self.empty():
            current = self.head
            while current.next:
                current = current.next
            return current.data
        return

    def empty(self):
        return self.size == 0

    def length(self):
        return self.size


if __name__ == "__main__":
    st = Stack()
    st.push(1)
    st.push(4)
    st.push(15)
    st.push(8)
    # print(st.empty())
    st.pop()
    st.pop()
    st.pop()
    st.print_list()
    print(f"Length list: {st.length()}")
    st.push(24)
    print(f"Length list: {st.length()}")
    st.print_list()