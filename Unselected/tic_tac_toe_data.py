import pygame

WIDTH = 800
ROWS = 3

X_IMAGE = pygame.image.load("assets/x.png")
O_IMAGE = pygame.image.load("assets/o.png")

# resize images
X_IMAGE = pygame.transform.scale(X_IMAGE, (WIDTH // ROWS, WIDTH // ROWS))
O_IMAGE = pygame.transform.scale(O_IMAGE, (WIDTH // ROWS, WIDTH // ROWS))

# Colors
LINE_COLOR = (128, 128, 128)  # Light gray for grid lines
BG_COLOR = (0, 0, 0)  # Black background

priorMoves = []
