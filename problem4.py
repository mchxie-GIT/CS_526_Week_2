class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class SortedDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        elif value <= self.head.value:
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif value >= self.tail.value:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            current = self.head
            while current.value < value:
                current = current.next
            node.prev = current.prev
            node.next = current
            current.prev.next = node
            current.prev = node
        self.size += 1

    def delete(self, value):
        current = self.head
        while current is not None and current.value < value:
            current = current.next
        if current is None or current.value != value:
            return False
        if current.prev is None:
            self.head = current.next
        else:
            current.prev.next = current.next
        if current.next is None:
            self.tail = current.prev
        else:
            current.next.prev = current.prev
        self.size -= 1
        return True

    def exists(self, value):
        def search(node):
            if node is None or node.value > value:
                return False
            if node.value == value:
                return True
            return search(node.next)
        return search(self.head)

    def count(self, value):
        def count_from(node):
            if node is None or node.value > value:
                return 0
            if node.value == value:
                return 1 + count_from(node.next)
            return count_from(node.next)
        return count_from(self.head)

    def total(self):
        def add_from(node):
            if node is None:
                return 0
            return node.value + add_from(node.next)
        return add_from(self.head)

    def print_list(self):
        def print_from(node):
            if node is None:
                return ''
            if node.next is None:
                return str(node.value)
            return str(node.value) + ' <-> ' + print_from(node.next)
        print(print_from(self.head) if self.head is not None else '(empty)')

    def middle_node(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def sum_middle_three(self):
        if self.size < 3:
            raise ValueError('at least 3 nodes required')
        mid = self.size // 2
        start = mid - 1 if self.size % 2 == 1 else mid - 2
        current = self.middle_node(start)
        return current.value + current.next.value + current.next.next.value

    def median(self):
        if self.size == 0:
            raise ValueError('empty list')
        mid = self.size // 2
        if self.size % 2 == 1:
            return self.middle_node(mid).value
        left = self.middle_node(mid - 1)
        return (left.value + left.next.value) / 2


if __name__ == '__main__':
    numbers = SortedDoublyLinkedList()
    for value in [10, 4, 29, 8, 2, 15, 41]:
        numbers.add(value)
    print('Initial list:')
    numbers.print_list()
    print('total:', numbers.total())
    print('sum_middle_three:', numbers.sum_middle_three())
    print('median:', numbers.median())
    print('delete(41):', numbers.delete(41))
    numbers.print_list()
    print('total:', numbers.total())
    print('sum_middle_three:', numbers.sum_middle_three())
    print('median:', numbers.median())
    numbers.add(8)
    numbers.print_list()
    print('count(8):', numbers.count(8))
    print('count(5):', numbers.count(5))
    print('exists(15):', numbers.exists(15))
    print('exists(5):', numbers.exists(5))
