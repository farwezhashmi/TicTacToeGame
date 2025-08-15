'''Tic-Tac-Toe Game development with using Python3 By Shaik Pharvej'''

def create_board():
    return [" " for _ in range(9)]

def display_board(board): #This is use to display the board
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}    1 | 2 | 3")
    print("---+---+---  ---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}    4 | 5 | 6")
    print("---+---+---  ---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}    7 | 8 | 9")
    print()

def player_move(board, player): #This func is use to take the  from player 
    while True:
        try:
            move = int(input(f"{player}, enter position (1-9): ")) - 1
            if move in range(9) and board[move] == " ":
                board[move] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Enter a number between 1 and 9.")

def check_win(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],   #These are the winnning position in rows
        [0,3,6], [1,4,7], [2,5,8],   #These are the winnning position in Columns
        [0,4,8], [2,4,6]              #These are the winnning position in diagonals
    ]

    for line in win_positions:
        if board[line[0]] == player and board[line[1]] == player and board[line[2]] == player:
            return True
    return False

def check_draw(board):
    return " " not in board

def play_two_player():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)
        player_move(board, current_player)

        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 {current_player} wins!")
            return
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            return
        current_player = "O" if current_player == "X" else "X"

def main():
    print("Welcome to Text Tic-Tac-Toe!")
    print("Game board positions are numbered as follows:")
    print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9\n")
    
    while True:
        play_two_player()
        again = input("Play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing!\nBY SHAIK PHARVEJ :)")
            break

if __name__ == "__main__":
    main()
