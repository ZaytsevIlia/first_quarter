import random


class LotoCard:
    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self._numbers = random.sample(range(1, self._MAX_NUMBER), self._MAX_NUMBER_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def check_num_in_card(self, barrel):
        for line in self._card:
            if barrel in line:
                return True
        return False

    def strikethrough(self, barrel):
        for line in self._card:
            for num in line:
                if barrel == num:
                    self._numbers_stroked += 1
                    self._card[self._card.index(line)][line.index(num)] = '-'


class LotoGame:
    def __init__(self, player_card, computer_card):
        self.player_card = player_card
        self.computer_card = computer_card
        self.pouch = list(num for num in range(1, 91))

    def start(self):
        random.shuffle(self.pouch)
        while True:
            print(self.player_card.player_type + '\n' + '-' * 25)
            for line in self.player_card._card:
                for num in line:
                    print(num, end=' ')
                print()
            print()
            print(self.computer_card.player_type + '\n' + '-' * 25)
            for line in self.computer_card._card:
                for num in line:
                    print(num, end=' ')
                print()
            barrel = self.pouch.pop()
            print()
            print(f'Новый бочонок {barrel}, осталось {len(self.pouch)}')
            answer = input('Хотите зачеркнуть? y/n: ')

            if self.player_card.check_num_in_card(barrel):
                if answer == 'y':
                    self.player_card.strikethrough(barrel)
                else:
                    print('Вы проиграли!')
                    break
            else:
                if answer == 'y':
                    print('Вы проиграли!')
                    break

            if self.computer_card.check_num_in_card(barrel):
                self.computer_card.strikethrough(barrel)

            if self.player_card._numbers_stroked == self.player_card._MAX_NUMBER_IN_CARD:
                print(f'{self.player_card.player_type} выиграл!')
                break

            if self.computer_card._numbers_stroked == self.computer_card._MAX_NUMBER_IN_CARD:
                print(f'{self.computer_card.player_type} выиграл!')
                break


human = LotoCard('Ivan')
computer = LotoCard('R2D2')

game = LotoGame(human, computer)
game.start()
