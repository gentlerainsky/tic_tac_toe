class HumanPlayer:
    def __init__(self, board_size):
        self.size = board_size
        self.symbol = None

    def assign_symbol(self, symbol):
        self.symbol = symbol

    def mark(self, board, symbol, position):
        if type(position) == tuple:
            row, col = position
        else:
            row = position // self.size
            col = position - self.size * (position // self.size)
        if board[row * self.size + col] == ' ':
            board[row * self.size + col] = symbol
            return True
        else:
            return False

    def play(self, board):
        print('human player', self.symbol, 'turn')
        print(board)
        is_move_made = False
        current_board = None
        while not is_move_made:
            next_position = input('Input a position row,col: ')
            row, col = next_position.split(',')
            row = int(row.strip()) - 1
            col = int(col.strip()) - 1
            current_board = board.get_current_board()
            is_move_made = self.mark(current_board, self.symbol, (row, col))
            if not is_move_made:
                print('illegal move')
        return current_board
