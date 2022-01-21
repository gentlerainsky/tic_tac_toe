class Board:
    def __init__(self, size = 3):
        self.size = size
        self.current_board = [' ', ] * (size ** 2)

    def get_current_board(self):
        return self.current_board.copy()

    def set_board(self, board_setting):
        if type(board_setting) == tuple:
            self.current_board = list(board_setting)
        else:
            self.current_board = board_setting

    def get_free_positions(self):
        return [pos for pos in range(len(self.current_board)) if self.current_board[pos] == ' ']

    def get_possible_states(self, symbol):
        free_positions = self.get_free_positions()
        states = []
        for free_position in free_positions:
            tmp = self.current_board.copy()
            tmp[free_position] = symbol
            states.append(Board.get_hash(tmp, symbol))
        return states

    def check_winner(self):
        for symbol in ['O', 'X']:
        # check horizontal
            for i in range(self.size):
                has_winner = True
                for j in range(self.size):
                    if self.current_board[i * self.size + j] != symbol:
                        has_winner = False
                        continue
                if has_winner:
                    return symbol
        # check vertically
            for j in range(self.size):
                has_winner = True
                for i in range(self.size):
                    if self.current_board[i * self.size + j] != symbol:
                        has_winner = False
                        continue
                if has_winner:
                    return symbol
        # check '/' vertically
            has_winner = True
            for i in range(self.size):
                if self.current_board[i * self.size + (self.size - i - 1)] != symbol:
                    has_winner = False
                    continue
            if has_winner:
                return symbol
        # check '\' diagonally
            has_winner = True
            for i in range(self.size):
                if self.current_board[i * self.size + i] != symbol:
                    has_winner = False
                    continue
            if has_winner:
                return symbol
        if len(self.get_possible_states('-')) == 0:
            return '-'
        return None

    @staticmethod
    def get_hash(board, symbol_1):
        symbol_2 = 'X' if symbol_1 == 'O' else 'O'
        return tuple([1 if x == symbol_1 else -1 if x == symbol_2 else 0 for x in board])

    def hash(self, symbol_1):
        symbol_2 = 'X' if symbol_1 == 'O' else 'O'
        return tuple([1 if x == symbol_1 else -1 if x == symbol_2 else 0 for x in self.current_board])

    @staticmethod
    def unhash(hashed_state, symbol_1):
        symbol_2 = 'X' if symbol_1 == 'O' else 'O'
        return [symbol_1 if x == 1 else symbol_2 if x == -1 else ' ' for x in hashed_state]

    def __repr__(self):
        text = ('-' * (2 * self.size + 1)) + '\n'
        for i in range(self.size):
            tmp = []
            for j in range(self.size):
                tmp.append(str(self.current_board[i * self.size + j]))
            text += f'|{"|".join(tmp)}|\n'
            text += ('-' * (2 * self.size + 1))
            text += '\n'
        return text


if __name__ == '__main__':
    board = Board(3)
    print(board)

    state = {}
    state[board.hash('X')] = 1
    print(state[board.hash('X')])

    board = Board(3)
    board.set_board([
        'O', 'O', ' ',
        'X', 'X', 'X',
        'O', ' ', ' '
    ])
    print('setup 1: ', 'X' == board.check_winner())
    print('setup 1 free pos: ', [2, 7, 8] == board.get_free_positions())

    board.set_board([
        'O', 'O', ' ',
        'X', 'O', 'X',
        'O', ' ', ' '
    ])
    print('setup 2: ', None == board.check_winner())

    board.set_board([
        'O', 'O', 'X',
        'X', 'X', 'O',
        'O', ' ', ' '
    ])
    print('setup 3: ', None == board.check_winner())

    board.set_board([
        'O', 'O', 'X',
        ' ', 'O', 'X',
        'X', 'O', ' '
    ])
    print('setup 4: ', 'O' == board.check_winner())

    board.set_board([
        'O', 'O', 'X',
        ' ', 'X', 'X',
        'X', 'O', ' '
    ])
    print('setup 5: ', 'X'== board.check_winner())
    print(board.get_possible_states('O'))
    board.set_board([
        'O', 'O', 'X',
        ' ', 'O', 'X',
        'X', 'O', 'O'
    ])
    print('setup 6: ', 'O' == board.check_winner())

    board.set_board([
        'O', 'O', 'X',
        ' ', 'X', 'X',
        ' ', 'O', 'O'
    ])
    print('setup 7: ', None == board.check_winner())

    board.set_board([
        'X', 'O', 'O',
        ' ', 'X', ' ',
        ' ', 'O', 'X'
    ])
    print('setup 8: ', 'X' == board.check_winner())
    print(board.get_possible_states('X'))
    board.set_board([
        'X', 'O', ' ',
        ' ', ' ', ' ',
        ' ', 'O', 'X'
    ])
    print('setup 9: ', None == board.check_winner())
    print('setup 9 free pos: ', [2, 3, 4, 5, 6] == board.get_free_positions())

    board.set_board([
        'X', 'O', 'O',
        ' ', ' ', ' ',
        'O', 'O', 'X'
    ])
    print('setup 9: ', None == board.check_winner())

    board.set_board([
        'O', 'O', 'O',
        ' ', ' ', ' ',
        'O', 'O', 'X'
    ])
    print('setup 9: ', 'O' == board.check_winner())

    board.set_board([
        'O', 'X', 'O',
        'X', 'X', 'O',
        'X', 'O', 'O'
    ])
    print('setup 10: ', 'O' == board.check_winner())

    board.set_board([
        'X', 'X', 'O',
        ' ', ' ', 'O',
        'X', 'O', 'O'
    ])
    print('setup 11: ', 'O' == board.check_winner())
