from modules.Player.HumanPlayer import HumanPlayer
from modules.Game import Game
import pickle
import os


file_name = os.getenv('BOT_FILE') or 'trained_bot.pkl'
with open(file_name, 'rb') as f:
    print('load bot file from', file_name)
    bot1 = pickle.load(f)

bot1.is_explore = False
human_player = HumanPlayer(board_size=3, )
choice = input('play? (Y/N): ')
is_human_player1 = True
bot1.is_thinking_out_loud = True
while choice.upper() == 'Y':
    if is_human_player1:
        game = Game(3, human_player, 'O', bot1, 'X')
    else:
        game = Game(3, bot1, 'O', human_player, 'X')
    game.loop(show_step=True)
    is_human_player1 = not is_human_player1
    choice = input('play? (Y/N): ')
