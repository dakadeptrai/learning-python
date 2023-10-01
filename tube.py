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
    def checkfull(self):
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

from typing import List
class TubeManager():
    def __init__(self,tubelist : list[Tube] = []):
        self.tubelist = tubelist
        self.status = [False]*len(tubelist)
    def isValidMove(self,scrTube : Tube,desTube : Tube):
        if (not scrTube.checkempty()) and (not desTube.checkfull()):
            if desTube.checkempty():
                return True
            elif scrTube.getTopColor().data==desTube.getTopColor().data:
                return True
            else:
                return False
        return False
    def moveWater(self,srcIndex,desIndex):
        scrTube = self.tubelist[srcIndex]
        desTube = self.tubelist[desIndex]
        if self.isValidMove(scrTube,desTube):
            color = scrTube.pop()
            desTube.push(color)
    def isFinish(self):
        for i in range(len(self.tubelist)):
            tubeitem = self.tubelist[i]
            if tubeitem.checkempty():
                self.status[i] = True
            elif tubeitem.checkfull():
                self.status[i] = True
                colors = tubeitem.getListColor()
                waterA = colors[0]
                for waterB in colors[1:]:
                    if waterA != waterB:
                        self.status[i] = False
            else:
                self.status[i] = False
        for s in self.status:
            if s == False:
                print('You didnt win')
                return False
        print('You Win')
tm = TubeManager([
    Tube(["Red","Green","Blue","Yellow"]),
    Tube(["Red","Green","Blue","Yellow"]),
    Tube(["Red","Green","Blue","Yellow"]),
    Tube(["Red","Green","Blue","Yellow"]),
    Tube(),
    Tube()
])
for t in tm.tubelist:
    print(t)
gameOver = False
while not gameOver:
    src = int(input('Source (0-5):'))
    des = int(input('Destination (0-5):'))
    tm.moveWater(src,des)
    for t in tm.tubelist:
        print(t)
    gameOver = tm.isFinish()

