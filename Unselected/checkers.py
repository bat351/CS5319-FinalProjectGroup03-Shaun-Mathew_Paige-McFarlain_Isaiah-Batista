# reference: https://medium.com/analytics-vidhya/checkers-python-eff2786b985b
import pygame
import sys
from itertools import combinations
from business_logic import *


# DATA LAYER
WIDTH = 800
ROWS = 8

RED = pygame.image.load("assets/red.png")
BLACK = pygame.image.load("assets/black.png")

REDKING = pygame.image.load("assets/redKing.png")
BLACKKING = pygame.image.load("assets/blackKing.png")

TOTALBLACK = 12
TOTALRED = 12

# USER INTERFACE LAYER
pygame.init()
SCREEN = pygame.display.set_mode((800, 800))

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.colour = (255, 255, 255)
        self.piece = None

    def draw(self, SCREEN):
        pygame.draw.rect(
            SCREEN, self.colour, (self.x, self.y, WIDTH / ROWS, WIDTH / ROWS)
        )
        if self.piece:
            SCREEN.blit(self.piece.image, (self.x, self.y))


def update_display(SCREEN, grid, rows, width):
    for row in grid:
        for spot in row:
            spot.draw(SCREEN)
    draw_grid(SCREEN, rows, width)
    pygame.display.update()


def make_grid(rows, width):
    grid = []
    gap = width // rows
    count = 0
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            if abs(i - j) % 2 == 0:
                node.colour = (100, 100, 100)
            if (abs(i + j) % 2 == 0) and (i < 3):
                node.piece = Piece("R")
            elif (abs(i + j) % 2 == 0) and i > 4:
                node.piece = Piece("B")
            count += 1
            grid[i].append(node)
    return grid


