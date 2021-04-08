import sys, pygame as pg

pg.init()
screen_size = 750, 750
screen = pg.display.set_mode(screen_size)

def draw_background():
    screen.fill(pg.Color("lavender"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 720, 720), 10)
    i = 1
    while (i * 80) < 720:
        #draw vertical lines
        pg.draw.line(screen, pg.Color("black"), pg.Vector2((i * 80)+ 15, 15), pg.Vector2((i * 80) + 15, 735), 5)
        #draw horizontal lines
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15, (i * 80)+ 15), pg.Vector2(735, (i * 80) + 15), 5)

        i += 1



def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    draw_background()
    pg.display.flip()




while 1:
    game_loop()