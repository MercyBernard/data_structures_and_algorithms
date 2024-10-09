class Node:
    # A function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def find_third_smallest(root):
    # function to perform in-order traversal
    def in_order_traverse(node):
        if node is None:
            return None
        # Traverse the left subtree
        left = in_order_traverse(node.left)
        if left is not None:
            return left
        # Visit the current node
        nonlocal count
        count += 1
        if count == 3:
            return node.data
        # Traverse the right subtree
        return in_order_traverse(node.right)

    count = 0
    return in_order_traverse(root)

# Creating the BST
root = Node(400)
root.left = Node(200)
root.right = Node(600)
root.left.left = Node(100)
root.left.right = Node(300)
root.right.left = Node(500)
root.right.right = Node(700)

# Find and print the third smallest element
third_smallest = find_third_smallest(root)
print("The third smallest element is:", third_smallest)