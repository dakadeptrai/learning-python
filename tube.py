
from stack_oop import StackLL, Node

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

    def pourOut(self): # co the dung push truc tiep
        self.pop()

from typing import List

class TubeManager():
    def __init__(self,tubelist : List[Tube] = []) -> None:
        self.tubelist = tubelist
        self.status = [False]*len(tubelist) # [False]

    def isValidMove(self,srcTube: Tube, desTube: Tube):
        """
        kiểm tra xem có thể di chuyển nước giữa 
        srcTube và desTube 
        """
        # nếu srcTube không rỗng và desTube không full
            # nếu desTube không rỗng
                # return True
            # srcTube có màu sắc ở top bằng với desTube 
                #return True

            # trường hợp còn lại 
                #return False
        #return False

        if (not srcTube.checkempty()) and (not desTube.checkfull()):
            # desTube không rỗng
            if desTube.checkempty():
                return True
            # srcTube có màu sắc ở top bằng với desTube 
            elif srcTube.getTopColor().data == desTube.getTopColor().data:
                return True
            else:
                return False
        return False

    def moveWater(self, srcIdx, desIdx):
        # srcTube = vị trí của srcTube trong tubelist
        # desTube = vị trí của desTube trong tubelist
        # kiểm tra xem có thể di chuyển nước giữa srcTube và desTube 
            # color = xóa giá trị của srcTube tại tall
            # xóa thêm giá trị vào desTube tại tall





        srcTube = self.tubelist[srcIdx]
        desTube = self.tubelist[desIdx]
        if self.isValidMove(srcTube,desTube):
            color = srcTube.pop()
            desTube.push(color)
        
    def isFinish(self):

        for i in range(len(self.tubelist)):
            tubeitem = self.tubelist[i]
            # kiem tra ong co rong (empty) khong?
            if tubeitem.checkempty():
                self.status[i] = True
            # kiem tra cac mau trong ong co dong nhat hay khong?
            elif tubeitem.checkfull():
                self.status[i]=True
                colors = tubeitem.getListColor()
                waterA = colors[0]
                for waterB in colors [1:]:
                    if waterA != waterB:
                        self.status[i]=False
            else: # neu khong rong vaf khon dong nhat thi False
                self.status[i]=False
        # Duyet qua danh sach trang thai cua cac tube
        for s in self.status:
            if s == False:
                print('You did not win')
                return False
        print('You win!')

tM = TubeManager([
    Tube(['red', 'green' , 'blue' ,'yellow']),
    Tube(['red', 'green' , 'blue' ,'yellow']),
    Tube(['red', 'green' , 'blue' ,'yellow']),
    Tube(['red', 'green' , 'blue' ,'yellow']),
    Tube(),
    Tube()
])

for t in tM.tubelist:
    print(t)

gameOver = False
while not gameOver:
    src = int(input('Source (0-5):'))
    des = int(input('Destination (0-5):'))
    tM.moveWater(src, des)
    for t in tM.tubelist:
        print(t)
    gameOver = tM.isFinish()
