import doctest


class Hostess:
    name: str

    def __init__(self, name: str, table: int) -> None:
        """
        Создание и подготовка объекта "Хостес"

        :param name: Имя клиента
        :param table: Номер стола

        Примеры:
        >>> hostess = Hostess('Bob', 13) # Инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Имя должен быть типа str")
        self.name = name

        if not isinstance(table, int):
            raise TypeError("Стол должен быть типа int")
        self.table = table

    def greetings(self) -> str:
        """
        Функция добавляет к тексту привествия имя клиента

        :return: Привествие с именем клиента

        Примеры:
        >>> hostess = Hostess('Bob', 7)
        >>> hostess.greetings()
        Рады вас видеть, Bob
        """

    def table_order(self, booking: str) -> str:
        """
        Функция принимает решение в зависимости от переменной booking ("пригласить",
                                                                       "предложить", "переспросить")

        :param booking: принимает ответ, True, False
        :return: Возращает заранее готовый текст с именем клиента, в зависимости от ответа

        Примеры:
        >>> hostess = Hostess('Bob', 32)
        >>> hostess.table_order('да')
        Bob, , позвольте вас пригласить к столику 32
        >>> hostess.table_order('нет')
        Bob, Какой столик пожелаете?
        >>>hostess.table_order('Может быть')
        Извините, Bob, не раслышала, да или нет?
        >>> hostess = Hostess('Bob', 'Сорок два')
        Traceback (most recent call last):
        ...
        TypeError: Стол должен быть типа int
        """

        if booking:
            return f"{self.name}, позвольте вас пригласить к столику {self.table}"
        elif not booking:
            return f'{self.name}, Какой столик пожелаете?'
        else:
            return f'Извините, {self.name}, не раслышала, да или нет?'


class IntegerSideCube:
    side: int
    cube_quantity: int

    def __init__(self, side: int, cube_quantity: int):
        """
        Создание и подготовка объекта "Куб"

        :param side: Сторона ребра куба
        :param cube_quantity: Количество кубов

        Примеры:
        >>> cube = IntegerSideCube(12, 1) # Инициализация экземпляра класса
        """

        if isinstance(side, int):
            raise ValueError("Сторона должна быть типа int")
        self.side = side

        if isinstance(side, int):
            raise ValueError("Количество кубов должен быть типа int")

        if cube_quantity == 0:
            raise ValueError("Количество кубов не может ровняться 0")
        self.cube_quantity = cube_quantity

    def volume(self) -> int:
        """
        Функция расчитывает объем куба

        Для расчета объема куба, сторона(side) возводится в третью степень (side**3)

        :return: Объем куба

        Примеры:
        >>> cube = IntegerSideCube(5, 1)
        >>> cube.volume()
        125
        >>> cube = IntegerSideCube(8, 3)
        >>> cube.volume()
        1536
        >>> cube = IntegerSideCube(10, 0)
        >>> cube.volume()
        Traceback (most recent call last):
        ...
        ValueError: Количество кубов не может ровняться 0
        >>> cube = IntegerSideCube(17.5, 0)
        Traceback (most recent call last):
        ...
        ValueError: Сторона должна быть типа int
        """

    def area(self) -> int:
        """
        Функция расчитывает площадь куба или нескольких

        Чтобы расчитать площадь куба, необходи сначало расчитать площадь одной стороны
        Для этого одну сторону нужно возвести в квадрат (side**2)
        После расчитанную площадь необходимо умножить на 6 (area_side*6)

        if self.cube_quantity > 1:
             : return Возращается площадь умноженная на cube_quantity

        :return: площадь куба

        Примеры:
        >>> cube = IntegerSideCube(12, 1)
        >>> cube.area()
        1728
        """


class Prediction:
    question: str
    number_questions: int

    def __init__(self, question: str, number_questions: int):
        """
        Создание и подготовка объекта "Предсказание"

        :param question: Вопрос
        :param number_questions: Количество вопросов

        Примеры:
        >>> predict = Prediction('Сегодня будет хороший день?', 1) # Инициализация экземпляра класса
        """
        if not isinstance(question, str):
            raise TypeError("Вопрос должен быть типом str")
        self.question = question

        if not isinstance(number_questions, int):
            raise TypeError("Вопрос должен быть типом int")
        self.number_questions = number_questions

    def prediction(self) -> str:
        """
        Функция отвечает на заданный вопрос
        Если вопросов несколько, возращает несколько ответов

        if self.umber_questions > 1:
             : return n-е количество ответов

        :return: Текст 'да' или 'нет' или несколько ответов

        Примеры:
        >>> prediction = Prediction('Сегодня будет хороший день? Будет сегодня дождь?', 2)
        >>> prediction.prediction()
        да, нет
        >>> prediction = Prediction('Мне купить эту книгу?', 1)
        >>> prediction.prediction()
        да
        >>> prediction = Prediction(['У меня тяжелые противники?, Я смогу победить?'], 2)
        Traceback (most recent call last):
        ...
        TypeError("Вопрос должен быть типом str")
        """

        if not isinstance(self.question, str):
            raise TypeError("Вопрос должен быть типом str")
        bl = self.random_number()
        if bl == 1:
            return 'да'
        else:
            return 'нет'

    def random_number(self) -> int:
        """
        Функция возращает случайное число

        :return: Число 1 или 0

        Примеры:
        >>> prediction = Prediction()
        >>> prediction.random_number()
        1
        """

    def random_question(self) -> str:
        """
        Функция возращает случайно выбранный вопрос

        Внутри функции хранится n-ое кол-во вопросов
        Случайным образом выбирается один вопрос и возращается

        :return: Вопрос

        Примеры:
        >>> prediction = Prediction()
        >>> prediction.random_question()
        Какой твой любимый цвет?
        """


if __name__ == "__main__":
    doctest.testfile(__name__)
