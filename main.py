import pygame
import sys
from buttom import Image_Buttom
from random import randint


pygame.init()


MAX_FPS = 60


game_font = pygame.font.Font("images/myttf.ttf", 80)
game_font_score = pygame.font.Font("images/myttf.ttf", 30)
clock = pygame.time.Clock()

# _________________________________________________________

screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Catter")
screen_menu_back = pygame.image.load("images/fon.gif")
screen_menu_back = pygame.transform.scale(screen_menu_back, (screen_width, screen_height))


# _________________________________________________________

def main_menu():
    button_new_game = Image_Buttom(screen_width / 2 - 150, 150, 300, 150, "New Game", "images/button_pink.png",
                                   "images/button_run.png",
                                   "images/soft_click.wav")
    button_option = Image_Buttom(screen_width / 2 - 150, button_new_game.y + 150, 300, 150, "option",
                                 "images/button_pink.png", "images/button_run.png",
                                 "images/soft_click.wav")
    button_record = Image_Buttom(screen_width / 2 - 150, button_option.y + 150, 300, 150, "record",
                                 "images/button_pink.png", "images/button_run.png",
                                 "images/soft_click.wav")
    button_exit = Image_Buttom(screen_width / 2 - 150, button_record.y + 150, 300, 150, "exit",
                               "images/button_pink.png",
                               "images/button_run.png",
                               "images/soft_click.wav")
    menu = True
    while menu:
        screen.blit(screen_menu_back, (0, 0))
        font = pygame.font.Font("images/myttf.ttf", 80)
        text_surface = font.render("MENU", True, (35, 45, 83))
        text_rect = text_surface.get_rect(center=(screen_width / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT:
                if event.button == button_new_game:
                    fade()
                    new_game()
                if event.button == button_option:
                    fade()
                    option_menu()
                if event.button == button_record:
                    fade()
                    pass
                if event.button == button_exit:
                    menu = False
                    pygame.quit()
                    sys.exit()
            for btm in [button_new_game, button_option, button_record, button_exit]:
                btm.handle_event(event)

        for btm in [button_new_game, button_option, button_record, button_exit]:
            btm.check_hover(pygame.mouse.get_pos())
            btm.draw(screen)

        pygame.display.flip()


def option_menu():
    button_audio = Image_Buttom(screen_width / 2 - 150, 150, 300, 150, "audio", "images/button_pink.png",
                                "images/button_run.png",
                                "images/soft_click.wav")
    button_video = Image_Buttom(screen_width / 2 - 150, button_audio.y + 150, 300, 150, "video",
                                "images/button_pink.png", "images/button_run.png",
                                "images/soft_click.wav")
    button_complexity = Image_Buttom(screen_width / 2 - 150, button_video.y + 150, 300, 150, "complexity",
                                     "images/button_pink.png", "images/button_run.png",
                                     "images/soft_click.wav")
    button_back = Image_Buttom(screen_width / 2 - 150, button_complexity.y + 150, 300, 150, "back",
                               "images/button_pink.png",
                               "images/button_run.png",
                               "images/soft_click.wav")
    option = True
    while option:
        screen.blit(screen_menu_back, (0, 0))
        font = pygame.font.Font("images/myttf.ttf", 80)
        text_surface = font.render("OPTION", True, (35, 45, 83))
        text_rect = text_surface.get_rect(center=(screen_width / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                option = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    option = False
            if event.type == pygame.USEREVENT:
                if event.button == button_audio:
                    fade()
                    pass
                if event.button == button_video:
                    fade()
                    pass
                if event.button == button_complexity:
                    fade()
                    pass
                if event.button == button_back:
                    fade()
                    option = False
            for btm in [button_audio, button_video, button_complexity, button_back]:
                btm.handle_event(event)
        for btm in [button_audio, button_video, button_complexity, button_back]:
            btm.check_hover(pygame.mouse.get_pos())
            btm.draw(screen)

        pygame.display.flip()


def new_game():
    fill_color = (225, 166, 173)

    cat_width, cat_height = 100, 100

    cat_right = pygame.image.load("images/cat_run.png")
    cat_right = pygame.transform.scale(cat_right, (cat_width, cat_height))

    cat_left = pygame.image.load("images/cat_leght.png")
    cat_left = pygame.transform.scale(cat_left, (cat_width, cat_height))

    cat_pin = pygame.image.load("images/cat_pin.png")
    cat_pin = pygame.transform.scale(cat_pin, (cat_width, cat_height))

    cat_current = cat_right
    rect_x = screen_width / 2 - cat_width / 2
    rect_y = screen_height - cat_height

    cat_is_moving_left, cat_is_moving_right = False, False

    STEP = 10

    pin_active = False
    pin_timer = 0

    # _________________________________________________________
    boom_width, boom_height = 70, 70

    boom_image = pygame.image.load("images/boom.png")
    boom_image = pygame.transform.scale(boom_image, (boom_width, boom_height))

    booms = []
    BOOM_SPEED = 8
    boom_fired = False

    # _________________________________________________________

    rate_width, rate_height = 70, 70
    rate_images = [
        pygame.image.load("images/rate_run_left_1.png"),
        pygame.image.load("images/rate_run_left_2.png"),
        pygame.image.load("images/rate_run_right_1.png"),
        pygame.image.load("images/rate_run_right_2.png")
    ]

    rate_images_rip = pygame.image.load("images/rate_rip.png")

    def spawn_rate():
        """Спавнит новую крысу со случайным изображением"""
        return randint(0, screen_width - rate_width), 0, pygame.transform.scale(
            rate_images[randint(0, len(rate_images) - 1)], (rate_width, rate_height))

    RATE_SPEED = 0.5
    rate_new_speed = RATE_SPEED

    rate_x, rate_y, rate_image = spawn_rate()

    # _________________________________________________________

    game_is_running = True

    game_score = 0

    dead_rates = []

    while game_is_running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cat_is_moving_left = True
                    pin_active = False
                    cat_current = cat_left
                if event.key == pygame.K_RIGHT:
                    cat_is_moving_right = True
                    pin_active = False
                    cat_current = cat_right
                if event.key == pygame.K_SPACE and not boom_fired:
                    boom_x = rect_x + cat_width * 0.5 - boom_width * 0.5
                    boom_y = rect_y
                    booms.append([boom_x, boom_y])
                    cat_current = cat_pin
                    pin_active = True
                    pin_timer = current_time
                    boom_fired = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_is_running = False

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

        if pin_active and current_time - pin_timer > 1000:
            cat_current = cat_left if cat_is_moving_left else cat_right
            pin_active = False

        new_booms = []
        for boom_x, boom_y in booms:
            boom_y -= BOOM_SPEED
            if boom_y > -boom_height:
                new_booms.append([boom_x, boom_y])
            else:
                boom_fired = False

        booms = new_booms

        # Двигаем крысу
        rate_y += rate_new_speed

        # Проверяем попадание снаряда в крысу
        for boom_x, boom_y in booms:
            if rate_x - boom_width * 0.5 < boom_x < rate_x + rate_width + boom_width * 0.5 \
                    and rate_y < boom_y < rate_y + rate_height:
                boom_fired = False

                dead_rates.append((rate_x, rate_y, current_time))

                rate_x, rate_y, rate_image = spawn_rate()
                rate_new_speed += 0.1  # теперь скорость будет увеличиваться
                game_score += 1

        # Удаляем мертвых крыс, если прошло больше 1 секунды
        dead_rates = [(x, y, t) for x, y, t in dead_rates if current_time - t <= 1000]

        # Если крыса дошла до низа, она возрождается
        if rate_y + rate_height >= screen_height:
            rate_x, rate_y, rate_image = spawn_rate()

        if rate_y + rate_height >= rect_y:
            game_is_running = False

        screen.fill(fill_color)
        screen.blit(cat_current, (rect_x, rect_y))
        screen.blit(rate_image, (rate_x, rate_y))

        for dead_x, dead_y, _ in dead_rates:
            screen.blit(pygame.transform.scale(rate_images_rip, (rate_width, rate_height)), (dead_x, dead_y))

        if boom_fired:
            for boom_x, boom_y in booms:
                screen.blit(boom_image, (boom_x, boom_y))

        game_score_text = game_font_score.render(f"Score: {game_score}", True, (35, 45, 83))
        screen.blit(game_score_text, (20, 20))

        pygame.display.update()

    # Финальная подпись_____________________

    game_over_text = game_font.render("GAME OVER", True, (35, 45, 83))
    game_over_table = game_over_text.get_rect()
    game_over_table.center = (screen_width / 2, screen_height / 2)
    screen.blit(game_over_text, game_over_table)

    pygame.display.update()
    pygame.time.wait(5000)


# затемнение
def fade():
    fade_start = 0  # Начальный уровень прозрачности

    while fade_start <= 30:  # Плавно увеличиваем прозрачность
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        fade_surface = pygame.Surface(screen.get_size())
        fade_surface.fill((255, 255, 255))  # Делаем белый цвет вместо черного
        fade_surface.set_alpha(fade_start)

        screen.blit(fade_surface, (0, 0))  # Отрисовываем белое затемнение
        pygame.display.flip()

        fade_start += 5  # Увеличиваем уровень прозрачности

clock.tick(MAX_FPS)

if __name__ == "__main__":
    main_menu()

main_menu()
