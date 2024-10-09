class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # Method to insert a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to traverse and print the list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=", ")
            current = current.next
    

ll = LinkedList()  # Creates a LinkedList object
ll.insert_at_end(1)  # Inserts 1 at the beginning
ll.insert_at_end(2)  # Inserts 2 at the beginning
ll.insert_at_end(3)  # Inserts 3 at the beginning
ll.insert_at_end(4)  # Inserts 4 at the beginning
ll.traverse()
