import pygame

import sys
from itertools import combinations

from business_logic import *
from tic_tac_toe_logic import *


pygame.init()
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Tic Tac Toe")


def update_display(win, grid, rows, width):
    win.fill(BG_COLOR)  # Clear the screen with background color
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()


def draw_grid(win, rows, width):
    gap = width // ROWS
    for i in range(rows):
        pygame.draw.line(
            win, LINE_COLOR, (0, i * gap), (width, i * gap), width=4
        )  # Thicker lines
        for j in range(rows):
            pygame.draw.line(win, LINE_COLOR, (j * gap, 0), (j * gap, width), width=4)


class Piece:
    def __init__(self, image):
        self.image = image


def make_move(grid, row, col, player):
    if grid[row][col].piece is None:
        if player == "Player 1":
            grid[row][col].piece = Piece(X_IMAGE)

        elif player == "Player 2":
            grid[row][col].piece = Piece(O_IMAGE)

        return True
    return False


def tic_tac_toe(WIDTH, ROWS):
    grid = make_grid(ROWS, WIDTH)

    # reset player if new game
    reset_player()

    while True:
        # get current player
        currPlayer = get_player()
        if check_winner(grid, X_IMAGE):
            return "Player 1"
        elif check_winner(grid, O_IMAGE):
            return "Player 2"
        elif check_draw(grid):
            return "Draw"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("EXIT SUCCESSFUL")
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // (WIDTH // ROWS)
                col = x // (WIDTH // ROWS)

                if make_move(grid, row, col, currPlayer):
                    # if move is valid, change player
                    change_player()
                    priorMoves.append((row, col))

        update_display(WIN, grid, ROWS, WIDTH)
