import pygame
from tic_tac_toe_data import *

class Piece:
    def __init__(self, image):
        self.image = image


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


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            grid[i].append(node)
    return grid

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

