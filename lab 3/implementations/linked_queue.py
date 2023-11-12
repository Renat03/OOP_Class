from interfaces.abstract_queue import AbstractQueue


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue(AbstractQueue):
    def __init__(self, capacity=5):
        self.front = None
        self.rear = None
        self.size = 0
        self.capacity = capacity

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is full")
        else:
            new_node = Node(item)
            if self.rear:
                self.rear.next = new_node
            self.rear = new_node
            if not self.front:
                self.front = new_node
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:    
            value = self.front.value
            self.front = self.front.next
            if self.size == 0:
                self.rear = None
            self.size -= 1
            return value

    def peek(self):
        if self.is_empty():
            return None
        return self.front.value

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity
