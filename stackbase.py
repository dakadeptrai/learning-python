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