# Tic-Tac-Toe with Reinforcement Learning

## Installation

Use either Pipenv or pip to install the dependency. There are not many dependency for this project as it is meant to be
coded from scratch. Only `numpy` and `pandas` are used to help with some training statistics computation.

```bash
pipenv install
```
or
```bash
pip -r requirements.txt
```

## Run

### Training
To train a reinforcement learning bot. 
```bash
python train.py
```

### Test
```bash
python test_bot.py
```
or run the following file to play with the bot.
```bash
python test_play.py
```

**Note:** You can specify an environment variable `BOT_FILE` to set the input/output reinforcement learning state in
each script. For example, `BOT_FILE=tmp.pkl python train.py` and then `BOT_FILE=tmp.pkl python test_play.py`.

## Structure
- `/modules/Game.py` - Manage a game by give turn to each player.
- `/modules/Board.py` - Store game state, and a function to check if a game has ended.
- `/modules/ReinforcementTrainer.py` - Manage the learning process of reinforcement learning bot.
- `/modules/Player/`
  - `/modules/Player/ReinforcementLearningPlayer.py` - A bot that implement the reinforcement learning algorithm.
  - `/modules/Player/RandomPlayer.py` - A bot that play a random move.
  - `/modules/Player/MinimaxPlayer.py` - A bot that implement a minimax searching algorithm.
  - `/modules/Player/HumanPlayer.py` - Use this player, so it will ask for an input from terminal before play.
