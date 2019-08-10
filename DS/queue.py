# defining queue object
class Queue(object):
    def __init__(self, head=None):
        self.line = [head]

    # helper function for adding elements
    def enqueue(self, value):
        if self.line[0] is None:
            self.line[0] = value
        else:
            self.line.append(value)

    # helper function for popping elements
    def deque(self):
        return self.line.pop(0)

    # helper function for peeking the first element of the queue
    def peek(self):
        return self.line[0]

    # helper function for knowing the queue
    def show_queue(self):
        print(self.line)


# test cases
# initializing queue
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.show_queue()