import random

print(
            "Welcome to Tic-Tac-Toe. Grid positions are given as Cartesian coordinates, with 0,0 being the bottom left space."
            )
while True:
        HUM = input("X or O?")
            
        if HUM != 'X' and HUM != 'O' and HUM != 'x' and HUM != 'o':
                continue
        else:
                if HUM == 'x' or HUM == 'X':
                    HUM = 'X'
                    COMP = 'O'
                if HUM == 'o' or HUM == 'O':
                    HUM = 'O'
                    COMP = 'X'
                print(f'{HUM}\'s it is!')
                break




def init_board():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

game_board = init_board()

def board_visual(board):
    separator = 0
    for row in board:
        print("|".join(row))
        if separator < 2: # tried to do this with board.index(row) but with identical rows, did not work
            print("-----")
            separator += 1

board_visual(game_board)

def game_move(player, turn):

    while True:
        if player is COMP:
            target = comp_target()
        else:
            target = hum_target()
        
        if board[target] == ' ':
                board[target] = player
                break
        else:
            print('Already taken, choose an empty space')


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

        if col != 0 and col != 1 and col != 2 and row != 0 and row != and row != 2: 
            print(f'{col},{row} is an invalid space')
            continue
        else
            break
    return row, col

def comp_target():
    col = random.randint(0,2)
    row = random.randint(0,2)

def active_player():
    if HUM == 'X':
        active = COMP if turn % 2 == 0 else HUM
    else:
        active  = HUM if turn % 2 == 0 else HUM
    return active

def term_conditions(player, turn):
    if turn > 4:
        for combo in winning_combos:
            score = 0
            for index in combo:
                if boxes[index] == player:
                    score +=1
                if score == 3:
                    return 'win'

        if turn == 9:
            return 'tie'

def play(player, turn):
    while True:
        game_move(player,turn)
        print_board()
        result = term_conditions(player, turn)
        if result == 'win':
            print('Congratulations

# Test
test_board = init_board()
board_visual(test_board)
