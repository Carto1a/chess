import pygame
from pygame.locals import *


class Square:
    clicked = 0
    color = 0
    color_move = 0
    color_selected = 0
    color_take = 0
    color_atual = 0
    pos = 0
    size = 0
    sqt = 0
    screen = 0
    selected = False
    states = {}

    def __init__(self, screen, square_size, x, y, colors):
        self.screen = screen
        self.pos = (x, y)
        self.size = square_size
        self.color = colors[0]
        self.color_atual = colors[0]
        self.color_selected = colors[3]
        self.color_move = colors[2]
        self.color_take = colors[1]
        self.states = {"selected": self.color_selected, "normal": self.color,
                       "move": self.color_move, "take": self.color_take}
        self.sqt = pygame.Rect(self.size, self.size, self.size, self.size)

    def __str__(self):
        return self.sqt

    def update(self, board_pos, square_size):
        self.sqt.update(board_pos[0] + square_size * self.pos[1],
                        board_pos[1] + square_size * self.pos[0], square_size, square_size)

    def draw(self):
        pygame.draw.rect(self.screen, self.color_atual, self.sqt)

    def is_collide(self, point):
        collide = self.sqt.collidepoint(point)
        return collide
        # if collide:
        # 	self.clicked = not self.clicked
        # 	color = (self.color_cliked, self.color)[self.clicked]
        # 	self.draw(self.screen, color)

        # 	self.selected = not self.selected

        # 	return self.selected

        # return False

    def change_state(self, state: str):
        self.color_atual = self.states[state]
