# Импорт модулей
import pygame
import random

# Инициализация Pygame
pygame.init()

# Создание игрового экрана
SCREEN_WIDTH = 800      # ширина
SCREEN_HEIGHT = 600     # высота
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # переменная вывода экрана

# Настройка игрового окна
pygame.display.set_caption("Игра Тир")  # вывод названия игры

# Установка иконки для игрового окна
icon = pygame.image.load("img/icon.jpg")        # загрузка иконки
pygame.display.set_icon(icon)                   # вывод иконки на экран

# Работа со спрайтами (загрузка и вывод на экран)
target_img = pygame.image.load("img/target.png")

# Определение размеров цели
target_width = 80       # ширина
target_height = 80      # высота

# Установка начальных координат цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)   # переменная случайной координаты "х"
target_y = random.randint(0, SCREEN_HEIGHT - target_height) # переменная случайной координаты "y"

# Установка цвета для фона (рандомный выбор RGB: красного, зеленого, синего)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))














# Создание игрового цикла
running = True  # Переменная контроля игрового цикла
while running:  # Игра завершается при изменении переменной с True на False
        pass    # Заглушка, пока цикл не содержат кода



# Команда завершения работы модуля
pygame.quit()
