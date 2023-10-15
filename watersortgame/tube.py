from stack_oop import StackLL

class Tube(StackLL):
    def __init__(self, listColor : list = None, size=4, top = None) -> None:
        super().__init__(top, size)
        if listColor != None: # ['red', 'green' , 'blue' ,'yellow']
            for c in listColor:
                self.push(c)

    def getListColor(self):
        tmp = self.top
        listcolor = []
        while tmp != None:
            listcolor.append(tmp.data)
            tmp=tmp.next

        return listcolor

    def checkempty(self):
        if self.length == 0:
            return True
        return False

    def checkfull(self):
        if self.length == self.buffer_size:
            return True
        return False

    def getTopColor(self):
        return self.top

    def pourIn(self,data): # co the dung push truc tiep
        self.push(data)

    def pourOut(self,data): # co the dung push truc tiep
        self.pop()

t = Tube(['red', 'green' , 'blue' ,'yellow']),