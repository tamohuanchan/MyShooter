import pygame
import sys
from buttom import Image_Buttom
from random import randint

pygame.init()

game_font = pygame.font.Font("images/myttf.ttf", 80)
game_font_score = pygame.font.Font("images/myttf.ttf", 30)
clock = pygame.time.Clock()

# _________________________________________________________

screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Catter")
fill_color = (225, 166, 173)

# _________________________________________________________

button_new_game = Image_Buttom(screen_width / 2 - 150, 150, 300, 150, "New Game", "images/button_pink.png",
                               "images/button_run.png",
                               "images/soft_click.wav")
button_option = Image_Buttom(screen_width / 2 - 150, button_new_game.y + 150, 300, 150, "option",
                             "images/button_pink.png", "images/button_run.png",
                             "images/soft_click.wav")
button_record = Image_Buttom(screen_width / 2 - 150, button_option.y + 150, 300, 150, "record",
                             "images/button_pink.png", "images/button_run.png",
                             "images/soft_click.wav")
button_exit = Image_Buttom(screen_width / 2 - 150, button_record.y + 150, 300, 150, "exit", "images/button_pink.png",
                           "images/button_run.png",
                           "images/soft_click.wav")


def main_menu():
    menu = True
    while menu:
        screen.fill(fill_color)
        font = pygame.font.Font("images/myttf.ttf", 80)
        text_surface = font.render("MENU", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(screen_width / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT:
                if event.button == button_new_game:
                    pass
                if event.button == button_option:
                    pass
                if event.button == button_record:
                    pass
                if event.button == button_exit:
                    menu = False
                    pygame.quit()
                    sys.exit()

            button_new_game.handle_event(event)
            button_option.handle_event(event)
            button_record.handle_event(event)
            button_exit.handle_event(event)

        button_new_game.check_hover((pygame.mouse.get_pos()))
        button_option.check_hover((pygame.mouse.get_pos()))
        button_record.check_hover((pygame.mouse.get_pos()))
        button_exit.check_hover((pygame.mouse.get_pos()))

        button_new_game.draw(screen)
        button_option.draw(screen)
        button_record.draw(screen)
        button_exit.draw(screen)

        pygame.display.flip()


main_menu()
