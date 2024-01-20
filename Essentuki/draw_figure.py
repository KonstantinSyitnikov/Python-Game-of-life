import pygame
import numpy as np
import time
import pygame
import numpy as np
import time

RES = WIDTH, HEIGHT = 1500, 900
TILE = 6
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 10
aj = 1
pygame.init()
surface = pygame.display.set_mode(RES)

next_field = np.array([[0 for i in range(W)] for j in range(H)])
current_field = np.array([[1 if i == W // 2 or j == H // 2 else 0 for i in range(W)] for j in range(H)])


def draw_field():
    surface.fill(pygame.Color('black'))
    for x in range(0, WIDTH, TILE):
        pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILE):
        pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y))
    for i in range(W):
        for j in range(H):
            if current_field[j, i] == 1:
               pygame.draw.rect(surface, pygame.Color('forestgreen'), (i * TILE + 1, j * TILE + 1, TILE - 1, TILE - 1))


    pygame.display.flip()




def get_neighbours(cell):
   
    count = 0
   
    row, col = cell
   
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= row + i < H and 0 <= col + j < W:
                count += current_field[row + i, col + j]
              
    return count

run = True

while run:
    aj += 1
    draw_field()
    next_field = current_field.copy()
    for i in range(W):
        for j in range(H):
            
            neighbours = get_neighbours((j, i))
            if aj==10:
                print (aj)
                aj=1
            if current_field[j, i] == 1 and (neighbours < 2 or neighbours > 3):
                next_field[j, i] = 0
            if current_field[j, i] == 0 and neighbours == 3:
                next_field[j, i] = 1
    current_field = next_field.copy()
    time.sleep(1 / FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            break
       