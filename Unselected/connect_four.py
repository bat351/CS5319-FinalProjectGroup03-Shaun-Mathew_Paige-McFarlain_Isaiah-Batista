# sources: https://github.com/KeithGalli/Connect4-Python/blob/master/connect4.py
# 		 https://www.youtube.com/watch?v=SDz3P_Ctm7U

import numpy as np
import math
import pygame
import sys
from business_logic import *
from connect_four_logic import *


SCREEN = pygame.display.set_mode((800, 800))

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(
                SCREEN,
                BLUE,
                (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE),
            )
            pygame.draw.circle(
                SCREEN,
                BLACK,
                (
                    int(c * SQUARESIZE + SQUARESIZE / 2),
                    int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2),
                ),
                RADIUS,
            )

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(
                    SCREEN,
                    RED,
                    (
                        int(c * SQUARESIZE + SQUARESIZE / 2),
                        SIZE - int(r * SQUARESIZE + SQUARESIZE / 2),
                    ),
                    RADIUS,
                )
            elif board[r][c] == 2:
                pygame.draw.circle(
                    SCREEN,
                    YELLOW,
                    (
                        int(c * SQUARESIZE + SQUARESIZE / 2),
                        SIZE - int(r * SQUARESIZE + SQUARESIZE / 2),
                    ),
                    RADIUS,
                )


def connect_4():

    board = create_board()
    print(board)
    game_over = False

    pygame.init()

    draw_board(board)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 75)

    # reset player if new game
    reset_player()

    while not game_over:
        # get player
        player = get_player()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            # BUSINESS LOGIC LAYER
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(SCREEN, BLACK, (0, 0, SIZE, SQUARESIZE))
                posx = event.pos[0]
                if player == "Player 1":
                    pygame.draw.circle(SCREEN, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                elif player == "Player 2":
                    pygame.draw.circle(
                        SCREEN, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS
                    )
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(SCREEN, BLACK, (0, 0, SIZE, SQUARESIZE))

                # Player 1 input
                if player == "Player 1":
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)
                        if winning_move(board, 1):
                            return "Player 1"
                # Player 2 input
                elif (player == "Player 2"):
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)
                        if winning_move(board, 2):
                            return "Player 2"
                print_board(board)
                draw_board(board)
                # change player
                change_player()

                if game_over:
                    pygame.time.wait(3000)
