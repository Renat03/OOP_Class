from interfaces.abstract_stack import AbstractStack


class DictStack(AbstractStack):
    def __init__(self, capacity=5):
        self.stack = {}
        self.capacity = capacity
        self.next_index = 0

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack is full")
        self.stack[self.next_index] = item
        self.next_index += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        self.next_index -= 1
        return self.stack.pop(self.next_index)

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.next_index - 1]

    def is_empty(self):
        return self.next_index == 0

    def is_full(self):
        return self.next_index == self.capacity
