import pygame
import random
import sys
from itertools import combinations

from checkers import ROWS, WIDTH

WIDTH = 800
ROWS = 3

X_IMAGE = pygame.image.load('assets/x.png')
O_IMAGE = pygame.image.load('assets/o.png')

# pause = False

pygame.init()
WIN = pygame.display.set_mode((WIDTH, WIDTH))
surface = pygame.Surface((WIDTH, WIDTH), pygame.SRCALPHA)
pygame.display.set_caption('Tic Tac Toe')

priorMoves = []

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.colour = (255, 255, 255)
        self.piece = None

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.colour, (self.x, self.y, WIDTH / ROWS, WIDTH / ROWS))
        if self.piece:
            WIN.blit(self.piece.image, (self.x, self.y))

def update_display(win, grid, rows, width):
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

def make_grid(rows, width):
    grid = []
    gap = width // rows
    count = 0
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            grid[i].append(node)
            count += 1
    return grid

def draw_grid(win, rows, width):
    WIN.blit(surface, (0, 0))
    gap = width // ROWS
    for i in range(rows):
        pygame.draw.line(win, (128, 128, 128), (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, (128, 128, 128), (j * gap, 0), (j * gap, width))

# def draw_pause():
#     pygame.draw.rect(surface, (128, 128, 128, 150), [0, 0, WIDTH, WIDTH])
#     WIN.blit(surface, (0, 0))

class Piece:
    def __init__(self, image):
        self.image = image

def make_move(grid, row, col, player):
    if grid[row][col].piece is None:
        if player == 'X':
            grid[row][col].piece = Piece(X_IMAGE)
        else:
            grid[row][col].piece = Piece(O_IMAGE)
        return True
    return False

def check_winner(grid, player):
    for i in range(ROWS):
        if all([grid[i][j].piece is not None and grid[i][j].piece.image == player for j in range(ROWS)]):
            return True
        if all([grid[j][i].piece is not None and grid[j][i].piece.image == player for j in range(ROWS)]):
            return True
    if all([grid[i][i].piece is not None and grid[i][i].piece.image == player for i in range(ROWS)]):
        return True
    if all([grid[i][ROWS - i - 1].piece is not None and grid[i][ROWS - i - 1].piece.image == player for i in range(ROWS)]):
        return True
    return False

def tic_tac_toe(WIDTH,ROWS):
    grid = make_grid(ROWS, WIDTH)
    currMove = 'X'

    while True:

        if check_winner(grid, X_IMAGE):
            return 'Player 1'
        elif check_winner(grid, O_IMAGE):
            return 'Player 2'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('EXIT SUCCESSFUL')
                pygame.quit()
                sys.exit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
            #         if pause:
            #             pause = False
            #         else:
            #             pause = True
            #              draw_pause()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // (WIDTH // ROWS)
                col = x // (WIDTH // ROWS)

                if  make_move(grid, row, col, currMove):
                    if currMove == 'X':
                        currMove = 'O'
                    else:
                        currMove = 'X'
                    priorMoves.append((row, col))


        update_display(WIN, grid, ROWS, WIDTH)
