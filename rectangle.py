# import sys
#
# import pygame
#
# # clock = pygame.time.Clock()
# #  clock.tick(5)     скорость обновления экрана
#
# pygame.init()
#
# screen_width, screen_height = 1200, 800
# screen = pygame.display.set_mode((screen_width, screen_height))
#
# pygame.display.set_caption("Shooter")
# fill_color = (225, 166, 173)
#
# rect_width, rect_height = 100, 50
# rect_x = screen_width / 2 - rect_width / 2
# rect_y = screen_height / 2 - rect_height / 2
# rect_color = (209, 65, 82)
#
# STEP = 10
#
# while True:
#     for event in pygame.event.get():
#         # print(event)
#         if event.type == pygame.QUIT:
#             sys.exit()
#         if event.type == pygame.KEYDOWN :
#             if event.key == pygame.K_UP and rect_y>=STEP:
#                 rect_y -= STEP
#             if event.key == pygame.K_DOWN and rect_y<=screen_height-STEP-rect_height:
#                 rect_y += STEP
#             if event.key == pygame.K_LEFT and rect_x>=STEP:
#                 rect_x -= STEP
#             if event.key == pygame.K_RIGHT and rect_x<=screen_width-STEP-rect_width:
#                 rect_x += STEP
#     screen.fill(fill_color)
#     pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
#
#     pygame.display.update()
