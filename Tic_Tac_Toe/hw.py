from random import choice


class TicTacGame:
    PLAYER_1: str = 'X'
    PLAYER_2: str = 'O'
    BOARD: dict = {'7': ' ', '8': ' ', '9': ' ',
                   '4': ' ', '5': ' ', '6': ' ',
                   '1': ' ', '2': ' ', '3': ' '}

    def show_board(self):
        print(self.BOARD['7'] + '|' + self.BOARD['8'] + '|' + self.BOARD['9'])
        print('-+-+-')
        print(self.BOARD['4'] + '|' + self.BOARD['5'] + '|' + self.BOARD['6'])
        print('-+-+-')
        print(self.BOARD['1'] + '|' + self.BOARD['2'] + '|' + self.BOARD['3'])

    def validate_input(self):
        while True:
            try:
                val = input()
                if int(val) not in range(1, 10):
                    print('Номер поля должен быть цифрой от 1 до 9')
                elif self.BOARD[val] != ' ':
                    print('Поле уже занято!')
                else:
                    return val
            except ValueError:
                print('Номер поля должен быть цифрой от 1 до 9: ')

    def start_game(self):
        first_player = choice([self.PLAYER_1, self.PLAYER_2])
        second_player = (self.PLAYER_2 if first_player == self.PLAYER_1 else
                         self.PLAYER_1)
        for i in range(9):
            if i % 2 == 0 or i == 0:
                current_player = first_player
            else:
                current_player = second_player
            print(f'Сейчас ход игрока {current_player}')
            self.show_board()
            print('Введите номер поля (от 1 до 9) для хода: ')
            input_value = self.validate_input()
            self.BOARD[input_value] = current_player
            if self.check_winner(current_player):
                print(f'Победил игрок {current_player}')
                self.show_board()
                break
            elif i == 8:
                print('Draw')
                self.show_board()

    def check_winner(self, player):
        if self.BOARD['1'] == self.BOARD['2'] == self.BOARD['3'] == player:
            return True
        elif self.BOARD['4'] == self.BOARD['5'] == self.BOARD['6'] == player:
            return True
        elif self.BOARD['7'] == self.BOARD['8'] == self.BOARD['9'] == player:
            return True
        elif self.BOARD['1'] == self.BOARD['4'] == self.BOARD['7'] == player:
            return True
        elif self.BOARD['2'] == self.BOARD['5'] == self.BOARD['8'] == player:
            return True
        elif self.BOARD['3'] == self.BOARD['6'] == self.BOARD['9'] == player:
            return True
        elif self.BOARD['1'] == self.BOARD['5'] == self.BOARD['9'] == player:
            return True
        elif self.BOARD['3'] == self.BOARD['5'] == self.BOARD['7'] == player:
            return True
        else:
            return False


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
