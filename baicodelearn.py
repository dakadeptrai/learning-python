class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def create_node(x):
    temp = Node()
    temp.next = None
    temp.data = x
    return temp

def print_list(l):
    p = l
    while p is not None:
        print(p.data, end=" ")
        p = p.next

def add_element(p, x):
    temp = create_node(x)
    p.next = temp
    return temp

def convert(l, a, b):
    p = l
    while p is not None:
        if p.data == a:
            p.data = b
        p = p.next
    return l

n = int(input())

# T
print()
x = int(input())
l = create_node(x)
p = l
for i in range(1, n):
    x = int(input())
    p = add_element(p, x)

a = int(input())
b = int(input())

l = convert(l, a, b)

print_list(l) 