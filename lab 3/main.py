from implementations.list_stack import ListStack

ls = ListStack()
print(ls.is_full())
ls.push(1)
ls.push({"number": 5})
ls.push('3')
print(ls.peek())
ls.pop()
print(ls.peek())