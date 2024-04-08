import pygame, sys
from button import Button
from arcade_model import CHECKERS_WINS, CONNECT_4_WINS, TIC_TAC_TOE_WINS, SCREEN


# MODEL
pygame.init()

pygame.display.set_caption("Player Statistics")


class player_stats:
    def __init__(self):
        player_stats.display_player_stats()

    def display_player_stats():

        while True:
            MOUSE_POS = pygame.mouse.get_pos()

            # VIEW
            SCREEN.fill("black")

            TITLE = pygame.font.Font("assets/font.ttf", 30).render(
                "PLAYER STATISTICS", True, "White"
            )
            TRECT = TITLE.get_rect(center=(400, 75))
            SCREEN.blit(TITLE, TRECT)

            P1_LABEL = pygame.font.Font("assets/font.ttf", 25).render(
                "P1 Wins:", True, "White"
            )
            P1_RECT = P1_LABEL.get_rect(topleft=(275, 150))
            SCREEN.blit(P1_LABEL, P1_RECT)

            P2_LABEL = pygame.font.Font("assets/font.ttf", 25).render(
                "P2 Wins:", True, "White"
            )
            P2_RECT = P2_LABEL.get_rect(topleft=(525, 150))
            SCREEN.blit(P2_LABEL, P2_RECT)

            CHECKERS_LABEL = pygame.font.Font("assets/font.ttf", 20).render(
                "Checkers", True, "White"
            )
            CHECKERS_RECT = CHECKERS_LABEL.get_rect(topleft=(25, 250))
            SCREEN.blit(CHECKERS_LABEL, CHECKERS_RECT)

            P1_CHECKERS_WINS = pygame.font.Font("assets/font.ttf", 20).render(
                str(CHECKERS_WINS[0]), True, "White"
            )
            P1_CHECKERS_WINS_RECT = P1_CHECKERS_WINS.get_rect(topleft=(275, 250))
            SCREEN.blit(P1_CHECKERS_WINS, P1_CHECKERS_WINS_RECT)

            P2_CHECKERS_WINS = pygame.font.Font("assets/font.ttf", 20).render(
                str(CHECKERS_WINS[1]), True, "White"
            )
            P2_CHECKERS_WINS_RECT = P2_CHECKERS_WINS.get_rect(topleft=(525, 250))
            SCREEN.blit(P2_CHECKERS_WINS, P2_CHECKERS_WINS_RECT)

            CONNECT_4_LABEL = pygame.font.Font("assets/font.ttf", 20).render(
                "Connect-4", True, "White"
            )
            CONNECT_4_RECT = CONNECT_4_LABEL.get_rect(topleft=(25, 375))
            SCREEN.blit(CONNECT_4_LABEL, CONNECT_4_RECT)

            P1_CONNECT_4_WINS = pygame.font.Font("assets/font.ttf", 20).render(
                str(CONNECT_4_WINS[0]), True, "White"
            )
            P1_CONNECT_4_WINS_RECT = P1_CONNECT_4_WINS.get_rect(topleft=(275, 375))
            SCREEN.blit(P1_CONNECT_4_WINS, P1_CONNECT_4_WINS_RECT)

            P2_CONNECT_4_WINS = pygame.font.Font("assets/font.ttf", 20).render(
                str(CONNECT_4_WINS[1]), True, "White"
            )
            P2_CONNECT_4_WINS_RECT = P2_CONNECT_4_WINS.get_rect(topleft=(525, 375))
            SCREEN.blit(P2_CONNECT_4_WINS, P2_CONNECT_4_WINS_RECT)

            TIC_TAC_TOE_LABEL = pygame.font.Font("assets/font.ttf", 20).render(
                "Tic-Tac-Toe", True, "White"
            )
            TIC_TAC_TOE_RECT = TIC_TAC_TOE_LABEL.get_rect(topleft=(25, 500))
            SCREEN.blit(TIC_TAC_TOE_LABEL, TIC_TAC_TOE_RECT)

            P1_TIC_TAC_TOE_WINS = pygame.font.Font("assets/font.ttf", 20).render(
                str(TIC_TAC_TOE_WINS[0]), True, "White"
            )
            P1_TIC_TAC_TOE_WINS_RECT = P1_TIC_TAC_TOE_WINS.get_rect(topleft=(275, 500))
            SCREEN.blit(P1_TIC_TAC_TOE_WINS, P1_TIC_TAC_TOE_WINS_RECT)

            P2_TIC_TAC_TOE_WINS = pygame.font.Font("assets/font.ttf", 20).render(
                str(TIC_TAC_TOE_WINS[1]), True, "White"
            )
            P2_TIC_TAC_TOE_WINS_RECT = P2_TIC_TAC_TOE_WINS.get_rect(topleft=(525, 500))
            SCREEN.blit(P2_TIC_TAC_TOE_WINS, P2_TIC_TAC_TOE_WINS_RECT)

            TOTAL_WINS_LABEL = pygame.font.Font("assets/font.ttf", 22).render(
                "Total Wins", True, "White"
            )
            TOTAL_WINS_RECT = TOTAL_WINS_LABEL.get_rect(topleft=(25, 625))
            SCREEN.blit(TOTAL_WINS_LABEL, TOTAL_WINS_RECT)

            P1_TOTAL_WINS = pygame.font.Font("assets/font.ttf", 22).render(
                str(CHECKERS_WINS[0] + CONNECT_4_WINS[0] + TIC_TAC_TOE_WINS[0]),
                True,
                "White",
            )
            P1_TOTAL_WINS_RECT = P1_TOTAL_WINS.get_rect(topleft=(275, 625))
            SCREEN.blit(P1_TOTAL_WINS, P1_TOTAL_WINS_RECT)

            P2_TOTAL_WINS = pygame.font.Font("assets/font.ttf", 22).render(
                str(CHECKERS_WINS[1] + CONNECT_4_WINS[1] + TIC_TAC_TOE_WINS[1]),
                True,
                "White",
            )
            P2_TOTAL_WINS_RECT = P2_TOTAL_WINS.get_rect(topleft=(525, 625))
            SCREEN.blit(P2_TOTAL_WINS, P2_TOTAL_WINS_RECT)

            BACK = Button(
                pos=(400, 750),
                input="Return to Main Menu",
                font=pygame.font.Font("assets/font.ttf", 30),
                base="White",
                hover="Green",
            )
            BACK.changeColor(MOUSE_POS)
            BACK.update(SCREEN)

            # CONTROLLER
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK.checkForInput(MOUSE_POS):
                        return

            pygame.display.update()
