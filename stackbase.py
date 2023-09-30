class StackBase:
    def __init__(self,top = None, buffer_size = 100) -> None:
        self.top = top
        self.buffer_size = buffer_size
        self.lenght = 0 if top == None else 1
    def push (self,data):
        raise NotImplementedError('function push(self, data) hasn\'tbeen implemented yet.')
    def pop (self):
        raise NotImplementedError('function pop(self) hasn\'tbeen implemented yet.')
    def peek (self):
        raise NotImplementedError('function peek(self) hasn\'tbeen implemented yet.')
    def __str__(self):
        raise NotImplementedError('function __str__(self) hasn\'tbeen implemented yet.')
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack(StackBase):
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