class Book:
    def __init__(self, name: str, author: str):
        """
        Создание и подгатовка абстракного класса Book

        :param name: Название книги
        :param author: Автор книги
        """
        self._name = name
        self._author = author

    def __str__(self):
        return f'{self._name}, {self._author}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, data):
        raise AttributeError('Изменять атрибут name запрещено')

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, data):
        raise AttributeError('Изменять атрибут author запрещено')


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """
        Класс PaperBook используется для создания объекта бумажной книги

        :param name:Название книги
        :param author:Автор книги
        :param pages: Количество страниц
        """
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError('Значение pages для PaperBook должно быть типа int')
        elif pages <= 0:
            raise ValueError('Значение pages не может быть отрицательным или равно нулю')
        else:
            self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, data):
        if not isinstance(data, int):
            raise TypeError('Значение pages для PaperBook должно быть типа int')
        elif data <= 0:
            raise ValueError('Значение pages не может быть отрицательным или равно нулю')
        else:
            self._pages = data

    def __str__(self):
        return f'Название книги: {self.name}. Автор книги: {self.author}. Количество страниц: {self.pages}'

    def __repr__(self):
        return 'PaperBook(name={!r}, author={!r}, pages={})'.format(self._name, self._author, self.pages)


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
        Класс AudioBook испальзуется для создания объекта аудиокниги
        :param name: Название книги
        :param author: Автор книги
        :param duration: Продолжительность книги
        """
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError('Значение duration для AudioBook должно быть типа float')
        elif duration <= 0:
            raise ValueError('Значение duration не может быть отрицательным или равно нулю')
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, data):
        if not isinstance(data, float):
            raise TypeError('Значение duration для AudioBook должно быть типа float')
        elif data <= 0:
            raise ValueError('Значение duration не может быть отрицательным или равно нулю')
        else:
            self._duration = data

    def __str__(self):
        return f'Название книги: {self.name}. Автор книги: {self.author}. Продолжительность записи: {self.duration}'

    def __repr__(self):
        return 'AudioBook(name={!r}, author={!r}, duration={})'.format(self._name, self._author, self.duration)

if __name__ == '__main__':
    book1 = PaperBook('Ночь в Лиссабоне', 'Эрих Мария Ремарк', 258)
    print(book1)
    print(repr(book1))
    print()

    book2 = AudioBook('Трудно быть богом', 'Братья Стругацкие', 356.1)
    print(book2)
    print(repr(book2))

