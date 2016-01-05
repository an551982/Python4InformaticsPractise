def chop(lst):
    lst.pop(0)
    lst.pop(-1)
    return None

def middle(lst):
    return lst[1:-1]

LIST = ['a','b','c','d','e']
print middle(LIST)
print LIST
chop(LIST)
print LIST

