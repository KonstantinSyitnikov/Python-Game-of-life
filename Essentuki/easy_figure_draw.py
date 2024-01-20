import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Рисование треугольника")

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Установка начальных точек треугольника

triangle_points = [(300, 100), (200, 500), (600, 500)]
""" 
x1, y1 = 300, 100
x2, y2 = 200, 300
x3, y3 = 400, 300
 
# Основной цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(WHITE)

    # Рисование треугольника
    pygame.draw.polygon(screen, BLACK, [(x1, y1), (x2, y2), (x3, y3)])

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()



"""
def draw_line(start, end):
    pygame.draw.line(screen, WHITE, start, end)
    
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()   
    
    # очистка экрана
   screen.fill(BLACK)

# рисование треугольника с помощью линий
   for i in range(3):
    start_point = triangle_points[i]
    end_point = triangle_points[(i + 1) % 3]
    draw_line(start_point, end_point)

# обновление экрана
    pygame.display.flip()     