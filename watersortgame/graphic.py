
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
        colorRect = []
        for y in range(4):
            colorRect = pg.Rect(self.id*(COLOR_WITH + 50)+50,\
                                HEIGHT//2 - y*COLOR_HEIGHT,COLOR_WITH,COLOR_HEIGHT)
            colorRect.append(colorRect)
        return colorRect
    def draw_Tube(self):
        colors = self.tube.getListColor()[::-1]
        for i in range(len(colors)):
            if i == 0:
                pg.drdaw.rect(self.screen,COLORS[colors[i]],self.color_graphics[i],
                            border_bottom_left_radius= TUBE_BORDER_RADIUS,
                            border_bottom_right_radius=TUBE_BORDER_RADIUS,)
            else:
                pg.draw.rect(self.screen,COLORS[colors[i]], self.color_graphics[i])
        tube_graphics = pg.Rect(self.tube_x,self.tube_y,COLOR_WITH,5*COLOR_HEIGHT)
        pg.draw.rect(self.screen,COLORS['black'],tube_graphics,3,
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
        self.tube_graphic.update(self.tube_graphic.left,
                                 self.tube_graphic.top - offset,
                                 self.tube_graphic.width,
                                 self.tube_graphic.height)
        self.tube_graphic.update(self.tube_graphic_top_cover.left,
                                 self.tube_graphic_top_cover-offset,
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
        self.status = [False]*len(self.tubeGraphicList)
    def isValidMove(self,fromTube : Tube,toTube:Tube):
        if fromTube.checkempty() or toTube.checkfull():
            return False
        if toTube.checkempty():
            return True
        if fromTube.getTopColor().data != toTube.getTopColor.data:
            return False
        return True
    def moveWaterByIdx(self,srcIdx:int,desIdx:int):
        srcTube = self.tubeGraphicList[srcIdx].tube
        desTube = self.tubeGraphicList[desIdx].tube
        if self.isValidMove(srcTube,desTube):
            color = srcTube.pop()
            desTube.pourIn(color)
    def moveWater(self,srcTube:Tube,desTube:Tube):
        if self.isValidMove(srcTube,desTube):
            desTube.push(srcTube.pop())
    def isFinish(self):
        for i in range(len(self.tubeGraphicList)):
            tubeitem = self.tubeGraphicList[i].tube
            if tubeitem.checkempty():
                self.status[i] = True
            elif tubeitem.checkfull():
                colors = tubeitem.getListColor()
                waterA = colors[0]
                self.status[i]=True
                for waterB in colors[1:]:
                    if waterA != waterB:
                        self.status[i] = False
            else:
                self.status[i] = False
        for statusitem in self.status:
            if statusitem == False:
                print('You didnt win')
                return False
        print('you win!')
        return True
