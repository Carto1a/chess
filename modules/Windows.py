import os
import array
import math
import cairo
import pygame
import numpy
from pygame.locals import *
from modules.Board import Board


class Windows():

    screen: pygame.Surface
    board: Board
    line: Rect

    lista_img: list = []

    board_size: int = 0
    board_size_pervius: int = 0
    line_size: int = 0
    line_size_x: int = 25
    selected: bool = False
    screen_size_previus: tuple = (0, 0)
    theme_dir: str = ''
    currenct_theme: str = '0'

    def __init__(self):
        self.screen = pygame.display.set_mode(
            (640, 360), HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.board = Board(self.screen)
        self.line = pygame.Rect(
            self.line_size, self.line_size, self.line_size, self.line_size)

        if self.currenct_theme in os.listdir('assets/pieces'):
            for item in numpy.sort(os.listdir(f'assets/pieces/{self.currenct_theme}')):
                self.lista_img.append(pygame.image.load(
                    f"assets/pieces/{self.currenct_theme}/{item}"))
        else:
            print("esse tema não exite")

        self.board.init_squares(Color(44, 59, 120, 10))
        self.board.init_pieces()

    def check_click(self, event):
        click = pygame.mouse.get_pressed()[0]
        if click and not self.clicked:
            self.clicked = True
            self.board.check_pos()

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

    def check_windows_resize(self):
        screen = self.screen
        if self.screen_size_previus != (screen.get_width(), screen.get_height()):
            self.screen_size_previus = (
                screen.get_width(), screen.get_height())
            screen_size = (round(screen.get_width() / 2),
                           round(screen.get_height() / 2))

            if screen_size[0] > screen_size[1]:
                # largura é maior
                self.board_size = round(
                    screen.get_height() - ((screen_size[1] + screen_size[0]) / 28))
                self.line_size = screen.get_height()

            else:
                # altura é maior
                self.board_size = round(
                    screen.get_width() - ((screen_size[1] + screen_size[0]) / 28))
                self.line_size = screen.get_width()

            board_center = (round(
                screen_size[0] - self.board_size / 2), round(screen_size[1] - self.board_size / 2))
            line_center = (round(
                screen_size[0] - self.line_size / 2), round(screen_size[1] - self.line_size / 2))

            self.line.update(
                line_center[0], line_center[1], self.line_size, self.line_size)
            self.board.update_size_pos(board_center, self.board_size)
            self.board.update_squares()

    def reload_images(self, board_size):
        lista = []
        size_cal = round(board_size / 8)

        for item in self.lista_img:
            lista.append(pygame.transform.smoothscale(
                item, (size_cal, size_cal)))

        return lista

    def draw(self):
        self.screen.fill(Color(56, 56, 56))

        pygame.draw.rect(self.screen, "black", self.line)
        pygame.draw.rect(self.screen, "black", self.board.rect)

        self.board.draw_squares()
        self.board.draw_pieces(self.reload_images)
