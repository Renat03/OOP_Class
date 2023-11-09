from interfaces.abstract_queue import AbstractQueue


class ListQueue(AbstractQueue):
    def __init__(self, capacity=5):
        self.queue = []
        self.capacity = capacity

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is full")
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity
