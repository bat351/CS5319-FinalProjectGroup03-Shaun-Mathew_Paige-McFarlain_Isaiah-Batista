import pygame

import sys
from itertools import combinations

from arcade_model import *


ROWS = 3

X_IMAGE = pygame.image.load("assets/x.png")
O_IMAGE = pygame.image.load("assets/o.png")

# resize images
X_IMAGE = pygame.transform.scale(X_IMAGE, (WIDTH // ROWS, WIDTH // ROWS))
O_IMAGE = pygame.transform.scale(O_IMAGE, (WIDTH // ROWS, WIDTH // ROWS))

# Colors
LINE_COLOR = (128, 128, 128)  # Light gray for grid lines
BG_COLOR = (0, 0, 0)  # Black background


# VIEW
class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.color = BG_COLOR  # Initially same as background
        self.piece = None

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, WIDTH / ROWS, WIDTH / ROWS))
        if self.piece:
            WIN.blit(self.piece.image, (self.x, self.y))


def update_display(win, grid, rows, width):
    win.fill(BG_COLOR)  # Clear the screen with background color
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            grid[i].append(node)
    return grid


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


# MODEL
def check_winner(grid, player):
    for i in range(ROWS):
        if all(
            [
                grid[i][j].piece is not None and grid[i][j].piece.image == player
                for j in range(ROWS)
            ]
        ):
            return True
        if all(
            [
                grid[j][i].piece is not None and grid[j][i].piece.image == player
                for j in range(ROWS)
            ]
        ):
            return True
    if all(
        [
            grid[i][i].piece is not None and grid[i][i].piece.image == player
            for i in range(ROWS)
        ]
    ):
        return True
    if all(
        [
            grid[i][ROWS - i - 1].piece is not None
            and grid[i][ROWS - i - 1].piece.image == player
            for i in range(ROWS)
        ]
    ):
        return True
    return False


def check_draw(grid):

    if all([grid[i][j].piece is not None for i in range(ROWS) for j in range(ROWS)]):
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

            # CONTROLLER
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // (WIDTH // ROWS)
                col = x // (WIDTH // ROWS)

                if make_move(grid, row, col, currPlayer):
                    # if move is valid, change player
                    change_player()

        update_display(SCREEN, grid, ROWS, WIDTH)
