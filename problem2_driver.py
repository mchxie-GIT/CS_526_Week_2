import sys
from problem2 import SinglyLinkedList

def main():
    linked_list = SinglyLinkedList()
    arguments_needed = {
        'append': 1, 'prepend': 1, 'insert': 2,
        'get': 1, 'find': 1, 'len': 0, 'update': 2,
        'delete': 1, 'delete_at': 1, 'print_list': 0
    }
    for line in sys.stdin:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        command = parts[0]
        if command not in arguments_needed or len(parts) - 1 != arguments_needed.get(command, -1):
            print('Warning: invalid command:', line)
            continue
        try:
            if command in ('insert', 'get', 'update', 'delete_at'):
                index = int(parts[1])
            if command == 'append':
                linked_list.append(parts[1])
            elif command == 'prepend':
                linked_list.prepend(parts[1])
            elif command == 'insert':
                linked_list.insert(index, parts[2])
            elif command == 'get':
                print('get(' + str(index) + ') =', linked_list.get(index))
            elif command == 'find':
                print('find(' + parts[1] + ') =', linked_list.find(parts[1]))
            elif command == 'len':
                print('len =', len(linked_list))
            elif command == 'update':
                linked_list.update(index, parts[2])
            elif command == 'delete':
                if not linked_list.delete(parts[1]):
                    print('Warning: value not found:', parts[1])
            elif command == 'delete_at':
                print('delete_at(' + str(index) + ') =', linked_list.delete_at(index))
            elif command == 'print_list':
                linked_list.print_list()
        except (IndexError, ValueError):
            print('Warning: invalid index:', line)
    print('Final list:', end=' ')
    linked_list.print_list()


if __name__ == '__main__':
    main()
