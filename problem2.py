class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError('index out of range')
        if index == 0:
            self.prepend(value)
        elif index == self.size:
            self.append(value)
        else:
            previous = self.head
            for i in range(index - 1):
                previous = previous.next
            node = Node(value)
            node.next = previous.next
            previous.next = node
            self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('index out of range')
        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def find(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def update(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError('index out of range')
        current = self.head
        for i in range(index):
            current = current.next
        current.value = value

    def delete(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.delete_at(0)
            return True
        previous = self.head
        while previous.next is not None:
            if previous.next.value == value:
                previous.next = previous.next.next
                if previous.next is None:
                    self.tail = previous
                self.size -= 1
                return True
            previous = previous.next
        return False

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('index out of range')
        if index == 0:
            removed = self.head
            self.head = self.head.next
            self.size -= 1
            if self.head is None:
                self.tail = None
            return removed.value
        previous = self.head
        for i in range(index - 1):
            previous = previous.next
        removed = previous.next
        previous.next = removed.next
        if previous.next is None:
            self.tail = previous
        self.size -= 1
        return removed.value

    def print_list(self):
        current = self.head
        values = []
        while current is not None:
            values.append(str(current.value))
            current = current.next
        print(' -> '.join(values) if values else '(empty)')
