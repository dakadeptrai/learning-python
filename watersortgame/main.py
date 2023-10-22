from typing import List
import pygame as pg
from config import WIDTH, HEIGHT, COLORS
from graphic import TubeGraphic, TubeGraphicManager
from tube import Tube

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Water Puzzle Game by Sumato')

tM = TubeGraphicManager(screen,[
    Tube(['green', 'red' , 'blue' ,'yellow']),
    Tube(['red', 'green' , 'blue' ,'yellow']),
    Tube(['red', 'green' , 'blue' ,'yellow']),
    Tube(['red', 'green' , 'blue' ,'yellow']),
    Tube([]),
    Tube([]),
])
# Hàm draw_move_text sẽ hiển thị số lượt di chuyển.
def processInput(events,tube_graphics):
    for event in events:
        if event.type == pg.MOUSEBUTTONDOWN:
            print('MOUSEBUTTONDOWN detected')
            detect_interaction(tube_graphics)
#def detect_interactions(tube_graphics: List[TubeGraphic]):
    #for tg in tube_graphics:
        #detect_tube_selection(tg)
def detect_tube_selection(tg:TubeGraphic):
    mouse_focus = pg.mouse.get_focused() != 0
    left_mouse_clicked = pg.mouse.get_pressed()[0]
    clicked_on_tube = tg.tube_graphic.collidepoint(pg.mouse.get_pos())
    tube_empty = tg.tube.checkempty()
    if mouse_focus and left_mouse_clicked and clicked_on_tube and not tube_empty:
        print(str(tg.id)+' is selected')
        tg.lift_up()
move_count = 0
def detect_destination_tube_and_deselection(source_tube: TubeGraphic,destination_tube:TubeGraphic):
    global move_count
    #Neu chon destination tube trung voi source tube thi bo qua
    if destination_tube.is_selected:
        destination_tube.lift_down()
        return
    mouse_focused_on_game = pg.mouse.get_focused()!= 0
    left_mouse_clicked = pg.mouse.get_pressed()[0]
    mouse_tube_collision = destination_tube.tube_graphic.collidepoint(pg.mouse.get_pos())
    #kiem tra chuot co click vao destination tube khong
    if mouse_focused_on_game and left_mouse_clicked and mouse_tube_collision:
        #kiem tra hanh dong do mau co hop le khong
        if tM.isValidMove(source_tube.tube,destination_tube.tube):
            tM.moveWater(source_tube.tube,destination_tube.tube)
            move_count += 1
def detect_interaction(tube_graphics: List[TubeGraphic]):
    any_tube_selected= any(tg.is_selected for tg in tube_graphics)
    if any_tube_selected:
        source_tube=[tg for tg in tube_graphics if tg.is_selected][0]
    for tube in tube_graphics:
        if not any_tube_selected:
            detect_tube_selection(tube)
        else:
            detect_destination_tube_and_deselection(source_tube,tube)
def render(screen, events):
    ''' Update current game state '''
    global gameOver
    screen.fill((127,127,127))
    
    for tube_graphic in tM.tubeGraphicList:
        tube_graphic.drawTube()
    gameOver = tM.isFinish()
    processInput(events,tM.tubeGraphicList)
    pg.display.update()


gameOver = False
def gameLoop():
    while not gameOver:
        pressed_keys = pg.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pg.event.get():
            quit_attempt = False
            if event.type == pg.QUIT:
                quit_attempt = True
            elif event.type == pg.KEYDOWN:
                alt_pressed = pressed_keys[pg.K_LALT] or \
                                pressed_keys[pg.K_RALT]
                if event.key == pg.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pg.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                pg.quit()
            else:
                filtered_events.append(event)
        render(screen, filtered_events)
    pg.time.delay(5000)


if __name__ == '__main__':
    gameLoop()