def draw_grid(SCREEN, rows, width):
    # SCREEN.blit(surface, (0, 0))
    gap = width // ROWS
    for i in range(rows):
        pygame.draw.line(SCREEN, (100, 100, 100), (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(SCREEN, (100, 100, 100), (j * gap, 0), (j * gap, width))


class Piece:
    def __init__(self, team):
        self.team = team
        self.image = RED if self.team == "R" else BLACK
        self.type = None

    def draw(self, x, y):
        SCREEN.blit(self.image, (x, y))


def getNode(grid, rows, width):
    gap = width // rows
    RowX, RowY = pygame.mouse.get_pos()
    Row = RowX // gap
    Col = RowY // gap
    return (Col, Row)


def resetColours(grid, node):
    positions = generatePotentialMoves(node, grid)
    positions.append(node)

    for colouredNodes in positions:
        nodeX, nodeY = colouredNodes
        grid[nodeX][nodeY].colour = (
            (100, 100, 100) if abs(nodeX - nodeY) % 2 == 0 else (255, 255, 255)
        )


def HighlightpotentialMoves(piecePosition, grid):
    positions = generatePotentialMoves(piecePosition, grid)
    for position in positions:
        Column, Row = position
        grid[Column][Row].colour = (0, 200, 0)

# BUSINESS LOGIC LAYER
def opposite(team):
    return "R" if team == "B" else "B"


def generatePotentialMoves(nodePosition, grid):
    checker = lambda x, y: x + y >= 0 and x + y < 8
    positions = []
    column, row = nodePosition
    if grid[column][row].piece:
        vectors = (
            [[1, -1], [1, 1]]
            if grid[column][row].piece.team == "R"
            else [[-1, -1], [-1, 1]]
        )
        if grid[column][row].piece.type == "KING":
            vectors = [[1, -1], [1, 1], [-1, -1], [-1, 1]]
        for vector in vectors:
            columnVector, rowVector = vector
            if checker(columnVector, column) and checker(rowVector, row):
                # grid[(column+columnVector)][(row+rowVector)].colour=ORANGE
                if not grid[(column + columnVector)][(row + rowVector)].piece:
                    positions.append((column + columnVector, row + rowVector))
                elif grid[column + columnVector][row + rowVector].piece and grid[
                    column + columnVector
                ][row + rowVector].piece.team == opposite(grid[column][row].piece.team):

                    if (
                        checker((2 * columnVector), column)
                        and checker((2 * rowVector), row)
                        and not grid[(2 * columnVector) + column][
                            (2 * rowVector) + row
                        ].piece
                    ):
                        positions.append(
                            (2 * columnVector + column, 2 * rowVector + row)
                        )

    return positions

def highlight(ClickedNode, Grid, OldHighlight):
    Column, Row = ClickedNode
    Grid[Column][Row].colour = (200, 0, 0)
    if OldHighlight:
        resetColours(Grid, OldHighlight)
    HighlightpotentialMoves(ClickedNode, Grid)
    return (Column, Row)


# BUSINESS LOGIC LAYER
def move(grid, piecePosition, newPosition, TOTALBLACK, TOTALRED):
    resetColours(grid, piecePosition)
    newColumn, newRow = newPosition
    oldColumn, oldRow = piecePosition

    piece = grid[oldColumn][oldRow].piece
    grid[newColumn][newRow].piece = piece
    grid[oldColumn][oldRow].piece = None

    if newColumn == 7 and grid[newColumn][newRow].piece.team == "R":
        grid[newColumn][newRow].piece.type = "KING"
        grid[newColumn][newRow].piece.image = REDKING
    if newColumn == 0 and grid[newColumn][newRow].piece.team == "B":
        grid[newColumn][newRow].piece.type = "KING"
        grid[newColumn][newRow].piece.image = BLACKKING
    if abs(newColumn - oldColumn) == 2 or abs(newRow - oldRow) == 2:
        grid[int((newColumn + oldColumn) / 2)][int((newRow + oldRow) / 2)].piece = None

        return grid[newColumn][newRow].piece.team
    return opposite(grid[newColumn][newRow].piece.team)


def checkers(WIDTH, ROWS, TOTALBLACK, TOTALRED):
    while True:
        grid = make_grid(ROWS, WIDTH)
        highlightedPiece = None
        currMove = "B"

        while True:

            if TOTALBLACK == 0:
                return "Player 1"
            if TOTALRED == 0:
                return "Player 2"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("EXIT SUCCESSFUL")
                    pygame.quit()
                    sys.exit()

              
                if event.type == pygame.MOUSEBUTTONDOWN:  # and not pause
                    clickedNode = getNode(grid, ROWS, WIDTH)
                    ClickedPositionColumn, ClickedPositionRow = clickedNode
                    if grid[ClickedPositionColumn][ClickedPositionRow].colour == (
                        0,
                        200,
                        0,
                    ):
                        if highlightedPiece:
                            pieceColumn, pieceRow = highlightedPiece
                        if currMove == grid[pieceColumn][pieceRow].piece.team:
                            resetColours(grid, highlightedPiece)
                            prevMove = currMove
                            currMove = move(
                                grid,
                                highlightedPiece,
                                clickedNode,
                                TOTALBLACK,
                                TOTALRED,
                            )
                            if currMove == prevMove and prevMove == "B":
                                TOTALRED = TOTALRED - 1
                            elif currMove == prevMove and prevMove == "R":
                                TOTALBLACK = TOTALBLACK - 1
                            
                            # Access data layer via menu layer
                            else:
                                change_player()

                    elif highlightedPiece == clickedNode:
                        pass
                    else:
                        if grid[ClickedPositionColumn][ClickedPositionRow].piece:
                            if (
                                currMove
                                == grid[ClickedPositionColumn][
                                    ClickedPositionRow
                                ].piece.team
                            ):
                                highlightedPiece = highlight(
                                    clickedNode, grid, highlightedPiece
                                )

                update_display(SCREEN, grid, ROWS, WIDTH)


# checkers(WIDTH, ROWS, TOTALRED, TOTALBLACK)
