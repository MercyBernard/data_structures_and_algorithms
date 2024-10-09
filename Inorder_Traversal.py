class Node:
    # A function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Function to perform in-order traversal
def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.data, end=' ')
        in_order_traversal(root.right)

# Function to find the minimum value node in a tree
def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Function to delete a node
def delete_node(root, key):
    if root is None:
        return root

    # If the key to be deleted is smaller than the root's key
    if key < root.data:
        root.left = delete_node(root.left, key)

    # If the key to be deleted is greater than the root's key
    elif key > root.data:
        root.right = delete_node(root.right, key)

    # If key is same as root's key, then this is the node to be deleted
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children, get the inorder successor (smallest in the right subtree)
        temp = min_value_node(root.right)

        root.data = temp.data

        # Delete the inorder successor
        root.right = delete_node(root.right, temp.data)

    return root

# Function to delete the root node
def delete_root_node(root):
    return delete_node(root, root.data)

# Test cases
# 1. Regular Test Case: Binary Tree
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

# Print in-order traversal of the original tree
print("In-order traversal of the original tree:")
in_order_traversal(root)
print()

# Delete the root node
root = delete_root_node(root)

# Print in-order traversal of the new tree
print("In-order traversal of the tree after deleting the root node:")
in_order_traversal(root)
print()

# 2. Single node
# root = Node(4)
# print("In-order traversal of the original tree:")
# in_order_traversal(root)
# print()

# Delete the root node
# root = delete_root_node(root)

# Print in-order traversal of the new tree
# print("In-order traversal of the tree after deleting the root node:")
# in_order_traversal(root)
# print()