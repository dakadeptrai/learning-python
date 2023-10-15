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
    
def render(screen, events):
    ''' Update current game state '''
    global gameOver
    screen.fill((127,127,127))
    
    for tube_graphic in tM.tubeGraphicList:
        tube_graphic.drawTube()
    gameOver = tM.isFinish()
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
