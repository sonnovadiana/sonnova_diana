class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        return 'Книга {}'.format(self.name)

    def __repr__(self):
        return "Book(id = {}, name = '{}', pages = {})".format(self.id, self.name, self.pages)

library = [Book(id = 12, name = 'Ницше', pages = 400),
             Book(id = 63, name = 'Мураками', pages = 365),
             Book(id = 97, name = 'Бродский', pages = 560),
             Book(id = 34, name = 'Пелевин', pages = 400)]

for book in library:
    print(f'{book}\n'
          f'{repr(book)}\n\n'
          f'//////////////////\n')
