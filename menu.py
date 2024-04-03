import pygame, sys
from button import Button
from checkers import checkers

pygame.init()

SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def win(winner):
     while True:
        WINNER_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        WINNER = winner + " wins"
        pygame.display.set_caption(WINNER)
        WINNER_TEXT = get_font(100).render(WINNER, True, "White")
        WINNER_RECT = WINNER_TEXT.get_rect(center=(400, 400))
        SCREEN.blit(WINNER_TEXT, WINNER_RECT)
        WINNER_BACK = Button(pos=(400, 600), input="MAIN MENU", font=get_font(50), base="White", hover="Green")

        WINNER_BACK.changeColor(WINNER_MOUSE_POS)
        WINNER_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WINNER_BACK.checkForInput(WINNER_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def play_checkers():
    pygame.display.set_caption("Checkers")
    SCREEN.fill("black")
    win(checkers(800, 8, 12, 12))
    
    
def player_stats():
    while True:
        PLAYER_STATS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        PLAYER_STATS_TEXT = get_font(30).render("This is the PLAYER STATISTICS screen", True, "Black")
        PLAYER_STATS_RECT = PLAYER_STATS_TEXT.get_rect(center=(400, 400))
        SCREEN.blit(PLAYER_STATS_TEXT, PLAYER_STATS_RECT)

        PLAYER_STATS_BACK = Button(pos=(400, 600), input="BACK", font=get_font(75), base="Black", hover="Green")

        PLAYER_STATS_BACK.changeColor(PLAYER_STATS_MOUSE_POS)
        PLAYER_STATS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAYER_STATS_BACK.checkForInput(PLAYER_STATS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        CHECKERS_BUTTON = Button(pos=(400, 250), 
                            input="CHECKERS", font=get_font(75), base="#d7fcd4", hover="White")
        PLAYER_STATS_BUTTON = Button(pos=(400, 400), 
                            input="PLAYER STATS", font=get_font(75), base="#d7fcd4", hover="White")
        QUIT_BUTTON = Button(pos=(400, 550), 
                            input="QUIT", font=get_font(75), base="#d7fcd4", hover="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [CHECKERS_BUTTON, PLAYER_STATS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHECKERS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_checkers()
                if PLAYER_STATS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    player_stats()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()