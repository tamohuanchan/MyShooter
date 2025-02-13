import pygame
import sys


pygame.init()

clock = pygame.time.Clock()

screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Shooter")
fill_color = (225, 166, 173)

cat_width, cat_height = 100, 100

cat_right = pygame.image.load("images/cat_run.png")
cat_right = pygame.transform.scale(cat_right, (cat_width, cat_height))

cat_left = pygame.image.load("images/cat_leght.png")
cat_left = pygame.transform.scale(cat_left, (cat_width, cat_height))

cat_pin = pygame.image.load("images/cat_pin.png")
cat_pin = pygame.transform.scale(cat_pin, (cat_width, cat_height))

cat_current = cat_right  # Текущее изображение
rect_x = screen_width / 2 - cat_width / 2
rect_y = screen_height - cat_height

cat_is_moving_left, cat_is_moving_right = False, False
STEP = 20

pin_active = False
pin_timer = 0  # Время, когда нажали пробел

boom_width, boom_height = 100, 100

boom = pygame.image.load("images/boom.png")
boom = pygame.transform.scale(boom, (boom_width, boom_height))

boom_x = rect_x + cat_width * 0.5
boom_y = rect_y + cat_height * 0.5




while True:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cat_is_moving_left = True
                pin_active = False  # Сбрасываем pin-режим
                cat_current = cat_left
            if event.key == pygame.K_RIGHT:
                cat_is_moving_right = True
                pin_active = False  # Сбрасываем pin-режим
                cat_current = cat_right
            if event.key == pygame.K_SPACE:
                cat_current = cat_pin
                pin_active = True
                pin_timer = current_time  # Запоминаем время активации
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                cat_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                cat_is_moving_right = False

    # Движение
    if cat_is_moving_left and rect_x >= STEP:
        rect_x -= STEP
    if cat_is_moving_right and rect_x <= screen_width - STEP - cat_width:
        rect_x += STEP

    # Если прошло больше 1 секунды с момента нажатия SPACE, вернуть правильное изображение
    if pin_active and current_time - pin_timer > 1000:
        cat_current = cat_left if cat_is_moving_left else cat_right
        pin_active = False

    screen.fill(fill_color)
    screen.blit(cat_current, (rect_x, rect_y))
    pygame.display.update()

    clock.tick(60)  # Ограничение FPS
