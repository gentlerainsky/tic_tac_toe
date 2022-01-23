import math
from ..Board import Board


class MinimaxPlayer:
    def __init__(self, board_size):
        self.board_size = board_size
        self.symbol = None
        self.cache = {}

    def assign_symbol(self, symbol):
        self.symbol = symbol

    def play(self, board):
        next_possible_states = board.get_possible_states(self.symbol)
        best_state = None
        best_value = -math.inf
        for state in next_possible_states:
            tmp_board = Board(board.size)
            tmp_board.set_board(Board.unhash(state, self.symbol))
            value = self.minimax(tmp_board, 0, False)
            if value > best_value:
                best_state = state
                best_value = value
        tmp_board = Board(board.size)
        tmp_board.set_board(Board.unhash(best_state, self.symbol))
        return board.unhash(best_state, self.symbol)

    def minimax(self, current_board, depth, is_max):
        if current_board.hash(self.symbol) in self.cache:
            if is_max and 'max' in self.cache[current_board.hash(self.symbol)]:
                return self.cache[current_board.hash(self.symbol)]['max']
            elif 'min' in self.cache[current_board.hash(self.symbol)]:
                return self.cache[current_board.hash(self.symbol)]['min']
        winner = current_board.check_winner()
        if winner is not None:
            if winner == self.symbol:
                return 1
            elif winner == '-':
                return 0
            else:
                return -1
        if is_max:
            next_player_symbol = self.symbol
        else:
            next_player_symbol = 'O' if self.symbol == 'X' else 'X'
        next_possible_states = current_board.get_possible_states(next_player_symbol, self.symbol)
        if is_max:
            tmp_value = -math.inf
            comp_func = max
        else:
            tmp_value = math.inf
            comp_func = min
        for state in next_possible_states:
            tmp_board = Board(self.board_size)
            tmp_board.set_board(Board.unhash(state, self.symbol))
            tmp_value = comp_func(tmp_value, self.minimax(tmp_board, depth + 1, not is_max))
        if is_max:
            if current_board.hash(self.symbol) not in self.cache:
                self.cache[current_board.hash(self.symbol)] = {}
            self.cache[current_board.hash(self.symbol)]['max'] = tmp_value
        else:
            if current_board.hash(self.symbol) not in self.cache:
                self.cache[current_board.hash(self.symbol)] = {}
            self.cache[current_board.hash(self.symbol)]['min'] = tmp_value
        return tmp_value

    def win(self):
        pass

    def lose(self):
        pass

    def draw(self):
        pass

    def reset_epoch(self):
        pass


if __name__ == '__main__':
    player = MinimaxPlayer(3)
    player.assign_symbol('X')
    board = Board(3)
    board.set_board([
        'O', 'O', ' ',
        'X', 'X', ' ',
        'O', ' ', ' '
    ])
    print(player.play(board))

    board = Board(3)
    board.set_board([
        'O', 'O', ' ',
        'X', ' ', ' ',
        'O', 'X', ' '
    ])
    print(player.play(board))
