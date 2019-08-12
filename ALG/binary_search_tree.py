# creating node object class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# creating tree object class
class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = Node(root)

    # class functions
    def search(self, value):
        return self.bst_search(self.root, value)

    def insert(self, value):
        if self.root.value is None:
            self.root = Node(value)
        else:
            self.bst_insert(self.root, value)

    def print_tree(self):
        print(self.bst_print_tree(self.root, "")[:-3])

    # helper class functions
    def bst_search(self, start, value):
        if start:
            if start.value == value:
                return True
            elif start.value > value:
                self.bst_search(start.right, value)
            else:
                self.bst_search(start.left, value)
        return False

    def bst_insert(self, start, value):
        if value < start.value:
            if start.left is None:
                start.left = Node(value)
            else:
                self.bst_insert(start.left, value)
        elif value > start.value:
            if start.right is None:
                start.right = Node(value)
            else:
                self.bst_insert(start.right, value)

    def bst_print_tree(self, start, traversal):
        if start:
            traversal += str(start.value) + " - "
            traversal = self.bst_print_tree(start.left, traversal)
            traversal = self.bst_print_tree(start.right, traversal)
        return traversal

# test cases
bst = BinarySearchTree(1)
bst.insert(2)
bst.print_tree()