# class MinimaxPlayer:
#     def __init__(self, board_size):
#         self.board_size = board_size
#         self.symbol = None
#
#     def assign_symbol(self, symbol):
#         self.symbol = symbol
#
#     def play(self, board):
#         next_possible_states = board.get_possible_states(self.symbol)
#         return board.unhash(random.choice(next_possible_states), self.symbol)
