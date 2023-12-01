import sqlite3


class DataBase:
    def __init__(self):
        self._con = sqlite3.connect("db.db")
        self._cur = self._con.cursor()

        self._create_table()

    def _create_table(self) -> None:
        """
        Creating default tables in the database
        """

        self._cur.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, "
                          "author TEXT, genre TEXT, content TEXT)")

    def add_book_db(self, title: str, author: str, genre: str, content: str) -> None:
        """
        Adding a book to the database

        :param title: Title book
        :param content: Content book
        """

        self._cur.execute("INSERT INTO books (title, author, genre, content) VALUES (?, ?, ?, ?)", (title, author, genre, content))
        self._con.commit()

    def get_books_db(self) -> list:
        """
        Get all books from the database
        """

        self._cur.execute("SELECT * from books")
        return self._cur.fetchall()

    def get_book_db(self, id_: int) -> list:
        """
        Get book by ID from the database

        :param id_: ID book
        """

        self._cur.execute("SELECT * FROM books WHERE id = ?", (id_, ))
        return self._cur.fetchone()

    def del_book_db(self, id_: int) -> None:
        """
        Delete a book by ID from the database

        :param id_: ID book
        """

        self._cur.execute("DELETE FROM books WHERE id = ?", (id_, ))
        self._con.commit()

    def find_book_db(self, word: str) -> list:
        """
        Search for a book by keyword from the database

        :param word: keyword
        """

        args = (f'%{word.lower()}%', f'%{word.lower()}%',)
        self._cur.execute("SELECT * FROM books WHERE LOWER(title) LIKE ? OR LOWER(content) LIKE ?", args)
        return self._cur.fetchall()
    def find_book_db_genre(self, word: str) -> list:
        """
        Search for a book by genre from the database

        :param word: keyword
        """

        args = (f'%{word.lower()}%',)
        self._cur.execute("SELECT * FROM books WHERE LOWER(genre) LIKE ?", args)
        return self._cur.fetchall()