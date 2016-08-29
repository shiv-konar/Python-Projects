import os
import random


def display_board(board):
    os.system('clear')
    print '   |   |'
    print ' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9]
    print '   |   |'
    print '-----------'
    print '   |   |'
    print ' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6]
    print '   |   |'
    print '-----------'
    print '   |   |'
    print ' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3]
    print '   |   |'


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input("Player 1: Do you want to be X or O: ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input("Choose your next position (1-9): ")
    return int(position)


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, marker):
    return ((board[7] == board[8] == board[9] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[1] == board[2] == board[3] == marker) or
            (board[7] == board[5] == board[3] == marker) or
            (board[9] == board[5] == board[1] == marker) or
            (board[7] == board[4] == board[1] == marker) or
            (board[8] == board[5] == board[2] == marker) or
            (board[9] == board[6] == board[3] == marker))


def draw_check(board):
    for i in xrange(1, 10):
        if space_check(board, i):
            return False
    return True


def replay():
    return raw_input("Do you want to play another game? ").lower().startswith('y')


def main():
    print 'Welcome to Tic Tac Toe!'
    while True:
        theBoard = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print '%s goes first!' % turn

        game_on = True

        while game_on:
            if turn == 'Player 1':
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print "Congratulations! Player 1 wins!"
                    game_on = False
                else:
                    if draw_check(theBoard):
                        display_board(theBoard)
                        print "The game is a draw!"
                        break
                    else:
                        turn = 'Player 2'
            else:
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print "Congratulations! Player 2 wins!"
                    game_on = False
                else:
                    if draw_check(theBoard):
                        display_board(theBoard)
                        print "The game is a draw!"
                        break
                    else:
                        turn = 'Player 1'

        if not replay():
            break


if __name__ == '__main__':
    main()
