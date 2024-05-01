import random
import os.path
import json

random.seed()


def draw_board(board):
    print('\t' + "-" * 13)
    for row in board:
        print('\t' + "| {} | {} | {} |".format(row[0], row[1], row[2]))
        print('\t' + "-" * 13)
    pass


def welcome(board):
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print("The board layout is show below:")
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")
    pass


def initialise_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board


def get_player_move(board):
    draw_board(board)
    while True:
        try:
            square = int(input(" " * 20 + "1 2 3\n"
                               + " " * 20 + "4 5 6\n"
                               + "Choose your square: 7 8 9 : "))

            if 1 <= square <= 9:
                row = (square - 1) // 3
                col = (square - 1) % 3
                if board[row][col] == ' ':
                    break
                else:
                    print("Square not empty")
                    draw_board(board)

            else:
                print("Square number must be between 1 and 9")
                draw_board(board)

            if square == 'q':
                print('Player quits the game')
        except ValueError:
            print("Invalid number")
            draw_board(board)
    return row, col


def choose_computer_move(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board_copy = [row[:] for row in board]
                board_copy[row][col] = 'O'
                if check_for_win(board_copy, 'O'):
                    return row, col

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board_copy = [row[:] for row in board]
                board_copy[row][col] = 'X'
                if check_for_win(board_copy, 'X'):
                    return row, col

    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    if empty_cells:
        move = random.choice(empty_cells)
        return move
    else:
        return None


def check_for_win(board, mark):
    for row in board:
        if all(cell == mark for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True

    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True

    return False


def check_for_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def play_game(board):
    print("The game begins")
    initialise_board(board)

    while True:
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = 'X'
        draw_board(board)

        if check_for_win(board, 'X'):
            print('You win!')
            return 1

        if check_for_draw(board):
            print("It's a draw.")
            return 0

        computer_row, computer_col = choose_computer_move(board)
        board[computer_row][computer_col] = 'O'
        print(f"Computer plays Row {computer_row} Column {computer_col}")

        if check_for_win(board, 'O'):
            print('You lose!')
            return -1

        if check_for_draw(board):
            print("It's a draw.")
            return 0


def menu():
    print("Enter one of the following options:")
    print("\t1 - Play the game")
    print("\t2 - Save your score in the leaderboard")
    print("\t3 - Load and display the leaderboard")
    print("\tq - End the program")
    choice = input("1, 2, 3, or q? ").lower()
    while choice not in ['1', '2', '3', 'q']:
        print("Enter one of the following options:")
        print("\t1 - Play the game")
        print("\t2 - Save your score in the leaderboard")
        print("\t3 - Load and display the leaderboard")
        print("\tq - End the program")
        choice = input("1, 2, 3, or q? ").lower()
    return choice


def load_scores():
    filename = 'leaderboard.txt'
    leaders = {}
    try:
        with open(filename, 'r') as file:
            leaders = json.load(file)
    except FileNotFoundError:
        pass
    return leaders


def save_score(score):
    filename = 'leaderboard.txt'
    name = input("Enter your name: ")

    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            leaders = json.load(file)
    else:
        leaders = {}

    leaders[name] = score

    with open(filename, 'w') as file:
        json.dump(leaders, file)


def display_leaderboard(leaders):
    print("The current leaderboard is:")
    for name, score in sorted(leaders.items(), key=lambda item: item[1], reverse=True):
        print(f"{name}: {score}")
    pass
