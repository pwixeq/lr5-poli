class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __str__(self):
        status = 'Взята' if self.is_borrowed else 'Доступна'
        return f'{self.title} - {self.author} {self.year} [{status}]'

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'is_borrowed': self.is_borrowed,
        }
    @classmethod
    def from_dict(cls, d):
        book = cls(d['title'], d['author'], d['year'], d['is_borrowed'])
        book.is_borrowed = d['is_borrowed']
        return book


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Книга {book.title} добавлена в библиотеку')

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == book.title.lower():
                self.books.remove(book)
                print(f'Книга {title} удалена из библиотеки')
                return True
        print(f'Книга {title} не найдена в библиотеке')
        return False

    def find_by_year(self, year):
        result = [book for book in self.books if book.year == year]
        return result

    def find_by_author(self, author):
        res = [book for book in self.books if book.author == author]
        return res

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    print(f'Книга {title} уже взята')
                    return False
                else:
                    book.is_borrowed = True
                    print(f'Книга {title} не найдена')
                    return False
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f'Книга {title} была возвращена')
                    return True
                else:
                    print(f'Книга {title} в библиотеке')
                    return False
            else:
                print(f'Книга {title} не найдена')
                return False

    def get_available_books(self):
        return [book for book in self.books if not book.is_borrowed]

if __name__ == '__main__':
    lib = Library('kkgkg')
    book1 = Book('хуй', 'пенис', 1999)
    book2 = Book('пизда', 'вульва', 1998)
    lib.add_book(book1)
    lib.add_book(book2)
    lib.borrow_book('1998')
    print('пенис')
    for book in lib.find_by_author('пенис'):
        print(f' - {book}')
