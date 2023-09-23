class QueueList:
    def __init__(self,top = None,buffer_size = 100) -> None:
        self.top = top
        self.buffer_size = buffer_size
        self.lenght = 0 if top == None else 1
        self.queue_list = [] if top == None else [top]
    def is_empty(self):
        return len(self.queue_list) == 0
    def Enqueue(self,data):
        if self.lenght == self.buffer_size:
            return"the list is full"
        self.queue_list.append(data)
        self.lenght += 1
    def Dequeue(self):                                                                     
        if self.is_empty():
            return None
        self.lenght += 1
        tamp = self.queue_list[0]
        self.queue_list.pop(0)
        return tamp
            
queue = QueueList()
queue.Enqueue(1)
queue.Enqueue(2)
queue.Enqueue(3)
print(queue.Dequeue())
print(queue.Dequeue())
print(queue.queue_list)


