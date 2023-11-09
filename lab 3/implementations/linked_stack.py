from interfaces.abstract_stack import AbstractStack


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack(AbstractStack):
    def __init__(self, capacity=5):
        self.top = None
        self.size = 0
        self.capacity = capacity

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack is full")
        else:
            new_node = Node(item)
            new_node.next = self.top
            self.top = new_node
            self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            value = self.top.value
            self.top = self.top.next
            self.size -= 1
            return value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity
