BLACK = "B"
WHITE = "W"
NONE = "."


DIRECTIONS_LIST = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]



class InvalidMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    pass



class OthelloGameState:
    def __init__(self, rows: int, cols: int, first_turn: str, left_piece: str):
        self.rows = rows
        self.columns = cols
        self.turn = first_turn
        self.top_left_piece_color = left_piece
        self.game_state = self._new_game()



    ########   INITIALIZING GAME STATE   ########



    def _new_game(self)-> [[int]]:
        '''Creates a new game with the board set up in a 2D list, with the 4
        centerpieces determined based on color that was input.'''
        new_game_state = []
        for row in range(self.rows):
            new_game_state.append([])
            for col in range(self.columns):
                new_game_state[row].append(NONE)

        if self.top_left_piece_color == "B":
            new_game_state[self.rows//2 - 1][self.columns//2 - 1] = BLACK
            new_game_state[self.rows//2][self.columns//2] = BLACK
            new_game_state[self.rows//2 - 1][self.columns//2] = WHITE
            new_game_state[self.rows//2][self.columns//2 - 1] = WHITE
        elif self.top_left_piece_color == "W":
            new_game_state[self.rows//2 - 1][self.columns//2 - 1] = WHITE
            new_game_state[self.rows//2][self.columns//2] = WHITE
            new_game_state[self.rows//2 - 1][self.columns//2] = BLACK
            new_game_state[self.rows//2][self.columns//2 - 1] = BLACK
        return new_game_state



    def print_board(self):
        '''Prints the state of the board.'''
        for row in self.game_state:
            for col in row:
                if col == NONE:
                    print(".", end = " ")
                elif col == BLACK:
                    print("B", end = " ")
                elif col == WHITE:
                    print("W", end = " ")
            print('\r')



    ########   VALID MOVE LOGIC   ########

            

    def is_on_board(self, row: int, col: int):
        '''Checks if row and column inputted by the user is valid.'''
        return row in range(self.rows) and col in range(self.columns)



    def switch_turn(self):
        '''Switches the turn of the player.'''
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK
        print("TURN: ", self.turn)
        return self.turn




    def return_opposite_player(self):
        '''Returns the opposite player to use in other methods.'''
        if self.turn == BLACK:
            self.opposite_player = WHITE
        else:
            self.opposite_player = BLACK
        return self.opposite_player




    def flippable_piece_list(self, row: int, col: int):
        '''Retrieves list of tiles to flip based on row and column inputted.'''
        actual_flip_list = []
        for sub_list in DIRECTIONS_LIST:
            temp_flip_list = []
            dir_y = sub_list[0] 
            dir_x = sub_list[1] 
            new_row = row
            new_col = col
            while True:
                new_row += dir_y
                new_col += dir_x
                if self.is_on_board(new_row, new_col) and self.game_state[new_row][new_col] == self.opposite_player:
                    temp_flip_list.append((new_row, new_col))
                elif self.is_on_board(new_row, new_col) and self.game_state[new_row][new_col] == self.turn:
                    actual_flip_list += temp_flip_list
                    break
                else:
                    break

        actual_flip_list = list(set(actual_flip_list))
        return (actual_flip_list)



    def flip_piece(self, row: int, col: int, actual_flip_list: list):
        '''Makes move and flips the pieces based on input and list retrieved from flippable list method.'''
        if actual_flip_list == []:
            print("INVALID")
            raise InvalidMoveError
        
        elif self.is_on_board(row, col) == True and self.game_state[row][col] == NONE:
            self.game_state[row][col] = self.turn
            print('VALID')
            for row_col_list in actual_flip_list:
                row = row_col_list[0]
                col = row_col_list[1]
                if self.turn == BLACK:
                    self.game_state[row][col] = BLACK
                elif self.turn == WHITE:
                    self.game_state[row][col] = WHITE
        return self.game_state




    def possible_valid_moves(self):
        '''Retrieves list of possible valid  moves that can be made.'''
        valid_moves = []
        for row in range(self.rows):
            for col in range(self.columns):
                if self.game_state[row][col] == NONE:
                    if self.flippable_piece_list(row, col) != []:
                        valid_moves.append((row, col))
        return valid_moves
        
                    

    ##########  WINNER FORMULATION/ PIECE COUNTER METHODS   ###########



    def piece_counter(self):
        '''Counts the number of each piece and updates the count for each turn.'''
        self.black_counter = 0
        self.white_counter = 0
        for sublist in self.game_state:
            for piece in sublist:
                if piece == BLACK:
                    self.black_counter += 1
                elif piece == WHITE:
                    self.white_counter += 1
        print("B:", str(self.black_counter), " W:",str(self.white_counter))
        
        


    def return_winner(self, winning_condition: str):
        '''Returns the winner of the game.'''
        if winning_condition == ">":
            if self.black_counter > self.white_counter:
                print("WINNER: BLACK")
            elif self.white_counter > self.black_counter:
                print("WINNER: WHITE")
            else:
                print("WINNER: NONE")
        elif winning_condition == "<":
            if self.black_counter < self.white_counter:
                print("WINNER: BLACK")
            elif self.white_counter < self.black_counter:
                print("WINNER: WHITE")
            else:
                print("WINNER: NONE")
        



    def check_for_full_board(self):
        '''Checks for full board, and returns winner.'''
        game_status = 0
        for sublist in self.game_state:
            for piece in sublist:
                if piece == NONE:
                    game_status += 1
        return game_status

               
