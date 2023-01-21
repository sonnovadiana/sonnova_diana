class Book:
    def __init__(self, id: int, name: str, pages: int):
        """
        Создание и подготовка объекта Book

        :param id:int
             Уникальный номер книги
        :param name:str
             Имя писателя
        :param pages:int
             Кол-во страниц
        """
        if not isinstance(id, int):
            raise ValueError('id должен быть типа int')
        self.id = id

        if not isinstance(name, str):
            raise ValueError('name должен быть типа str')
        self.name = name

        if not isinstance(pages, int):
            raise ValueError('pages должен быть типа int')
        self.pages = pages

    def __str__(self):
        return 'Книга {}'.format(self.name)

    def __repr__(self):
        return "Book(id={}, name='{}', pages ={})".format(self.id, self.name, self.pages)


class Library:
    def __init__(self, books=None):
        """
        Класс Library используется для получение индефикатора и индекса книги в списке

        :param books:list
            Список книг
        """

        if books is None:
            self.books = []
        self.books = books

    def get_next_book_id(self):
        """
        Возращает индефикатор для добавления новой книги
        Если список пуст, возражает 1

        :return:int
        """

        if len(self.books) == 0:
            return 1
        return id(self.books[-1]) + 1

    def get_index_by_book_id(self, id_book: int):
        """
        Возращает индекс книги соответсвующему индефикатору
        Если нету книги с данным индефикатором вызывается исключение

        :param id_book:int
            Уникальный индефикатор

        :return:int
            Индекс
        """
        for index, book in enumerate(self.books):
            if id_book == id(book):
                return self.books.index(index)
        else:
            raise ValueError('Книги с запрашиваемым id не существует')


if __name__ == '__main__':
    my_book = Book(12, 'Мураками', 280)
    print(my_book)
    print(repr(my_book))

    library = Library(['Ксенофан', 'Фалес', 'Демокрит', 'Парменид'])
    print(library.get_next_book_id())
    print(library.get_index_by_book_id(1720169286097))
