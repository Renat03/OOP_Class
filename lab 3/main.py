# from implementations.dict_stack import DictStack

# ds = DictStack()
# print(ds.is_full())
# ds.push(1)
# ds.push({"number": 5})
# ds.push('3')
# print(ds.peek())
# ds.pop()
# print(ds.peek())

from implementations.list_queue import ListQueue

lq = ListQueue()
print(lq.is_full())
lq.enqueue("First in the queue")
lq.enqueue([1, 2, 3])
lq.enqueue(False)
print(lq.peek())
lq.dequeue()
print(lq.peek())