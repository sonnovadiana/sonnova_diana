import doctest


class Hostess:
    def __init__(self, name: str) -> None:
        """
        Создание и подготовка объекта "Хостес"

        :param name: Имя клиента

        Примеры:
        >>> hostess = Hostess('Bob') # Инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должен быть типа str")
        self.name = name
    def greetings(self) -> str:
        """
        Функция добавляет к тексту привествия имя клиента

        :return: Привествие с именем клиента

        Примеры:
        >>> hostess = Hostess('Bob')
        >>> hostess.greetings()
        """
        ...
    def table(self, booking: str) -> str:
        """
        Функция принимает решение в зависимости от переменной booking ("пригласить", "предложить", "переспросить")

        :param booking: принимает ответ "да", заказывал столик, "нет" не заказывал
        :return: Текст, в зависимости от ответа

        Примеры:
        >>> hostess = Hostess('Bob')
        >>> hostess.table('да')
        """
        if booking.lower() == 'да':
            return f"{self.name}, позвольте вас пригласить к столику"
        elif booking.lower() == 'нет':
            return f'{self.name}, Какой столик пожелаете?'
        else:
            return f'Извините, {self.name}, не раслышала, да или нет?'
        ...

class Cube:
    side: int
    def volume(self, side: int) -> int:
        """
        Функция расчитывает объем куба

        :param side: Сторона ребра куба
        :return: Объем куба #Для расчета объема куба, сторона(side) возводится в третью степень (side**3)

        Примеры:
        >>> cube = Cube()
        >>> cube.volume(5)
        125
        """
        if not isinstance(side, int):
            raise ValueError('Ребро куба должен быть типом int')
        ...
    def area(self, side: int) -> int:
        """
        Функция расчитывает площадь куба

        #Чтобы расчитать площадь куба, необходи сначало расчитать площадь одной стороны
        #Для этого одну сторону нужно возвести в квадрат (side**2)
        #После расчитанную площадь необходимо умножить на 6 (area_side*6)

        :param side: Сторона ребра куба
        :return: площадь куба

        Примеры:
        >>> cube = Cube()
        >>> cube.volume(12)
        864
        """
        if not isinstance(side, int):
            raise ValueError('Ребро куба должен быть типом int')
        ...

class Prediction:
    question: str
    def prediction(self, question: str) -> str:
        """
        Функция отвечает на заданный вопрос

        :param question: Вопрос
        :return: Текст 'да' или 'нет'

        Примеры:
        >>> prediction = Prediction()
        >>> prediction.prediction('Сегодня будет хороший день?')
        да
        """
        if not isinstance(question, str):
            raise TypeError("Вопрос должен быть типом str")
        bl = self.random_number()
        if bl == 1:
            return 'да'
        else:
            return 'нет'
        ...
    def random_number(self) -> int:
        """
        Функция возращает случайное число

        :return: Число 1 или 0

        Примеры:
        >>> prediction = Prediction()
        >>> prediction.random_number()
        1
        """
        ...
    def random_question(self) -> str:
        """
        Функция возращает случайно выбрнный вопрос

        #Внутри функции хранится n-ое кол-во вопросов
        #Случайным образом выбирается один вопрос и возращается

        :return: Вопрос

        Примеры:
        >>> prediction = Prediction()
        >>> prediction.random_question()
        Какой твой любимый цвет?
        """
        ...

if __name__ == "__main__":
    doctest.testfile()

