# CS_526_Week_2
Problem 1: By using a tail pointer, it allows a new node to be added to the end of a linked list without going through the entire list

Problem 2: Each node points to the next node. I keep head, tail, and size so adding at either end and finding the length are O(1). Other indexed operations and searches walk through nodes and take O(n) in the worst case. Insertions and deletions change the links instead of shifting array elements.

Problem 3: Every route starts with either 1, 2, or 3 steps. Therefore ways(n) = ways(n-1) + ways(n-2) + ways(n-3). The base cases are ways(0) = 1 (one completed route) and ways(n) = 0 for negative n (overshooting is invalid). With only 1- and 2-step moves, the results follow the Fibonacci sequence, shifted by one position (ways(n) = F(n+1)).

Problem 4: I insert each new value in its sorted position, adjusting both prev and next. This keeps the list sorted without sorting it again. Recursion works naturally for reading nodes one at a time in exists, count, total, and print_list. Because values are sorted, searching/counting can stop after passing the target. Insertion and traversal are O(n) in the worst case; removing a node after locating it is O(1).
