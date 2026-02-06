# Node class for a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to detect a cycle in the linked list
def has_cycle(head):
    slow = fast = head  # Two pointers

    while fast and fast.next:
        slow = slow.next          # Move slow by 1
        fast = fast.next.next     # Move fast by 2

        if slow == fast:          # Pointers meet => cycle exists
            return True

    return False  # No cycle found


# ---- Example usage ----
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head.next  # Cycle created

print(has_cycle(head))  # True


'''
 OUTPUT:
True
'''