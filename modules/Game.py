from .Board import Board
from pprint import pprint


class Game:
    def __init__(
            self,
            board_size,
            player1,
            player1_symbol,
            player2,
            player2_symbol,
    ):
        self.board_size = board_size
        self.board = Board(board_size)
        self.player1 = player1
        self.player1.assign_symbol(player1_symbol)
        self.player2 = player2
        self.player2.assign_symbol(player2_symbol)
        self.winner = None
        self.is_player1_turn = True
        self.history = []

    def play(self):
        if self.is_player1_turn:
            next_state = self.player1.play(self.board)
        else:
            next_state = self.player2.play(self.board)
        self.history.append((self.board.current_board, next_state, self.is_player1_turn))
        self.board.set_board(next_state)
        self.is_player1_turn = not self.is_player1_turn

    def print_history(self):
        print('--Game Replay--')
        print('player_1', self.player1.symbol)
        print('player_2', self.player2.symbol)
        tmp_board = Board(self.board_size)
        for index, value in enumerate(self.history):
            current_state, next_state, is_player1 = value
            print('step: ', index + 1)
            if is_player1 and self.board.get_hash(current_state, self.player1.symbol) in self.player1.policy.table:
                pprint(self.player1.policy.table[self.board.get_hash(current_state, self.player1.symbol)])
            tmp_board.set_board(next_state)
            print(tmp_board)
        print('finish')

    def loop(self, show_step=False, show_final=False, show_history=False):
        is_finish = False
        while not is_finish:
            self.play()
            if show_step:
                print(self.board)
            winner = self.board.check_winner()
            if winner is not None:
                is_finish = True
                self.winner = winner
                if show_step:
                    if self.winner != '-':
                        print(f"{self.winner} win")
                    else:
                        print('draw')
        if self.winner == self.player2.symbol and show_history:
            self.print_history()
            input('press any key')
        if show_final:
            print(self.board)
