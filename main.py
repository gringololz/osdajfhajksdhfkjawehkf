from modules import DataBase, Messages
from rgbprint import Color


class Book(DataBase, Messages):
    def __init__(self):
        super().__init__()
        Messages.__init__(self)

    def create_book(self) -> None:
        """
        Create a book
        """

        title = input("Введите заголовок книги: ")
        author = input('Введите автора книги: ')
        genre = input('Введите жанр книги: ')
        context = input("Введите описание книги: ")

        self.add_book_db(title, author, genre, context)
        self.print_success("Книга успешно создана!")

    def list_book(self) -> None:
        """
        Get a list of books
        """

        books = self.get_books_db()

        if len(books) == 0:
            self.print_error("У вас нет книг!")

        self.print_books(books)

    def del_book(self) -> None:
        """
        Delete the book
        """

        book_id = input("Введите ID книги которую хотите удалить: ")

        if not book_id.isnumeric():
            self.print_error("Вы ввели не число!")

        if self.get_book_db(int(book_id)):
            self.del_book_db(int(book_id))
            self.print_success("Книга успешно удалена!")
        else:
            self.print_error("Такой книги нет!")

    def find_book(self) -> None:
        """
        Find a book
        """

        word = input("Введите фразу или слово для поиска: ")

        books = self.find_book_db(word)

        if len(books) == 0:
            self.print_error("Книги не найдены!")

        self.print_books(books)

    def find_book_genre(self) -> None:
        """
        Find a book by genre
        """

        word = input("Введите жанр для поиска: ")

        books = self.find_book_db_genre(word)

        if len(books) == 0:
            self.print_error("Книги не найдены!")

        self.print_books(books)

    def start(self) -> None:
        """
        Start program
        """

        while True:
            self.clear_console()
            self.open_menu()
            input(f"\n{Color.orange}Нажмите пробел что-бы вернуться в меню{Color.reset}")


if __name__ == '__main__':
    book = Book()
    book.start()
