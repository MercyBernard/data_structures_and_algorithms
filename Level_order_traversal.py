#Import the deque class from the collections module
from collections import deque

#Create nodes for a binary tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    #Define level order traversal function
    def levelorder(self):
        LOT = [] #Empty list to store the traversal
        current = root
        stack = deque([self])

        while len(stack) > 0: #Loop runs while deque is not empty
            current = stack.popleft()
            LOT.append(current.data)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return LOT

#Test Cases
#Regular
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print(root.levelorder())

#Single node
#node = Node(4)
#print(node.levelorder())