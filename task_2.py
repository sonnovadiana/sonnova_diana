class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        return 'Книга {}'.format(self.name)

    def __repr__(self):
        return "Book(id = {}, name = '{}', pages = {})".format(self.id, self.name, self.pages)

test = Book(id = 1, name = 'Ницше', pages = 400)
print(test)
print(repr(test))