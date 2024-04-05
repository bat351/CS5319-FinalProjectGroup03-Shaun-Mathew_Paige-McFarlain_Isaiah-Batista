import pygame, sys
from button import Button
from checkers import checkers
from tic_tac_toe import tic_tac_toe

pygame.init()

SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

P1_WINS = 0
P2_WINS = 0


def win(winner):
     if winner == 'Player 1':
         P1_WINS +=1
     elif winner == 'Player 2':
         P2_WINS +=1
     while True:
        WINNER_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        WINNER = winner + " wins"
        pygame.display.set_caption(WINNER)
        WINNER_TEXT = pygame.font.Font("assets/font.ttf", 50).render(WINNER, True, "White")
        WINNER_RECT = WINNER_TEXT.get_rect(center=(400, 400))
        SCREEN.blit(WINNER_TEXT, WINNER_RECT)
        WINNER_BACK = Button(pos=(400, 600), input="MAIN MENU", font=pygame.font.Font("assets/font.ttf", 25), base="White", hover="Green")

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

def play_tic_tac_toe():
    pygame.display.set_caption("Tic-Tac-Toe")
    SCREEN.fill("black")
    win(tic_tac_toe(800, 3))


def player_stats():
    while True:
        PLAYER_STATS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        PLAYER_STATS_TEXT1 = pygame.font.Font("assets/font.ttf", 25).render("This is the", True, "Black")
        PLAYER_STATS_RECT1 = PLAYER_STATS_TEXT1.get_rect(center=(400, 400))
        SCREEN.blit(PLAYER_STATS_TEXT1, PLAYER_STATS_RECT1)
        PLAYER_STATS_TEXT2 = pygame.font.Font("assets/font.ttf", 25).render("PLAYER STATISTICS SCREEN", True, "Black")
        PLAYER_STATS_RECT2 = PLAYER_STATS_TEXT2.get_rect(center=(400, 450))
        SCREEN.blit(PLAYER_STATS_TEXT2, PLAYER_STATS_RECT2)

        PLAYER_STATS_BACK = Button(pos=(400, 600), input="BACK", font=pygame.font.Font("assets/font.ttf", 50), base="Black", hover="Green")

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

        MENU_TEXT = pygame.font.Font("assets/font.ttf", 60).render("MAIN MENU", True, "Grey")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        CHECKERS_BUTTON = Button(pos=(400, 250),
                            input="CHECKERS", font=pygame.font.Font("assets/font.ttf", 40), base="White", hover="Green")
        TIC_TAC_TOE_BUTTON = Button(pos=(400, 325),
                            input="TIC-TAC-TOE", font=pygame.font.Font("assets/font.ttf", 40), base="White", hover="Green")
        PLAYER_STATS_BUTTON = Button(pos=(400, 400),
                            input="PLAYER STATS", font=pygame.font.Font("assets/font.ttf", 40), base="White", hover="Green")
        QUIT_BUTTON = Button(pos=(400, 550),
                            input="QUIT", font=pygame.font.Font("assets/font.ttf", 40), base="White", hover="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [CHECKERS_BUTTON, TIC_TAC_TOE_BUTTON  ,PLAYER_STATS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHECKERS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_checkers()
                if TIC_TAC_TOE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_tic_tac_toe()
                if PLAYER_STATS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    player_stats()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
