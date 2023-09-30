from stack_oop import StackLL
#from <ten file> import <class/variable,...>
class Tube(StackLL):
    def __init__(self,listcolor : list = None, buffer_size = 4,top = None):
        super().__init__(top,buffer_size)
        if listcolor != None:
            for c in listcolor:
                self.push(c)
    def getListColor(self):
        tmp = self.top
        listcolor = []
        while tmp != None:
            listcolor.append(tmp.data)
            tmp = tmp.next
        return listcolor
    def getTopColor(self):
        return self.top
    def checkempty(self):
        if self.length == 0:
            return True
        return False
    def checkempty(self):
        if self.length == self.buffer_size:
            return True
        return False
    def pourIn(self,data):
        self.push(data)
    def pourOut(self):
        self.pop()
fast = Tube(['Green','Black','Yellow','Brown'])
print(fast.getTopColor().data)
fast.pourOut()
fast.pourIn('Blue')
print(fast.getListColor())


