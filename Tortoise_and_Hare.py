class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to check if the linked list is circular using the tortoise and hare algorithm
    def is_circular(self):
        if not self.head:
            return False

        tortoise = self.head
        hare = self.head

        while hare and hare.next:
            tortoise = tortoise.next  # Tortoise moves one step
            hare = hare.next.next  # Hare moves two steps

            if tortoise == hare:
                return True

        return False

# Example usage:
ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

ll.head.next = second
second.next = third
third.next = fourth
# Uncomment the next line to create a cycle
# fourth.next = second

print(ll.is_circular())  # Output: False (or True if cycle is created)
