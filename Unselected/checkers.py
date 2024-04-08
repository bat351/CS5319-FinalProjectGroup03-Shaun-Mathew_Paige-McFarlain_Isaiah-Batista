# reference: https://medium.com/analytics-vidhya/checkers-python-eff2786b985b
import pygame
import sys
from itertools import combinations
from business_logic import *
from checkers_logic import *

# USER INTERFACE LAYER
pygame.init()
SCREEN = pygame.display.set_mode((800, 800))


def update_display(SCREEN, grid, rows, width):
    for row in grid:
        for spot in row:
            spot.draw(SCREEN)
    draw_grid(SCREEN, rows, width)
    pygame.display.update()


def draw_grid(SCREEN, rows, width):
    gap = width // ROWS
    for i in range(rows):
        pygame.draw.line(SCREEN, (100, 100, 100), (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(SCREEN, (100, 100, 100), (j * gap, 0), (j * gap, width))


def highlight_moves(currPos, grid):
    positions = generatePotentialMoves(currPos, grid)
    for position in positions:
        Column, Row = position
        grid[Column][Row].colour = (0, 200, 0)


def highlight(currNode, grid, prevHighlight):
    Column, Row = currNode
    grid[Column][Row].colour = (200, 0, 0)
    if prevHighlight:
        resetColors(grid, prevHighlight)
    highlight_moves(currNode, grid)
    return (Column, Row)


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
                    currNode = getNode(grid, ROWS, WIDTH)
                    ClickedPositionColumn, ClickedPositionRow = currNode
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
                                currNode,
                            )
                            if currMove == prevMove and prevMove == "B":
                                TOTALRED = TOTALRED - 1
                            elif currMove == prevMove and prevMove == "R":
                                TOTALBLACK = TOTALBLACK - 1
                            
                            # Access data layer via menu layer
                            else:
                                change_player()

                    elif highlightedPiece == currNode:
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
                                    currNode, grid, highlightedPiece
                                )

                update_display(SCREEN, grid, ROWS, WIDTH)


# checkers(WIDTH, ROWS, TOTALRED, TOTALBLACK)
