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
    # SCREEN.blit(surface, (0, 0))
    gap = width // ROWS
    for i in range(rows):
        pygame.draw.line(SCREEN, (100, 100, 100), (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(SCREEN, (100, 100, 100), (j * gap, 0), (j * gap, width))


def HighlightpotentialMoves(piecePosition, grid):
    positions = generatePotentialMoves(piecePosition, grid)
    for position in positions:
        Column, Row = position
        grid[Column][Row].colour = (0, 200, 0)


def highlight(ClickedNode, Grid, OldHighlight):
    Column, Row = ClickedNode
    Grid[Column][Row].colour = (200, 0, 0)
    if OldHighlight:
        resetColours(Grid, OldHighlight)
    HighlightpotentialMoves(ClickedNode, Grid)
    return (Column, Row)


# BUSINESS LOGIC LAYER

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
