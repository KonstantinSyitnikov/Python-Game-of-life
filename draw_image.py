#pip install pillow
#pip install numpy

import pygame
import cv2
import numpy as np

def image_to_life_points(image_path, threshold=128):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary_image = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    life_points = np.argwhere(binary_image == 255)
    return life_points

def draw_life(screen, life_points, cell_size):
    for point in life_points:
        pygame.draw.rect(screen, (255, 255, 255), (point[1] * cell_size, point[0] * cell_size, cell_size, cell_size))

def main():
    pygame.init()

    # Параметры игры
    image_path = 'Image/DNK.jpeg'
    threshold = 128
    cell_size = 10  # Размер ячейки
    width, height = 800, 600  # Размер окна

    # Создаем окно Pygame
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game of Life")

    # Получаем начальные точки из изображения
    life_points = image_to_life_points(image_path, threshold)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Очищаем экран

        # Отрисовываем текущее поколение
        draw_life(screen, life_points, cell_size)

        pygame.display.flip()
        clock.tick(10)  # Количество кадров в секунду

    pygame.quit()

if __name__ == "__main__":
    main()





"""
def image_to_life_points(image_path, threshold=128):
    # Открываем изображение с помощью Pillow
    img = Image.open(image_path).convert('L')  # Конвертируем в черно-белый формат
    
    # Получаем массив numpy из изображения
    img_array = np.array(img)
    
    # Применяем пороговое значение для преобразования изображения в бинарное
    binary_array = (img_array > threshold).astype(int)
    
    # Получаем координаты начальных точек
    life_points = np.argwhere(binary_array == 1)
    
    return life_points

# Пример использования
image_path = 'Image/DNK.jpeg'
life_points = image_to_life_points(image_path)

print("Начальные точки для игры Жизнь:")
print(life_points)


"""