# Импорт модулей
import pygame
import random

# Инициализация Pygame
pygame.init()

# Создание игрового экрана
SCREEN_WIDTH = 800  # ширина
SCREEN_HEIGHT = 600  # высота
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # переменная вывода экрана

# Настройка игрового окна
pygame.display.set_caption("Игра Тир")  # вывод названия игры

# Установка иконки для игрового окна
icon = pygame.image.load("img/icon.jpg")  # загрузка иконки
pygame.display.set_icon(icon)  # вывод иконки на экран

# Работа со спрайтами (загрузка и вывод на экран)
target_img = pygame.image.load("img/target.png")
target_img = pygame.transform.scale(target_img, (80, 80))  # Принудительное изменение размера

# Определение размеров цели
target_width = 80  # ширина
target_height = 80  # высота

# Установка начальных координат цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)  # переменная случайной координаты "х"
target_y = random.randint(0, SCREEN_HEIGHT - target_height)  # переменная случайной координаты "y"

# Установка цвета для фона (рандомный выбор RGB: красного, зеленого, синего)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Создание игрового цикла
running = True  # Переменная контроля игрового цикла
while running:  # Игра завершается при изменении переменной с True на False
    screen.fill(color)  # Заливка экрана случайным цветом
    for event in pygame.event.get():  # Перебор событий игры с сохранением в переменной event
        if event.type == pygame.QUIT:  # в случае вызова события закрытия окна (нажатия крестика)
            running = False  # в переменной True переключается на False и игра заканчивается
        # Создание игровой механики
        if event.type == pygame.MOUSEBUTTONDOWN:  # Если результатом перебора событий является нажатие мышки
            mouse_x, mouse_y = pygame.mouse.get_pos()  # то координаты клика мышки сохранятся в переменных
            # Если координаты клика мышки попадают в диапазон координат изображения цели,
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # то изображение цели перемещается в произвольное место экрана
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Вывод изображения на экран
    screen.blit(target_img, (target_x, target_y))  # координаты вывода изображения на экран
    pygame.display.update()  # команда отображения любых изменений на экране (например, движение изображения)

# Команда завершения работы модуля
pygame.quit()
