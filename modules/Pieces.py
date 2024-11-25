import pygame
from pygame.locals import *
# from modules.Pawn import Pawn


class Pieces:
    selected = False
    onwer = 0  # w - white | b - black
    img = 0
    screen = 0
    piece_pos = 0
    x = 0
    y = 0

    def __init__(self, onwer, y, x, screen):
        self.onwer = onwer
        self.x = x
        self.y = y
        self.screen = screen

    def update(self, pos_cal, board, img=None):
        self.img = [img, self.img][img == None]
        self.piece_pos = (board.x + (pos_cal * self.x),
                          board.y + (pos_cal * self.y))

    def draw(self):
        self.screen.blit(self.img, (self.piece_pos[0], self.piece_pos[1]))

    def update_pos(self, board, pos_cal):
        self.piece_pos = (board.x + (pos_cal * self.x),
                          board.y + (pos_cal * self.y))

    # def move(self, pos, board , dead_piece):
    # 	# dead_piece = board.pieces_pos[pos[0]][pos[1]]
    # 	if dead_piece == self:
    # 		return

    # 	# check if is a legal move
    # 	# check if is Castling

    # 	for i, item in enumerate(board.pieces):
    # 		if item == dead_piece:
    # 			dead_piece = ''
    # 			board.pieces[i] = ''

    # 	board.pieces_pos[self.y][self.x] = ''
    # 	board.pieces_pos[pos[0]][pos[1]] = self
    # 	self.x = pos[1]
    # 	self.y = pos[0]

    # 	board.draw_pieces()
