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
        if self.value == target:
            return True
        if target < self.value and self.left != None:
            if self.left.value == target:
                return True
            else:
                return self.left.contains(target)
        if target > self.value and self.right != None:
            if self.right.value == target:
                return True
            else:
                return self.right.contains(target)
        
        return False
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)
        return

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
bst.insert(10)
bst.insert(12)
bst.insert(9)
def prnt(x):
    print(f"Current node - {x}")
bst.for_each(prnt)
print(bst.get_max())