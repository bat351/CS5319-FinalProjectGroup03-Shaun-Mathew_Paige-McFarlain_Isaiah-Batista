import pygame, sys
from button import Button
from checkers import checkers
# from menu import main_menu

SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Menu")
BG = pygame.image.load("../assets/Background.png")

PLAYER_STATS = 'Enabled'

def settings(current_game, PLAYER_STATS):
    while True:
        SCREEN.blit(BG, (0, 0))

        SETTINGS_MOUSE_POS = pygame.mouse.get_pos()

        SETTINGS_TEXT = pygame.font.Font("../assets/font.ttf", 50).render("SETTINGS", True, "Grey")
        SETTINGS_RECT = SETTINGS_TEXT.get_rect(center=(400, 100))

        PLAYER_STATS_BUTTON = Button(pos=(400, 250), 
                            input="Player Stats: " + PLAYER_STATS, font=pygame.font.Font("../assets/font.ttf", 25), base="White", hover="Green")
        RETURN_BUTTON = Button(pos=(400, 600), 
                            input="RETURN TO GAME", font=pygame.font.Font("../assets/font.ttf", 25), base="White", hover="Green")
        
        RESTART_BUTTON = Button(pos=(400, 650), 
                            input="RESTART GAME", font=pygame.font.Font("../assets/font.ttf", 25), base="White", hover="Green")
        MAIN_MENU_BUTTON = Button(pos=(400, 700), 
                            input="RETURN TO MAIN MENU", font=pygame.font.Font("../assets/font.ttf", 25), base="White", hover="Green")

        SCREEN.blit(SETTINGS_TEXT, SETTINGS_RECT)

        for button in [PLAYER_STATS_BUTTON, RETURN_BUTTON, RESTART_BUTTON, MAIN_MENU_BUTTON]:
            button.changeColor(SETTINGS_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAYER_STATS_BUTTON.checkForInput(SETTINGS_MOUSE_POS):
                    if PLAYER_STATS == 'Enabled':
                        PLAYER_STATS = 'Disabled'
                    else:
                        PLAYER_STATS = 'Enabled'
                if RETURN_BUTTON.checkForInput(SETTINGS_MOUSE_POS):
                    return(PLAYER_STATS)
                # if RESTART_BUTTON.checkForInput(SETTINGS_MOUSE_POS):
                    # if current_game == 'Checkers':
                        # checkers(800,800, 12, 12)
                # if MAIN_MENU_BUTTON.checkForInput(SETTINGS_MOUSE_POS):
                    # main_menu()
        pygame.display.update()

settings('Checkers', 'Enabled')