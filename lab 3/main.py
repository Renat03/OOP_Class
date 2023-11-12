# from implementations.dict_stack import DictStack

# ds = DictStack()
# print(ds.is_full())
# ds.push(1)
# ds.push({"number": 5})
# ds.push('3')
# print(ds.peek())
# ds.pop()
# print(ds.peek())

from implementations.circular_queue import CircularQueue

cq = CircularQueue()
print(cq.is_full())
cq.enqueue("First in the queue")
cq.enqueue([1, 2, 3])
cq.enqueue(False)
print(cq.peek())
cq.dequeue()
print(cq.peek())
