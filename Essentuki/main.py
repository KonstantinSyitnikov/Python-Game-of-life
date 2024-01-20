import pygame
from copy import deepcopy
import numpy as np
from numba import njit
from collections import deque
import imageio

RES = WIDTH, HEIGHT = 1400, 900
TILE = 7
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 8

pygame.init()
surface = pygame.display.set_mode(RES)
pygame.display.set_caption("It's alive! It's alive!")  # Set the initial title
clock = pygame.time.Clock()

next_field = np.array([[0 for i in range(W)] for j in range(H)])
current_field = np.array([[0 for i in range(W)] for j in range(H)])
for i in range(H):
    current_field[i][i + (W - H) // 2] = 1
    current_field[H - i - 1][i + (W - H) // 2] = 1

@njit(fastmath=True)
def check_cells(current_field, next_field):
    res = []
    for x in range(W):
        for y in range(H):
            count = 0
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if current_field[j % H][i % W] == 1:
                        count += 1

            if current_field[y][x] == 1:
                count -= 1
                if count == 2 or count == 3:
                    next_field[y][x] = 1
                    res.append((x, y))
                else:
                    next_field[y][x] = 0
            else:
                if count == 3:
                    next_field[y][x] = 1
                    res.append((x, y))
                else:
                    next_field[y][x] = 0

    return next_field, res


# Timer setup
start_time = pygame.time.get_ticks()
delay_time = 10  # 10 seconds in milliseconds

frames = []  # to store frames

while pygame.time.get_ticks() - start_time < delay_time:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# Main loop after the delay
while True:
    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
   # [pygame.draw.line(surface, pygame.Color('#0a120c'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
   # [pygame.draw.line(surface, pygame.Color('#0a120c'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
    current_field, res = check_cells(current_field, next_field)
    
    
    [pygame.draw.rect(surface, pygame.Color('#14ba28'),
                      (x * TILE + 1, y * TILE + 1, TILE - 1, TILE - 1)) for x, y in res]

    current_field = deepcopy(next_field)
    
    # Save the current frame
    frame = pygame.surfarray.array3d(surface)
    frames.append(frame)

    print(clock.get_fps())
    pygame.display.flip()
    clock.tick(FPS)

    # Break the loop after a certain number of frames to create a GIF
    if len(frames) == 340:
        break
    
   
# Save frames as a GIF    
expanded_width = WIDTH + 10
expanded_height = HEIGHT + 10
imageio.mimsave('Its alive! Its alive!.gif', frames, duration=1/FPS, subrect=(0, 0, expanded_width, expanded_height))



    
"""
import pygame
from random import randint
from copy import deepcopy

RES = WIDTH, HEIGHT = 1500, 900
TILE = 8
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 6

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()



next_field = [[0 for i in range(W)] for j in range(H)]
#current_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[1 if i == W // 2 or j == H // 2 else 0 for i in range(W)] for j in range(H)]
#current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]
#current_field = [[1 if not i % 9 else 0 for i in range(W)] for j in range(H)] # 2,5,8,9,10,11,13,18,21,22,26,30,33,65
#current_field = [[1 if not (2 * i + j) % 4 else 0 for i in range(W)] for j in range(H)] # (2,4),(4,4)
#current_field = [[1 if not (i * j) % 22 else 0 for i in range(W)] for j in range(H)] # 5,6,9,22,33
#current_field = [[1 if not i % 7 else randint(0, 1) for i in range(W)] for j in range(H)]
#for i in range(H):
 #   current_field[i][i+(W-H)//2]=1
  #  current_field[H-i-1][i+(W-H)//2]=1

def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:

    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [pygame.draw.line(surface, pygame.Color('#222922'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('#222922'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
    # draw life
    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if current_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('forestgreen'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            next_field[y][x] = check_cell(current_field, x, y)

    current_field = deepcopy(next_field)

    print(clock.get_fps())
    pygame.display.flip()
    clock.tick(FPS)

"""



#this is glider
"""
current_field = np.array([[0 for i in range(W)] for j in range(H)])
current_field[0][1] = 1
current_field[1][2] = 1
current_field[2][0] = 1
current_field[2][1] = 1
current_field[2][2] = 1
"""
#this is mirmidons
"""
current_field = np.array([[0 for i in range(W)] for j in range(H)])
current_field[1][2] = 1
current_field[1][3] = 1
current_field[2][1] = 1
current_field[3][2] = 1
current_field[3][3] = 1
current_field[3][4] = 1
current_field[4][1] = 1
current_field[4][3] = 1
"""
#this is pulsar
"""
current_field = np.array([[0 for i in range(W)] for j in range(H)])
pulsar_positions = [(2, 4), (2, 5), (2, 6), (2, 10), (2, 11), (2, 12),
                    (4, 2), (4, 7), (4, 9), (4, 14),
                    (5, 2), (5, 7), (5, 9), (5, 14),
                    (6, 2), (6, 7), (6, 9), (6, 14),
                    (7, 4), (7, 5), (7, 6), (7, 10), (7, 11), (7, 12),
                    (9, 4), (9, 5), (9, 6), (9, 10), (9, 11), (9, 12),
                    (10, 2), (10, 7), (10, 9), (10, 14),
                    (11, 2), (11, 7), (11, 9), (11, 14),
                    (12, 2), (12, 7), (12, 9), (12, 14),
                    (14, 4), (14, 5), (14, 6), (14, 10), (14, 11), (14, 12)]
for pos in pulsar_positions:
    current_field[pos[0]][pos[1]] = 1
"""

