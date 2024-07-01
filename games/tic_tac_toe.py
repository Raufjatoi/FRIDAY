# games/tic_tac_toe.py

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_winner = None  # Keep track of winner!

    def print_board(self):
        # This is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # If valid move, then make the move (assign square to letter)
        # Then return true. If invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Winner if 3 in a row anywhere.. check all possibilities
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def play_tic_tac_toe():
    t = TicTacToe()
    letter = 'X'  # Starting letter
    while t.empty_squares():
        if letter == 'O':
            square = random.choice(t.available_moves())
            if t.make_move(square, letter):
                if t.current_winner:
                    return "O wins!"
                letter = 'X'
        else:
            square = random.choice(t.available_moves())
            if t.make_move(square, letter):
                if t.current_winner:
                    return "X wins!"
                letter = 'O'
    return "It's a tie!"
