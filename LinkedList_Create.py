# Defines a Node class to represent each element in the linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data  # Stores the value of the node
        self.next = next  # Stores the reference to the next node

# Defines a LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initializes the head of the list to None (empty list)

    # Method to insert a new node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Creates a new node with the given data
        new_node.next = self.head  # Sets the next reference of the new node to the current head
        self.head = new_node  # Updates the head to point to the new node

    # Method to traverse and print the list
    def traverse(self):
        current = self.head  # Starts from the head of the list
        while current:  # Loops until the end of the list
            print(current.data, end=", ")  # Prints the data of the current node
            current = current.next  # Moves to the next node
        

# Example usage of the LinkedList class
ll = LinkedList()  # Creates a LinkedList object
ll.insert_at_beginning(1)  # Inserts 1 at the beginning
ll.insert_at_beginning(2)  # Inserts 2 at the beginning
ll.insert_at_beginning(3)  # Inserts 3 at the beginning
ll.insert_at_beginning(4)  # Inserts 4 at the beginning
ll.traverse()  # Traverses and prints the list


