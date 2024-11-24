import os
import array
import math
import cairo
import pygame
import numpy
from pygame.locals import *
from modules.Board import Board
from modules.Windows import Windows

pygame.init()

# b_bishop   0
# b_king     1
# b_knight   2
# b_pawn     3
# b_queen    4
# b_rook     5
# w_bishop   6
# w_king     7
# w_knight   8
# w_pawn     9
# w_queen    10
# w_rook     11


running: bool = True
mouse_button_down: pygame.event.Event = None

clock: pygame.time.Clock = pygame.time.Clock()
mainWindows: Windows = Windows()


def reload_images(board_size):
    lista = []
    size_cal = round(board_size / 8)

    for item in lista_img:
        lista.append(pygame.transform.smoothscale(item, (size_cal, size_cal)))

    return lista


while running:
    for event in pygame.event.get():
        # print(pygame.event.event_name(event.type))
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            mouse_button_down = event
            # print(mouse_button_down)

    mainWindows.check_windows_resize()
    mainWindows.check_click(mouse_button_down)
    mainWindows.draw()

    mouse_button_down = None

    pygame.display.flip()

    clock.tick(120)

pygame.quit()
