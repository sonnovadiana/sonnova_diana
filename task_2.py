class Book:

    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        return 'Книга {}'.format(self.name)

    def __repr__(self):
        return "Book(id = {}, name = '{}', pages = {})".format(self.id, self.name, self.pages)


book = Book(12, 'Мураками', 280)
print(book)
print(repr(book))


class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        self.books = books

    def get_next_book_id(self):
        if self.books is None:
            return 1
        return id(self.books[::-1][0])+1

    def get_index_by_book_id(self, id_book: int):
        for book in self.books:
            if id_book == id(book):
                return self.books.index(book)
        else:
            raise ValueError('Книги с запрашиваемым id не существует')


library = Library(['Ксенофан', 'Фалес', 'Демокрит', 'Парменид'])
print(library.get_next_book_id())
print(library.get_index_by_book_id(1720169286097))


