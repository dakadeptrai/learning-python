class StackBase:
    def __init__(self, top = None, buffer_size = 1000) -> None:
        self.top = top
        self.buffer_size = buffer_size
        self.length = 0 if top == None else 1

    def push(self, data): # phai override push
        raise NotImplementedError('function push(self, data) hasn\'t been implemented yet.')
    
    def pop(self):
        raise NotImplementedError('function pop(self) hasn\'t been implemented yet.')

    def peak(self):
        if self.length == 0:
            return 'Stack is empty.'
        return self.top

    def __str__(self):
        raise NotImplementedError('function __str__(self) hasn\'t been implemented yet.')


class StackList(StackBase):
    def __init__(self, top=None, buffer_size=1000) -> None:
        super().__init__(top, buffer_size)
        self.stack_list = [] if top == None else [top]

    def push(self, data):
        if self.length == self.buffer_size:
            print('Stack is full')
            return
        self.stack_list.append(data)
        self.top = data
        self.length +=1

    def pop(self):
        if self.length == 0:
            return 'Stack is empty!'
        self.length -=1
        self.top = self.stack_list[-2]
        value = self.stack_list[-1]
        del self.stack_list[-1]
        return value

    def __str__(self):
        return str(self.stack_list[::-1])

class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

class StackLL(StackBase):
    def __init__(self, top=None, buffer_size=1000) -> None:
        super().__init__(top, buffer_size)
    
    def push(self, data):
        if self.buffer_size == self.length:
            print('Stack is full')
            return 
        newNode = Node(data, self.top)
        self.top = newNode
        self.length +=1

    def pop(self):
        """
        xóa phần tử tại vị tri top (tall)
        """
        if self.top == None:
            return
        tmp = self.top.next
        value = self.top.data
        del self.top
        self.top = tmp
        self.length -=1
        return value

    def __str__(self):
        ret = ''
        tmp = self.top
        while tmp!= None:
            # print(tmp.data, end='->')
            ret += str(tmp.data) + '->'
            tmp = tmp.next
        return ret

# sB = StackBase()

# l = [1,2,3,4]
# sL = StackList()
# # stackList = StackLL()
# for element in l:
#     sL.push(element)
# print(sL)
# print(sL.pop())
# print(sL)

# sLL = StackLL()
# for element in l:
#     sLL.push(element)
# print(sLL)
# print(sLL.pop())
# print(sLL)

# print(issubclass(StackList, StackBase))
# print(issubclass(StackList, StackLL))