'''
User Input Specifications
1) Enter number of rows: Atleast 4, must be divisible by 2, max is 16
2) Enter number of columns: Atleast 4, must divisible by 2, max is 16
3) First Player Move Color: B(Black) or W(White)
4) Color of top left piece in initial board setup: B(Black) or W(White)
5) Winning Condition: > (most points to win) or < (least points to win)

6) MOVE INPUT SPECIFICATION: row# SPACE column# (ex: 1 3)
'''

import gamelogic


def othello_game():
    '''Obtains user inputs for initializing the game and runs the game.'''
    rows = _get_row_input()
    columns = _get_columns_input()
    first_turn_color = _first_turn_color()
    top_left_piece = _top_left_piece()
    winning_condition = _how_to_win()
    
    othello = gamelogic.OthelloGameState(rows, columns, first_turn_color, top_left_piece)
    othello.piece_counter()
    othello.print_board()
    print("TURN: ",first_turn_color)

    while True:
        othello.return_opposite_player()
        if othello.possible_valid_moves() == []:
            othello.switch_turn()
            othello.return_opposite_player()
            if othello.possible_valid_moves() == []:
                othello.return_winner(winning_condition)
                break

        try: 
            row, col = _move_input()    
            flip_list = othello.flippable_piece_list(row, col)
            othello.flip_piece(row, col, flip_list)
            othello.piece_counter()
            othello.print_board()
            othello.switch_turn()
        except:
            pass
        else:
            if othello.check_for_full_board == 0:
                othello.return_winner(winning_condition)
            



def _get_row_input():
    '''Gets the number of rows from user input.'''
    while True:
        rows = int(input("Enter number of rows: "))
        if rows % 2 == 0 and rows >= 4 and rows <= 16:
            return int(rows)
            break
        else:
            print("Enter an even number ranging from 4 to 16, inclusive")




def _get_columns_input():
    '''Gets the number of columns from user input.'''
    while True:
        columns = int(input("Enter number of columns: "))
        if columns % 2 == 0 and columns >= 4 and columns <= 16:
            return int(columns)
            break
        else:
            print("Enter an even number ranging from 4 to 16, inclusive")




def _first_turn_color():
    '''Gets the piece color of the first player from user input.'''
    first_player = input("Enter first player: ")
    return first_player




def _top_left_piece():
    '''Gets the top left piece color input for initializing the game.'''
    top_left_piece_color = input("Enter color of the top left piece: ")
    return top_left_piece_color




def _how_to_win():
    '''Gets winning condition for Othello.'''
    winning_condition = input("Enter winning condition: ")
    return winning_condition




def _move_input():
    '''Obtains the user's move input and adjusts the value to be used as list indexes.'''
    move = input("Enter move: ")
    move_list = move.split()
    row = int(move_list[0]) - 1
    col = int(move_list[1]) - 1
    return row, col
        

if __name__ == '__main__':
    othello_game()


