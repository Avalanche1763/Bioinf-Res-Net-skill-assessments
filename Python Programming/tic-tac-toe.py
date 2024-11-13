import random

print(
        "Welcome to Tic-Tac-Toe. Grid positions are given as Cartesian coordinates, with 0,0 being the bottom left space. \n (HINT: X moves first)"
            )
def choose_symbol():
    while True:
            symbol_HUM = input("X or O?")
            
            if symbol_HUM != 'X' and symbol_HUM != 'O' and symbol_HUM != 'x' and symbol_HUM != 'o':
                    continue
            else:
                if symbol_HUM == 'x' or symbol_HUM == 'X':
                    symbol_HUM = 'X'
                    symbol_COMP = 'O'
                if symbol_HUM == 'o' or symbol_HUM == 'O':
                    symbol_HUM = 'O'
                    symbol_COMP = 'X'
                print(f'{symbol_HUM}\'s it is!')
                return [symbol_HUM, symbol_COMP]
                break




def init_board():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

game_board = init_board()

def board_visual(board):
    separator_iter = 0
    for row in board:
        print("|".join(row))
        if separator_iter < 2: # tried to do this with board.index(row) but with identical rows, did not work
            print("-----")
            separator_iter += 1

#board_visual(game_board)

def game_move(symbol_HUM, player, board):

    while True:
        if player is not symbol_HUM:
            target = comp_target()
        else:
            target = hum_target()
        
        if board[target[0]][target[1]] == ' ':
                board[target[0]][target[1]] = player
                break
        elif player is symbol_HUM:
            print('Already taken, choose an empty space')
## TRYING TO MAKE A TESTER FOR APPLYING XS AND OS TO THE BOARD
def target_tester(board):
    target = hum_target()
    if board[target[0]][target[1]] == ' ':
        board[target[0]][target[1]] = 'T'
    else:
        print('taken, choose again')

def hum_target():
    while True:
        
        col = input("X coord? (0,1,2)")
        row = input("Y coord? (0,1,2)")
        
        try:
            col = int(col)
            row = int(row)
        except ValueError:
            print('Please use integer values')
            continue

        if not ((col == 0 or col == 1 or col == 2) and (row == 0 or row == 1 or row == 2)): 
            print(f'{col},{row} is an invalid space')
            continue
        else:
            row = 2 - row
            break
    return [row, col]

def comp_target():
    col = random.randint(0,2)
    row = random.randint(0,2)
    return [row, col]
def active_player(act_HUM, act_COMP, turn):
    if act_HUM == 'X':
        active = act_COMP if turn % 2 == 0 else act_HUM
    else:
        active  = act_HUM if turn % 2 == 0 else act_COMP
    return active

def term_conditions(player, turn, board):
    if turn > 4:
        if any(all(cell == player for cell in row) for row in board) or \
           any(all(row[i] == player for row in board) for i in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3)):
               victory_message = player + " Wins!"
               return ['W',victory_message]

        if turn == 9:
            return ['T','Tie!']
        else:
            return['','']
    else:
        return['','']


def game_main(game_board, game_turn):
    # choose x's or o's
    players = choose_symbol()
    HUM = players[0]; COMP = players[1]

    while True:
        #get active player based on turn, 0 goes first!
        game_player = active_player(HUM, COMP, game_turn)
        game_move(HUM, game_player, game_board)
        print('\n')
        board_visual(game_board)
        result = term_conditions(game_player, game_turn, game_board)
        if (result[0] == 'W' or result[0] == 'T'):
            print(f'{result[1]}\n')
            break
        game_turn += 1

def active_tester():
    human = input('hum?')
    comp = input('comp?')
    turn = 1
    while True:
        active = active_player(human, comp, turn)
        print(f'{active}')
        turn += 1

        if turn == 10:
            break

# Test
game_board = init_board()
game_turn = 1

game_main(game_board, game_turn)
#active_tester()
#
#print(f'{test_coords}')
