import pygame as pg
pg.init()
WIDTH = 1600
HEIGHT = 900
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Water Puzzle Game by Sumato')
from tube import Tube

COLORS = {
    'red': (255,0,0),
    'green': (0,255,0),
    'blue' : (0,0,255),
    'yellow' : (255,255,0),
    'black': (0,0,0),
    'white': (255,255,255),
    'BG': (127, 127, 127)
}
tube1 = Tube(['red','red', 'green', 'green'])

COLOR_HEIGHT = COLOR_WITH = WIDTH // 16 
TUBE_BORDER_RADIUS = COLOR_WITH // 2
tube_x = 0*(COLOR_WITH + 50) + 50
tube_y = HEIGHT//2 - 4*COLOR_HEIGHT
color_graphics = [pg.Rect(0*(COLOR_WITH + 50) + 50, \
                                HEIGHT//2 - i*COLOR_HEIGHT, COLOR_WITH,COLOR_HEIGHT) for i in range(4)]
tube_graphic_top_cover = pg.Rect((tube_x, tube_y, COLOR_WITH, 3))

#code here
def draw_Tube(tube:Tube):
    colors = tube.getListColor()[::-1]
    for i in range(len(colors)):
        if i == 0:
            pg.draw.rect(screen,COLORS[colors[i]],color_graphics[i],
                        border_bottom_left_radius= TUBE_BORDER_RADIUS,
                        border_bottom_right_radius=TUBE_BORDER_RADIUS,)
        else:
            pg.draw.rect(screen,COLORS[colors[i]], color_graphics[i])
    tube_graphics = pg.Rect(tube_x,tube_y,COLOR_WITH,5*COLOR_HEIGHT)
    pg.draw.rect(screen,COLORS['black'],tube_graphics,3,
                        border_bottom_left_radius= TUBE_BORDER_RADIUS,
                        border_bottom_right_radius=TUBE_BORDER_RADIUS)
    pg.draw.rect(screen,COLORS["BG"],tube_graphic_top_cover)
#end code

def render(screen, events):
    ''' Update current game state '''
    global gameOver
    screen.fill((127,127,127))
    print(events)
    draw_Tube(tube1)
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
