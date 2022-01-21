import random
import math
from pprint import pprint


class Policy:
    def __init__(self, board_size, default_value, learning_rate, decay_rate):
        self.board_size = board_size
        self.default_value = default_value
        self.decay_rate = decay_rate
        self.learning_rate = learning_rate
        self.table = {}

    def init_state(self, current_state, next_states):
        if current_state not in self.table:
            self.table[current_state] = {}
        for state in next_states:
            if state not in self.table[current_state]:
                self.table[current_state][state] = self.default_value

    def update(self, state_history, score):
        reversed_history = list(reversed(state_history))
        current_score = score
        state, next_state = reversed_history[0]
        self.table[state][next_state] = score
        for state, next_state in reversed_history[1:]:
            # value = self.table[state][next_state] + self.learning_rate * (self.decay_rate * current_score - self.table[state][next_state])
            # self.table[state][next_state] = value
            self.table[state][next_state] = (1 - self.learning_rate) * self.table[state][next_state] + self.learning_rate * self.decay_rate * current_score
            current_max = -1
            for s in self.table[state].keys():
                if self.table[state][s] > current_max:
                    current_max = self.table[state][s]
            current_score = current_max

    def load(self):
        pass

    def save(self):
        pass

class ReinforcementLearningPlayer:
    def __init__(self, board_size, policy, exploration_rate, win_score=1, lose_score=0, draw_score=0.1):
        self.board_size = board_size
        self.policy = policy
        self.state_history = []
        self.exploration_rate = exploration_rate
        self.symbol = None
        self.win_score = win_score
        self.lose_score = lose_score
        self.draw_score = draw_score
        self.is_explore = True
        self.is_thinking_out_loud = False
        self.train_on_lose = False

    def reset_epoch(self):
        self.state_history = []

    def assign_symbol(self, symbol):
        self.symbol = symbol

    def play(self, board):
        current_state = board.hash(self.symbol)
        next_possible_states = board.get_possible_states(self.symbol)
        self.policy.init_state(current_state, next_possible_states)
        if self.is_explore and (random.random() < self.exploration_rate):
            next_state = random.choice(next_possible_states)
        else:
            max_value = -math.inf
            next_state = None
            if self.is_thinking_out_loud:
                pprint(self.policy.table[current_state])
            for state in next_possible_states:
                if self.policy.table[current_state][state] > max_value:
                    max_value = self.policy.table[current_state][state]
                    next_state = state
        self.state_history.append((current_state, next_state))
        next_state = board.unhash(next_state, self.symbol)
        return next_state

    def win(self):
        if not self.train_on_lose:
            self.policy.update(self.state_history, self.win_score)

    def draw(self):
        # if not self.train_on_lose:
        self.policy.update(self.state_history, self.draw_score)

    def lose(self):
        self.policy.update(self.state_history, self.lose_score)

