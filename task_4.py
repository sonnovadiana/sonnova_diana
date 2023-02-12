import random
from tqdm import tqdm
import time


class Game:
    def __init__(self, player):
        """
        Инициализация объекта Game
        :param player: Имя игрока
        """
        self.player = player

    def loading(self, loading_time) -> None:
        """
        Реализуется полоска загрузки игры
        :param loading_time: Время загрузки игры. У каждой игры своя скорость загрузки
        :return: None
        """

        for i in tqdm(range(loading_time)):
            time.sleep(0.5)

    def description(self) -> str:
        return 'Программа создана чтобы расслабиться после тяжелого дня и поиграть всем известные нам игры.\n' \
               'Хорошего время провождения'

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, name):
        if not isinstance(name, str):
            raise TypeError('Введи имя игрока')
        self._player = name

    def __str__(self):
        return f"Имя игрока: {self.player}. Доступные игры: 'Угадай слово', 'Орел или решка"


class RandomWords(Game):
    def __init__(self, player: str) -> None:
        """
        Инициализация игры 'Угадай слово'
        Атрибут __loading_time закрытый, так как время загрузки игры у каждого разное
        :param player: Имя игрока
        """

        super().__init__(player)
        self.player = player
        self.__loading_time = 10
        self.words = ['вагон', 'яблоко', "собака", "душа"]

    def list_words(self, word: str) -> None:
        """
        Метод добавляет новое слово в список
        :param word: Слово
        :return:
        """
        if isinstance(word, str):
            self.words.append(word)
        else:
            raise TypeError('Нужно написать слово')

    def random_word(self) -> tuple:
        """
        :return: Возращает случайное слово и в случайном порядке буквы этого слова из списка
        """
        word = random.choice(self.words)
        return ''.join(random.sample(word, len(word))), word

    def play(self) -> None:
        """
        Реализация игры "Угадай слово"
        Из метода random_word получаем слово
        В цикле принимаем слово, если не верно счетчик увеличивается
        Если слово угадано, подравляем с победой
        :return: None
        """
        print("Загрузка игры")
        self.loading(self.__loading_time)

        victory = False
        score = 0

        random_letter_word, random_word = self.random_word()

        print('"Угадай слово"')
        print(f"Привествую {self.player}\nВ слове случайным образом перетасованы все буквы")
        print("Тебе предстоит угадай что это за слово, но не забывай что у тебя 5 попыток!\n")
        print(f'Слово которое тебе нужно угадать: {random_letter_word}')

        while victory != True and score < 5:
            player_input = input('Введи слово: ')

            if player_input.lower() == random_word:
                victory = True
                print(f'Да!Ты угадал. Это действительно слово {random_word}')
            else:
                score += 1
                print(f"Неверное слово, попробуй еще раз\n Попыток:{score}")

        print('Спасибо за игру')

    def description(self) -> str:
        return 'Игра под названием "Угадай слово"\n' \
               'Суть игры в том, что случайным образом выбирается слово и в этом слове рандомно перетасованы буквы.\n' \
               'Ваша задача угадать слово, но не забывайте что у вас 5 попыток'

    def __str__(self):
        return f'Имя игрока: {self.player}. Время загрузки игры: {self.__loading_time}. Доступные слова: {self.words}'

    def __repr__(self):
        return 'RandomWords(player={!r})'.format(self.player)

class Coin(Game):
    def __init__(self, player):
        """
        Класс игры "Орел или решка"
        Атрибут __loading_time закрытый, так как время загрузки игры у каждого разное
        :param player: Имя игрока
        """
        super().__init__(player)
        self.player = player
        self.__loading_time = 5

    def play(self) -> None:
        """
        Реализация игры "Орел или решка"
        Случайным образом выбирается 0-решка, 1-орел
        Введется счет угаданных и неудачных попыток
        :return: None
        """
        print("Загрузка игры")
        self.loading(self.__loading_time)

        print('"Орел или решка"')
        print(f"Приветсвую {self.player}")
        print('Подбрасывается монетка, твоя задача угадать выпал орел или решка')
        print('Чтобы выйти из игры напиши "stop"')

        # Счет игрока
        score = 0
        # Неудачные попытки
        unsuccessful_attempts = 0
        play = True
        while play:
            coin = self.random_coin()

            print('Орел или решка?')
            answer_player = input('Твой ответ: ')

            if answer_player.lower() == 'stop':
                play = False

            if answer_player.lower() == coin:
                print(f'\nТы угадал!, это действительно {coin}')
                score += 1
            else:
                print(f'\nНе угадал, удача обязательно будет на твоей стороне\nЭто был {coin}')
                unsuccessful_attempts += 1
            print(f'Счет: {score}\nНеудачные попытки: {unsuccessful_attempts}')

    def random_coin(self) -> str:
        """
        Случайным образом выбирается 0-решка, 1-орел
        :return: орел или решка
        """
        coin = random.randint(0, 1)
        if coin == 0:
            return 'решка'
        else:
            return 'орел'

    def description(self) -> str:
        return 'Игры под названием "Орел или решка"\n' \
               'Компьютер "подбрасывает монетку" и ваша задача угадать что выпадет.\n' \
               'В игре ведется счет удачных и неудачных попыток'

    def __str__(self):
        return f'Имя игрока: {self.player}. Время загрузки игры: {self.__loading_time}.'

    def __repr__(self):
        return 'Coin(player={!r})'.format(self.player)

if __name__ == '__main__':
    game = Game('Player')
    print(game.description())
    print(game)
    print()

    game_words = RandomWords('Player2')
    print(game_words.description())
    print(game_words)
    print(repr(game_words))
    print()

    game_coin = Coin('Player3')
    print(game_coin.description())
    print(game_coin)
    print(repr(game_coin))
    print()

    game_words.play()

