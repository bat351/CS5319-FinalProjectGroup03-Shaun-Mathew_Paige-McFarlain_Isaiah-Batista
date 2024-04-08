from data_layer import *

# Get and set functions for accessing the data layer
def change_player():
  global CURRENT_PLAYER
  if CURRENT_PLAYER == 'Player 1':
    CURRENT_PLAYER = 'Player 2'
  else:
    CURRENT_PLAYER = 'Player 1'

def get_player():
  return CURRENT_PLAYER

def reset_player():
  global CURRENT_PLAYER
  CURRENT_PLAYER = 'Player 1'


def win_update(winner, game):
    if game == "Checkers":
        if winner == "Player 1":
            CHECKERS_WINS[0] += 1
        elif winner == "Player 2":
            CHECKERS_WINS[1] += 1
    elif game == "Connect 4":
        if winner == "Player 1":
            CONNECT_4_WINS[0] += 1
        elif winner == "Player 2":
            CONNECT_4_WINS[1] += 1
    elif game == "Tic-Tac-Toe":
        if winner == "Player 1":
            TIC_TAC_TOE_WINS[0] += 1
        elif winner == "Player 2":
            TIC_TAC_TOE_WINS[1] += 1

       
def get_BG():
   return BG