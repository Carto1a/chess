import pygame
import math
from pygame.locals import *
from modules.Square import Square
# from modules.Pieces import Pieces
from modules.Pawn import Pawn


class Board:
    pieces_pos = [['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                  ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                  ['',   '', '',  '',  '',  '',  '',  ''],
                  ['',   'wp', '',  '',  '',  '',  '',  ''],
                  ['',   '', '',  '',  '',  '',  '',  ''],
                  ['',   '', '',  'bp',  '',  '',  '',  ''],
                  ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                  ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp']
                  ]
    pieces = []
    squares = []
    board_size = 0
    square_size = 0
    rect = 0
    board_center = 0
    board_size = 0
    board_size_pervius = 0
    clicked = False
    selected_piece = 0
    square_previus = 0
    selected = False
    lista_img_scale = []
    moves = 0
    turn: str = 'w'
    op_turn: dict = ['w', 'b']
    turn_counter: int = 0
    turn_interator: int = 1

    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(
            self.board_size, self.board_size, self.board_size, self.board_size)

    def init_squares(self, color_cliked):
        colors = [Color(93, 50, 49), Color(121, 72, 57)]
        move = Color(158, 32, 16)
        take = Color(232, 225, 9)
        selected = Color(6, 68, 184)
        color_set = True

        y = 0
        while y < 8:
            x = 0
            lista = []
            while x < 8:
                color = (colors[0], colors[1])[color_set]
                lista.append(Square(self.screen, self.square_size,
                             y, x, (color, take, move, selected)))
                color_set = not color_set
                x += 1
            self.squares.append(lista)
            color_set = not color_set
            y += 1

    def init_pieces(self):
        for indexy, itemy in enumerate(self.pieces_pos):
            for indexx, item in enumerate(itemy):
                if item == '':
                    continue

                if item[1] == "p":
                    self.pieces_pos[indexy][indexx] = Pawn(
                        item[0], indexy, indexx, self.screen)

                self.pieces.append(self.pieces_pos[indexy][indexx])

    def update_size_pos(self, board_center, board_size):
        self.board_center = board_center
        self.board_size = board_size
        self.rect.update(
            board_center[0], board_center[1], board_size, board_size)

    def update_squares(self):
        self.square_size = round(self.board_size / 8)

        y = 0
        while y < 8:
            x = 0
            while x < 8:
                self.squares[y][x].update(self.board_center, self.square_size)
                x += 1
            y += 1

    def draw_squares(self):
        y = 0
        while y < 8:
            x = 0
            while x < 8:
                self.squares[y][x].draw()
                x += 1
            y += 1

    def draw_pieces(self, reload_images=None):
        pos_cal = round(self.rect.width / 8)
        if self.board_size != self.board_size_pervius:
            self.lista_img_scale = reload_images(self.board_size)
            self.board_size_pervius = self.board_size
            for item in self.pieces:
                if item == '':
                    continue
                if item.onwer == "b":
                    if isinstance(item, Pawn):
                        item.update(pos_cal, self.rect,
                                    self.lista_img_scale[3])
                else:
                    if isinstance(item, Pawn):
                        item.update(pos_cal, self.rect,
                                    self.lista_img_scale[9])

                item.draw()

        else:
            for item in self.pieces:
                if item == '':
                    continue
                item.update(pos_cal, self.rect)
                item.draw()

    # verificar se o movimento é valido
    #
    def check_turn(self, piece):
        onwer = piece.onwer
        return (False, True)[onwer == self.turn]

    def next_turn(self):
        if self.turn_counter == 0 and self.turn_interator == -1:
            self.turn_interator *= -1
        if len(self.op_turn) == self.turn_counter + 1:
            self.turn_interator *= -1
        self.turn_counter += self.turn_interator
        self.turn = self.op_turn[self.turn_counter]

    def clear_moves(self):
        for square in self.moves:
            self.squares[square[0]][square[1]].change_state("normal")
        return

    def get_square(self):
        point = pygame.mouse.get_pos()
        square_size = self.square_size

        # x - (x(n-1)/n) - 1 forma uga uga
        point_normalized = (point[0] - self.rect.x, point[1] - self.rect.y)

        if point_normalized[0] < 0 or point_normalized[1] < 0:
            return
        if point_normalized[0] > self.rect.w or point_normalized[1] > self.rect.h:
            return

        pos_index = (math.floor(
            point_normalized[0]/square_size), math.floor(point_normalized[1]/square_size))

        select_squere = self.squares[pos_index[1]][pos_index[0]]

        return {'select': select_squere, 'x': pos_index[0], 'y': pos_index[1]}

    def check_pos(self):
        pos_square = self.get_square()
        piece_pos = self.pieces_pos[pos_square['y']][pos_square['x']]

        if self.selected:
            self.clear_moves()
            self.square_previus.change_state("normal")

            # reescrever essa parte?
            if piece_pos == self.selected_piece:
                self.selected = False
                self.selected_piece = 0
                return

            if (pos_square['y'], pos_square['x']) in self.moves:
                self.selected_piece.move(pos_square['select'].pos, self)
                self.next_turn()

            self.selected_piece = 0
            self.selected = False
            return

        if piece_pos == '':
            return

        # reescrever
        if not self.check_turn(piece_pos):
            return

        self.selected = pos_square['select']
        self.selected_piece = piece_pos
        self.square_previus = pos_square['select']
        self.selected.change_state("selected")
        print(f"x = {self.selected_piece.x} | y = {self.selected_piece.y}")

        self.moves = self.selected_piece.moves(
            self.pieces_pos, (self.selected_piece.y, self.selected_piece.x), self.selected_piece.onwer)
        for square in self.moves[0]:
            self.squares[square[0]][square[1]].change_state("move")
        for square in self.moves[1]:
            self.squares[square[0]][square[1]].change_state("take")

        self.moves = self.moves[0] + self.moves[1]
        print(self.moves)
        return

    def check_click(self, event):
        click = pygame.mouse.get_pressed()[0]
        if click and not self.clicked:
            self.clicked = True
            self.check_pos()

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

    def is_check():
        pass

    def is_mate():
        pass

    def is_possible_castling():
        pass
