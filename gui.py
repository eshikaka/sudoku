import sys, pygame as pg
import requests

pg.init()
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
number_grid = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
screen_size = 750, 750
screen = pg.display.set_mode(screen_size)
pg.display.set_caption("Sudoku")
font = pg.font.SysFont(None, 35)


# number_grid = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ]

def draw_background():
    screen.fill(pg.Color("lavender"))
    #draw outside square
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 720, 720), 10)
    i = 1
    while (i * 80) < 720:
        line_width = 1 if i % 3 > 0 else 7
        #draw vertical lines
        pg.draw.line(screen, pg.Color("black"), pg.Vector2((i * 80)+ 15, 15), pg.Vector2((i * 80) + 15, 735), line_width)
        #draw horizontal lines
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15, (i * 80)+ 15), pg.Vector2(735, (i * 80) + 15), line_width)

        i += 1

def draw_numbers():
    row = 0
    offset = 48
    while row < 9:
        col = 0
        while col < 9:
            output = grid[row][col]
            # print(str(output))

            if(0<output<10):
                n_text = font.render(str(output), True, pg.Color("black"))
                screen.blit(n_text, pg.Vector2((col * 80) + offset, (row * 80) + offset))
            col += 1

        row += 1


def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    draw_background()
    draw_numbers()
    pg.display.flip()




while 1:
    game_loop()