# defining Element Object
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# defining LinkedList Object
class LinkedList(object):
    def __init__(self, head=None):
        self.head = Element(head)

    def append(self, new_element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Element(new_element)
        else:
            self.head = Element(new_element)

    def insert_first(self, new_element):
        e = Element(new_element)
        e.next, self.head = self.head, e

    def delete_first(self):
        deleted = None
        if self.head:
            deleted = self.head
            self.head = deleted.next
        return deleted


# defining Stack Class Object
class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(1)

# Test stack functionality
stack.push(2)
stack.push(3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(4)
print(stack.pop().value)
