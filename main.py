from modules.ReinforcementTrainer import ReinforcementTrainer
from modules.Player.ReinforcementLearningPlayer import ReinforcementLearningPlayer, Policy
from modules.Player.HumanPlayer import HumanPlayer
from modules.Player.RandomPlayer import RandomPlayer
from modules.Game import Game
from pprint import pprint

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

benchmark_player = RandomPlayer(3)
for i in range(10):
    bot1.train_on_lose = False
    print('round', i)
    trainer1 = ReinforcementTrainer(3, bot1, bot2, benchmark_player)
    trainer1.loop(3000)
    print('== self-train score ==')
    pprint(trainer1.train_score)
    print('== benchmark score ==')
    pprint(trainer1.benchmark_score)
    bot2.policy.table = bot1.policy.table.copy()
    bot1.exploration_rate = bot1.exploration_rate * 0.9
    bot2.exploration_rate = bot2.exploration_rate * 0.9
    bot1.train_on_lose = True
    trainer2 = ReinforcementTrainer(3, bot1, benchmark_player, benchmark_player)
    trainer2.loop(1500)
    print('== random-train score ==')
    pprint(trainer2.train_score)
    print('== benchmark score ==')
    pprint(trainer2.benchmark_score)

# bot1.exploration_rate = 0.2
# for i in range(5):
#     bot1.train_on_lose = True
#     trainer2 = ReinforcementTrainer(3, bot1, benchmark_player, benchmark_player)
#     trainer2.loop(1500)
#     print('== random-train score ==')
#     pprint(trainer2.train_score)
#     print('== benchmark score ==')
#     pprint(trainer2.benchmark_score)
#     bot1.exploration_rate = bot1.exploration_rate * 0.9

# pprint(player2.policy.table)

# bot1.train_on_lose = True
# trainer2 = ReinforcementTrainer(3, bot1, benchmark_player, benchmark_player)
bot1.is_explore = False
for i in range(5):
    trainer2 = ReinforcementTrainer(3, bot1, benchmark_player, benchmark_player)
    trainer2.loop(1000)
    print('== random-train score ==')
    pprint(trainer2.train_score)
    print('== benchmark score ==')
    pprint(trainer2.benchmark_score)

game1 = Game(3, bot1, 'O', benchmark_player, 'X')
is_player1_turn = True
game1.is_player1_turn = is_player1_turn
bot1.is_explore = False
for i in range(100000):
    game1.loop(show_history=True)
    game1 = Game(3, bot1, 'O', benchmark_player, 'X')
    game1.is_player1_turn = not is_player1_turn

# bot1.is_explore = False
# human_player = HumanPlayer(board_size=3, )
#
# choice = input('play?')
# is_human_player1 = True
# bot1.is_thinking_out_loud = True
# while choice.upper() == 'Y':
#     if is_human_player1:
#         game = Game(3, human_player, 'O', bot1, 'X')
#     else:
#         game = Game(3, bot1, 'O', human_player, 'X')
#     game.loop(show_step=True)
#     is_human_player1 = not is_human_player1
#     choice = input('play?')
