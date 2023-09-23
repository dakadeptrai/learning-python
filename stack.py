'''class Stack:
    def __init__(self,top = None, buffer_size = 100) -> None:
        self.top = top
        self.buffer_size = buffer_size
        self.lenght = 0 if top == None else 1
        self.stack_list = [] if top == None else [top]
    def push(self,data):
        if self.buffer_size == self.lenght:
            print('list stack')
            return
        self.stack_list.append(data)
        self.top = data
        self.lenght += 1
    def pop(self):
        if self.lenght == 0:
            return 'Stack empty'

        self.lenght -= 1
        self.top = self.stack_list[-2]
        tamp = self.stack_list[-1]
        del self.stack_list[-1]
        return tamp
    def peek(self):
        if self.lenght == 0:
            return 'Stack empty'
        return self.top
stack = Stack(10)
print(stack.stack_list)
x = stack.push(11)
print(stack.stack_list)
x = stack.push(12)
print(stack.stack_list)
x = stack.pop()
print(stack.stack_list)
x = stack.pop()
print(stack.stack_list)'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        print()
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            data = self.top.data
            self.top = self.top.next
            return data
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.data
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
print(stack.pop())
print(stack.peek())