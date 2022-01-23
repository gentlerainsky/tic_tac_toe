from modules.Player.RandomPlayer import RandomPlayer
from modules.Player.MinimaxPlayer import MinimaxPlayer
from modules.Game import Game
import pickle
from pprint import pprint
import os


file_name = os.getenv('BOT_FILE') or 'trained_bot.pkl'
with open(file_name, 'rb') as f:
    print('load bot file from', file_name)
    bot1 = pickle.load(f)
bot1.is_explore = False

random_player = RandomPlayer(board_size=3, )
random_player_statistics = []
for i in range(10):
    win_count = 0
    lose_count = 0
    draw_count = 0

    for j in range(1000):
        game = Game(3, bot1, 'O', random_player, 'X')
        game.loop()
        if game.winner == 'O':
            win_count += 1
        elif game.winner == 'X':
            lose_count += 1
        else:
            draw_count += 1
    random_player_statistics.append((win_count, draw_count, lose_count))
print('random player statistics (win, draw, lose) for each testing session.')
pprint(random_player_statistics)

minimax_player = MinimaxPlayer(board_size=3, )
minimax_player_statistics = []
for i in range(10):
    win_count = 0
    lose_count = 0
    draw_count = 0

    for j in range(1000):
        game = Game(3, bot1, 'O', minimax_player, 'X')
        game.loop()
        if game.winner == 'O':
            win_count += 1
        elif game.winner == 'X':
            lose_count += 1
        else:
            draw_count += 1
    minimax_player_statistics.append((win_count, draw_count, lose_count))
print('minimax player statistics (win, draw, lose) for each testing session.')
pprint(minimax_player_statistics)
