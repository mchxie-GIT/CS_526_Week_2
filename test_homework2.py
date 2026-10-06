from problem2 import SinglyLinkedList
from problem3 import ways
from problem4 import SortedDoublyLinkedList

def test_singly():
    a = SinglyLinkedList()
    assert len(a) == 0 and not a.delete(1)
    a.append(2)
    a.prepend(1)
    a.insert(2, 3)
    a.insert(1, 2)
    assert [a.get(i) for i in range(len(a))] == [1, 2, 2, 3]
    assert a.find(2) == 1 and a.find(7) == -1
    a.update(0, 9)
    assert a.delete(2) and a.delete_at(2) == 3
    assert a.tail.value == 2
    assert a.delete_at(0) == 9 and a.delete_at(0) == 2
    assert a.head is None and a.tail is None and len(a) == 0
    for operation in (lambda: a.get(0), lambda: a.insert(-1, 4), lambda: a.delete_at(0)):
        try:
            operation()
            assert False, 'IndexError expected'
        except IndexError:
            pass


def test_stairs():
    assert [ways(i) for i in (0, 3, 4, 5, 10)] == [1, 4, 7, 13, 274]


def test_doubly():
    a = SortedDoublyLinkedList()
    assert a.total() == 0 and not a.exists(1) and not a.delete(1)
    for method in (a.median, a.sum_middle_three):
        try:
            method()
            assert False, 'ValueError expected'
        except ValueError:
            pass
    for value in (10, 4, 29, 8, 2, 15, 41):
        a.add(value)
    assert a.total() == 109 and a.sum_middle_three() == 33 and a.median() == 10
    assert a.delete(41) and a.total() == 68
    assert a.sum_middle_three() == 22 and a.median() == 9.0
    a.add(8)
    assert a.count(8) == 2 and a.count(5) == 0
    assert a.exists(15) and not a.exists(5)
    assert a.head.prev is None and a.tail.next is None
    current = a.head
    while current.next is not None:
        assert current.next.prev is current
        assert current.value <= current.next.value
        current = current.next
    assert not a.delete(999)
    while a.head is not None:
        assert a.delete(a.head.value)
    assert a.tail is None and a.size == 0


if __name__ == '__main__':
    test_singly()
    test_stairs()
    test_doubly()
    print('All tests passed.')
