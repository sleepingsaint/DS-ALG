# defining stack element object
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# defining stack object
class Stack(object):
    def __init__(self, head=None):
        self.head = head

    # helper class functions
    # function to add elements
    def append(self, new_element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Element(new_element)
        else:
            self.head = Element(new_element)

    # function to see the position of the element
    def get_position_value(self, position):
        current = self.head
        counter = 1
        if position < 1:
            return None
        else:
            while current and counter <= position:
                if counter == position:
                    return current.value
                current = current.next
                counter += 1
        return None

    # function to insert an element at an certain position
    # Inserting at position 3 means between the 2nd and 3rd elements
    def insert_element(self, index, new_element):
        if self.head:
            current = self.head
            counter = 1
            if index == 1:
                e = Element(new_element)
                e.next, self.head = self.head, e
            elif index > 1:
                while current and counter < index - 1:
                    current = current.next
                    counter += 1
                if not current:
                    print('cannot insert the element')
                else:
                    e = Element(new_element)
                    e.next, current.next = current.next, e

    # function to delete an first node with given value
    def delete(self, value):
        if self.head:
            current = self.head
            previous = None
            while current.value != value and current.next:
                previous = current
                current = current.next
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
        else:
            return None


# initializing the stack
stck = Stack()

# adding elements
stck.append(1)
stck.append(2)
stck.append(3)

# getting position


# inserting element
stck.insert_element(2, 4)
stck.delete(3)
print(stck.get_position_value(1))
print(stck.get_position_value(2))
print(stck.get_position_value(3))
print(stck.get_position_value(4))

stck.insert_element(500, 6)
print(stck.get_position_value(1))
print(stck.get_position_value(2))
print(stck.get_position_value(3))
