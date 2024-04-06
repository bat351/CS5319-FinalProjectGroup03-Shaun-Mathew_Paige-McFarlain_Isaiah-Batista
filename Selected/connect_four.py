# sources: https://github.com/KeithGalli/Connect4-Python/blob/master/connect4.py
# 		 https://www.youtube.com/watch?v=SDz3P_Ctm7U

import numpy as np
import math
import pygame
import sys

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
SQUARESIZE = 100

ROW_COUNT = 6
COLUMN_COUNT = 7
EVEN = 0
ODD = 1

SIZE = 800

SQUARESIZE = SIZE/COLUMN_COUNT

RADIUS = int(SQUARESIZE/2 - 5)



SCREEN = pygame.display.set_mode((800, 800))

def create_board():
	board = np.zeros((6,7))
	return board

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_valid_location(board, col):
	return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
	for i in range(ROW_COUNT):
		if board[i][col] == 0:
			return i

def winning_move(board, piece):
	# horizontal
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# vertical
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# positively sloped
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# negatively sloped
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(SCREEN, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(SCREEN, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			if board[r][c] == 1:
				pygame.draw.circle(SCREEN, RED, (int(c*SQUARESIZE+SQUARESIZE/2), SIZE-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2:
				pygame.draw.circle(SCREEN, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), SIZE-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)

def print_board(board):
	print(np.flip(board, 0))
	print("\n")

def  connect_4():

	board = create_board()
	print(board)
	game_over = False
	turn = 0

	pygame.init()


	draw_board(board)
	pygame.display.update()
	myfont = pygame.font.SysFont("monospace", 75)

	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEMOTION:
				pygame.draw.rect(SCREEN, BLACK, (0,0,SIZE,SQUARESIZE))
				posx = event.pos[0]
				if turn == 0:
					pygame.draw.circle(SCREEN, RED, (posx, int(SQUARESIZE/2)), RADIUS)
				else:
					pygame.draw.circle(SCREEN, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
			pygame.display.update()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.draw.rect(SCREEN, BLACK, (0,0, SIZE, SQUARESIZE))

				# Player 1 input
				if turn == 0:
					posx = event.pos[0]
					col = int(math.floor(posx/SQUARESIZE))
					if is_valid_location(board, col):
						row = get_next_open_row(board, col)
						drop_piece(board, row, col, 1)
						if winning_move(board, 1):
							return 'Player_1'
				# Player 2 input
				else:
					posx = event.pos[0]
					col = int(math.floor(posx/SQUARESIZE))
					if is_valid_location(board, col):
						row = get_next_open_row(board, col)
						drop_piece(board, row, col, 2)
						if winning_move(board, 2):
							return 'Player_2'
				print_board(board)
				draw_board(board)
				turn += 1
				turn = turn % 2

				if game_over:
					pygame.time.wait(3000)
