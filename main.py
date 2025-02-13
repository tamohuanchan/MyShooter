import pygame
import sys
from random import randint

pygame.init()

game_font = pygame.font.Font("images/myttf.ttf", 80)

clock = pygame.time.Clock()

# _________________________________________________________

screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Shooter")
fill_color = (225, 166, 173)

# _________________________________________________________

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

STEP = 10

pin_active = False
pin_timer = 0  # Время, когда нажали пробел

# _________________________________________________________
boom_width, boom_height = 70, 70  # Размер снаряда

boom_image = pygame.image.load("images/boom.png")
boom_image = pygame.transform.scale(boom_image, (boom_width, boom_height))

booms = []  # Список всех снарядов
BOOM_SPEED = 8  # Скорость полёта
boom_fired = False  # Флаг выстрела

# _________________________________________________________

rate_width, rate_height = 70, 70
rate_images = [
    pygame.image.load("images/rate_run_left_1.png"),
    pygame.image.load("images/rate_run_left_2.png"),
    pygame.image.load("images/rate_run_right_1.png"),
    pygame.image.load("images/rate_run_right_2.png")
]


def spawn_rate():
    """Спавнит новую крысу со случайным изображением"""
    return randint(0, screen_width - rate_width), 0, pygame.transform.scale(
        rate_images[randint(0, len(rate_images) - 1)], (rate_width, rate_height))


RATE_SPEED = 0.5
rate_new_speed = RATE_SPEED

rate_x, rate_y, rate_image = spawn_rate()

# _________________________________________________________

game_is_runnig = True

while game_is_runnig:
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
            if event.key == pygame.K_SPACE and not boom_fired:
                # Добавляем новый снаряд в список
                boom_x = rect_x + cat_width * 0.5 - boom_width * 0.5
                boom_y = rect_y
                booms.append([boom_x, boom_y])
                cat_current = cat_pin
                pin_active = True
                pin_timer = current_time  # Запоминаем время активации
                boom_fired = True  # Устанавливаем флаг выстрела

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                cat_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                cat_is_moving_right = False

    # Движение кота
    if cat_is_moving_left and rect_x >= STEP:
        rect_x -= STEP
    if cat_is_moving_right and rect_x <= screen_width - STEP - cat_width:
        rect_x += STEP

    # Если прошло больше 1 секунды после `SPACE`, вернуть прошлое направление
    if pin_active and current_time - pin_timer > 1000:
        cat_current = cat_left if cat_is_moving_left else cat_right
        pin_active = False

    # Двигаем все снаряды вверх и проверяем, остались ли они на экране
    new_booms = []
    for boom_x, boom_y in booms:
        boom_y -= BOOM_SPEED
        if boom_y > -boom_height:  # Снаряд на экране
            new_booms.append([boom_x, boom_y])
        else:
            boom_fired = False  # Снаряд улетел за экран

    booms = new_booms

    # Двигаем крысу
    rate_y += rate_new_speed

    # Проверяем попадание снаряда в крысу
    for boom_x, boom_y in booms:
        if rate_x - boom_width * 0.5 < boom_x < rate_x + rate_width + boom_width * 0.5 \
                and rate_y < boom_y < rate_y + rate_height:
            boom_fired = False  # Сброс флага, так как снаряд попал в цель
            rate_x, rate_y, rate_image = spawn_rate()  # Спавним новую крысу
            rate_new_speed +=RATE_SPEED+0.05

    # Если крыса дошла до низа, она возрождается
    if rate_y + rate_height >= screen_height:
        rate_x, rate_y, rate_image = spawn_rate()

    # Проверка на столкновение крысы с котом
    if rate_y + rate_height >= rect_y:
        game_is_runnig = False

    # Обновляем экран
    screen.fill(fill_color)
    screen.blit(cat_current, (rect_x, rect_y))
    screen.blit(rate_image, (rate_x, rate_y))

    # Отрисовка всех снарядов, если boom_fired = True
    if boom_fired:
        for boom_x, boom_y in booms:
            screen.blit(boom_image, (boom_x, boom_y))

    pygame.display.update()

    clock.tick(120)  # Ограничение FPS

# Финальная подпись_____________________

game_over_text = game_font.render("GAME OVER", True, (35, 45, 83))

game_over_table = game_over_text.get_rect()
game_over_table.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_table)

pygame.display.update()
pygame.time.wait(5000)

pygame.quit()
