from interfaces.abstract_stack import AbstractStack


class ListStack(AbstractStack):
    def __init__(self, capacity=5):
        self.stack = []
        self.capacity = capacity

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack is full")
        self.stack.insert(0, item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        self.stack.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[0]

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

