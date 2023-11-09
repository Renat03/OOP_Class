from implementations.dict_stack import DictStack

ds = DictStack()
print(ds.is_full())
ds.push(1)
ds.push({"number": 5})
ds.push('3')
print(ds.peek())
ds.pop()
print(ds.peek())