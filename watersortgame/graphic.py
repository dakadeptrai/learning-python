
from stack_oop import StackLL
from tube import Tube
import pygame as pg
from config import COLOR_HEIGHT, COLOR_WITH, TUBE_BORDER_RADIUS, COLORS, HEIGHT, WIDTH


from typing import List


class TubeGraphic:
    def __init__(self,tube:Tube,x,y,id,screen):
        self.id = id
        self.tube = tube
        self.screen = screen
        self.tube_graphic = pg.Rect(x,y,COLOR_WITH,5*COLOR_HEIGHT)
        self.tube_graphic_top_cover = pg.Rect((x,y,COLOR_WITH,3))
        self.is_selected = False
        self.color_graphics = self.get_color_graphics(y)
    def get_color_graphics(self,y):
        colorRects = []
        for y in range(4):
            colorRect = pg.Rect(self.id*(COLOR_WITH + 50)+50,\
                                HEIGHT//2 - y*COLOR_HEIGHT,COLOR_WITH,COLOR_HEIGHT)
            colorRects.append(colorRect)
        return colorRects
    def drawTube(self):
        colors = self.tube.getListColor()[::-1]     
        for i in range(len(colors)):
            if i == 0:
                pg.draw.rect(self.screen,COLORS[colors[i]],self.color_graphics[i],
                            border_bottom_left_radius= TUBE_BORDER_RADIUS,
                            border_bottom_right_radius=TUBE_BORDER_RADIUS,)
            else:
                pg.draw.rect(self.screen,COLORS[colors[i]], self.color_graphics[i])
        pg.draw.rect(self.screen,COLORS['black'],self.tube_graphic,3,
                            border_bottom_left_radius= TUBE_BORDER_RADIUS,
                            border_bottom_right_radius=TUBE_BORDER_RADIUS)
        pg.draw.rect(self.screen,COLORS["BG"],self.tube_graphic_top_cover)
    def lift_up(self):
        self._move_(20)
        self.is_selected = True
    def lift_down(self):
        self._move_(-20)
        self.is_selected = False
    def _move_(self,offset = 20):
        '''self.tube_graphic.update(self.tube_graphic.left,
                                 self.tube_graphic.top - offset,
                                 self.tube_graphic.width,
                                 self.tube_graphic.height)'''
        self.tube_graphic.update(self.tube_graphic_top_cover.left,
                                 self.tube_graphic_top_cover.top -offset,
                                 self.tube_graphic.width,
                                 self.tube_graphic.height)
        for cG in self.color_graphics:
            cG.update(cG.left,cG.top-offset,cG.width,cG.height)
class TubeGraphicManager():
    def __init__(self,screen,tubelist: list[Tube] = []) -> None:
        self.tubeGraphicList : List[TubeGraphic] = []
        #gan vi tri cho moi doi tuong Tubegraphic dua tren chi so trong tubelish
        for id, tub in enumerate(tubelist):
            #tao doi tuong tubegraphic voi tube,vi tri va man hinh tuong ung
            tubeRect = TubeGraphic(tub,id*(COLOR_WITH + 50)+50,HEIGHT//2 - 4*COLOR_HEIGHT, id, screen)
            self.tubeGraphicList.append(tubeRect)#them doi tuong Tubegraphic vao danh sach
        self.status = [False]*len(self.tubeGraphicList) # Khởi tạo danh sách trạng thái với các giá trị False
    def isValidMove(self,fromTube : Tube,toTube:Tube):
        if fromTube.checkempty() or toTube.checkfull():# Kiểm tra nếu ống nguồn trống hoặc ống đích đầy
            return False
        if toTube.checkempty():# Kiểm tra nếu ống đích trống
            return True
        if fromTube.getTopColor().data != toTube.getTopColor.data:
        # Kiểm tra nếu màu của ống trên cùng khác nhau
            return False
        return True
    def moveWaterByIdx(self,srcIdx:int,desIdx:int):
        srcTube = self.tubeGraphicList[srcIdx].tube # Lấy đối tượng Tube nguồn từ danh sách TubeGraphic
        desTube = self.tubeGraphicList[desIdx].tube # Lấy đối tượng Tube đích từ danh sách TubeGraphic
        if self.isValidMove(srcTube,desTube): # Kiểm tra nếu di chuyển hợp lệ
            color = srcTube.pop() # Xóa màu từ ống nguồn
            desTube.pourIn(color) # Đổ màu vào ống đích
    def moveWater(self,srcTube:Tube,desTube:Tube):
        if self.isValidMove(srcTube,desTube): # Kiểm tra nếu di chuyển hợp lệ
            desTube.push(srcTube.pop()) # Đẩy màu từ ống nguồn vào ống đích
    def isFinish(self):
        for i in range(len(self.tubeGraphicList)):
            tubeitem = self.tubeGraphicList[i].tube
            if tubeitem.checkempty(): # Kiểm tra nếu ống trống
                self.status[i] = True
            elif tubeitem.checkfull(): # Kiểm tra nếu ống đầy
                colors = tubeitem.getListColor()
                waterA = colors[0]
                self.status[i]=True
                for waterB in colors[1:]:
                    if waterA != waterB: # Kiểm tra nếu các màu trong ống không giống nhau
                        self.status[i] = False
            else:
                self.status[i] = False
        for statusitem in self.status:
            if statusitem == False: # Kiểm tra nếu trạng thái của bất kỳ ống nào là False
                print('You didnt win') # In ra thông báo không chiến thắng
                return False
        print('you win!')  # In ra thông báo chiến thắng
        return True
