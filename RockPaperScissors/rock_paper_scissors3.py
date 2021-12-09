import random

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
OPTIONS = (ROCK, PAPER, SCISSORS)
EXIT = '!exit'

class RockPaperScissorsGame:
    def __init__(self):
        self.player_move = None
        self.computer_move = None
        self.game_mode = True

    def get_player_move(self):
        while True:
            choice = input('> ')
            if choice == EXIT:
                self.game_mode = False
                print('Bye!')
                break
            else:
                for option in OPTIONS:
                    if option.lower().startswith(choice.lower()):
                        return option
                print('Invalid input.')

    def is_player_win_or_draw(self, computer_move, player_move):
        idx_c = OPTIONS.index(computer_move)
        idx_p = OPTIONS.index(player_move)
        if (idx_p, idx_c) in [(1, 0), (2, 1), (0, 2)]:
            return True
        elif idx_c == idx_p:
            return None
        else:
            return False

    def get_computer_move(self, player_move):
        return random.choice(OPTIONS)

    def show_player_lose(self, computer_move):
        print(f'Sorry, but the computer chose {computer_move}')

    def show_player_win(self, computer_move):
        print(f'Well done. The computer chose {computer_move} and failed')

    def show_draw(self, computer_move):
        print(f'There is a draw ({computer_move})')

    def start(self):
        while True:
            pm = self.get_player_move()
            if not self.game_mode:
                break
            cm = self.get_computer_move(player_move=pm)
            is_player_win_or_draw = self.is_player_win_or_draw(computer_move=cm, player_move=pm)
            if is_player_win_or_draw is None:
                self.show_draw(computer_move=cm)
            elif is_player_win_or_draw:
                self.show_player_win(computer_move=cm)
            else:
                self.show_player_lose(computer_move=cm)

if __name__ == '__main__':
    game = RockPaperScissorsGame()
    game.start()
