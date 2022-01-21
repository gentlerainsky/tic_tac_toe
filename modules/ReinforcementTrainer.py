from .Game import Game
import random


class ReinforcementTrainer:
    def __init__(
            self,
            board_size,
            learner,
            opponent,
            benchmark_player
    ):
        self.board_size = board_size
        self.learner = learner
        self.learner_symbol = 'X'
        self.opponent = opponent
        self.opponent_symbol = 'O'
        self.benchmark_player = benchmark_player
        self.game = None
        self.benchmark_score = []
        self.train_score = []

    def train(self):
        if random.random() < 0.5:
            player1 = self.learner
            player1_symbol = self.learner_symbol
            player2 = self.opponent
            player2_symbol = self.opponent_symbol
        else:
            player1 = self.opponent
            player1_symbol = self.opponent_symbol
            player2 = self.learner
            player2_symbol = self.learner_symbol
        self.game = Game(
            self.board_size,
            player1,
            player1_symbol,
            player2,
            player2_symbol
        )
        self.game.loop()
        if self.game.winner == self.learner_symbol:
            self.learner.win()
            self.opponent.lose()
        elif self.game.winner == self.opponent_symbol:
            self.learner.lose()
            self.opponent.win()
        else:
            self.learner.draw()
            self.opponent.draw()
        self.learner.reset_epoch()
        self.opponent.reset_epoch()

    def loop(self, step):
        percent_10 = max(int(step * 0.1), 100)
        for i in range(step):
            if (i % percent_10) == 0:
                print(i, 'steps trained')
                self.benchmark(100)
                self.self_play_benchmark(1000)
            self.train()


    def self_play_benchmark(self, step):
        win_count = 0
        lose_count = 0
        draw_count = 0
        self.learner.is_explore = False
        self.opponent.is_explore = False
        for i in range(step):
            if random.random() < 0.5:
                player1 = self.learner
                player1_symbol = self.learner_symbol
                player2 = self.opponent
                player2_symbol = self.opponent_symbol
            else:
                player1 = self.opponent
                player1_symbol = self.opponent_symbol
                player2 = self.learner
                player2_symbol = self.learner_symbol

            self.game = Game(
                self.board_size,
                player1,
                player1_symbol,
                player2,
                player2_symbol
            )
            self.game.loop()
            if self.game.winner == self.learner_symbol:
                win_count += 1
            elif self.game.winner == self.opponent_symbol:
                lose_count += 1
            else:
                draw_count += 1
        self.learner.is_explore = True
        self.opponent.is_explore = True
        self.train_score.append((win_count, draw_count, lose_count))

    def benchmark(self, step):
        win_count = 0
        lose_count = 0
        draw_count = 0
        self.learner.is_explore = False
        for i in range(step):
            if random.random() < 0.5:
                player1 = self.learner
                player1_symbol = self.learner_symbol
                player2 = self.benchmark_player
                player2_symbol = self.opponent_symbol
            else:
                player1 = self.benchmark_player
                player1_symbol = self.opponent_symbol
                player2 = self.learner
                player2_symbol = self.learner_symbol

            self.game = Game(
                self.board_size,
                player1,
                player1_symbol,
                player2,
                player2_symbol
            )
            self.game.loop()
            if self.game.winner == self.learner_symbol:
                win_count += 1
            elif self.game.winner == self.opponent_symbol:
                lose_count += 1
            else:
                draw_count += 1
        self.learner.is_explore = True
        self.benchmark_score.append((win_count, draw_count, lose_count))
