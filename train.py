from modules.ReinforcementTrainer import ReinforcementTrainer
from modules.Player.ReinforcementLearningPlayer import ReinforcementLearningPlayer, Policy
from modules.Player.RandomPlayer import RandomPlayer
import pickle
import numpy as np
import os


bot1 = ReinforcementLearningPlayer(
    board_size=3,
    policy=Policy(
        board_size=3,
        default_value=0.5,
        learning_rate=0.1,
        decay_rate=1
    ),
    exploration_rate=0.25,
    win_score=1,
    lose_score=0,
    draw_score=0.6
)

bot2 = ReinforcementLearningPlayer(
    board_size=3,
    policy=Policy(
        board_size=3,
        default_value=0.5,
        learning_rate=0.1,
        decay_rate=1
    ),
    exploration_rate=0.4,
    win_score=1,
    lose_score=0,
    draw_score=0.6
)
self_play_statistics = []
random_play_statistics = []
benchmark_player = RandomPlayer(3)
for i in range(30):
    bot1.train_on_lose = False
    print('round', i)
    trainer1 = ReinforcementTrainer(3, bot1, bot2, benchmark_player)
    trainer1.loop(3000)
    train_score = np.array(trainer1.train_score)
    self_play_statistics.append(np.mean(train_score, axis=0).tolist())
    print('self-play score', np.mean(train_score, axis=0).tolist())
    benchmark_score = np.array(trainer1.benchmark_score)
    random_play_statistics.append(np.mean(benchmark_score, axis=0).tolist())
    print('benchmark score -> ', np.mean(benchmark_score, axis=0).tolist())

print('self_play_statistics')
print(self_play_statistics)
print('random_play_statistics')
print(random_play_statistics)
file_name = os.getenv('BOT_FILE') or 'trained_bot.pkl'
with open(file_name, 'wb') as f:
    print('save bot file at', file_name)
    pickle.dump(bot1, f)
