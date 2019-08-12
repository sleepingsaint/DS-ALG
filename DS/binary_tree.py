# creating node object class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# creating binary tree object class
class BinaryTree(object):
    def __init__(self, root=None):
        self.root = Node(root)

    def search(self, value):
        return self.search_element(self.root, value)

    def print_tree(self):
        print(self.print_tree_helper(self.root, "")[:-3])

    def search_element(self, start, value):
        if start:
            if start.value == value:
                return True
            else:
                return self.search_element(start.left, value) or self.search_element(start.right, value)
        return False

    def print_tree_helper(self, start, tree_list):
        if start:
            tree_list += str(start.value) + " - "
            tree_list = self.print_tree_helper(start.left, tree_list)
            tree_list = self.print_tree_helper(start.right, tree_list)
        return tree_list

# test cases
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.print_tree()