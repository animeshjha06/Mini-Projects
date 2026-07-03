def print_board(board):
    for i , row in enumerate(board):
        row_str = "  "
        for j, col in enumerate(row):
            row_str += col
            if j != len(row)-1:
                row_str += " | "
        
        print(row_str)
        if i != len(board)-1:
            print("-------------")

def get_move(turn,board):
    while True:
        row = input("Row : ")
        col = input("Column : ")
        try:
            row = int(row)
            col = int(col)
        except:
            print("Wrong input ! Numbers only...")
            continue

        if row < 1 or row >len(board):
            print("Invalid row, try again")
        elif col<1 or col >len(board):
            print("Invalid column, try again")
        elif board[row - 1][col -1] != ' ':
            print("Already taken, try again")
        else:
            break
        
    board[row - 1][col -1] = turn

def check_winner(turn, board):
    lines = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],

        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],

        [(0,0),(1,1),(2,2)],
        [(2,0),(1,1),(0,2)]
    ]

    for line in lines:
        win = True
        for pos in line:
            row,col = pos
            if board[row][col] != turn:
                win = False
                break

        if win:
            return True
    
    return False

#  Tic Tac Toe Game ----------------------------

board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

turn = "X"
turn_number = 0
print_board(board)

while turn_number < 9:
    print()
    print("It is player",turn," turn!!")

    get_move(turn,board)
    turn_number += 1

    print_board(board)

    if check_winner(turn,board):
        break

    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'

if turn_number == 9:
    print("Match Tied!!")
else:
    print("The winner is player",turn)