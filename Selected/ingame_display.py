import pygame

def currentplayer(player, screen):
	position = (10, 10)
	textfont = pygame.font.SysFont('Corbel',50)
	text = textfont.render(f"Player{player}", True, "white")
	screen.blit(text, position)

def winner(player, screen):
	position = (350,350)
	textfont = pygame.font.SysFont('Corbel',100)
	text = textfont.render(f"Player{player} Wins", True, "white")
	text_rect = text.get_rect(center=position)
	screen.fill("black")
	screen.blit(text, text_rect)


