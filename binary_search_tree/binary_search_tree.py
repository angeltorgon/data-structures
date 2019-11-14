import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value > value:
            if self.left == None:
                new_tree = BinarySearchTree(value)
                self.left = new_tree
            else:
                self.left.insert(value)
        if self.value < value:
            if self.right == None:
                new_tree = BinarySearchTree(value)
                self.right = new_tree
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(8)
bst.insert(4)
print(bst.left.value, "< -- Left Value")
bst.insert(10)
print(bst.right.value, "< -- Right Value")
bst.insert(12)
print(bst.right.right.value, "< -- Right Value of right node")
bst.insert(9)
print(bst.right.left.value, "< -- Left Value of right node")
