class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author
        
    def __str__(self):
        return f'{self._name}, {self._author}'
    
    def __repr__(self):
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
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError('Значение pages для PaperBook должно быть типа int')
        self.pages = pages

    def __repr__(self):
        return f"{self._name}, {self._author}, {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError('Значение duration для AudioBook должно быть типа float')
        self.duration = duration

    def __repr__(self):
        return f'{self._name}, {self._author}, {self.duration}'


