from rgbprint import gradient_print, Color
import os

class Messages:
    def __init__(self):
        self.commands_list = [
            {"title": "Открыть книги", "function": self.list_book},
            {"title": "Создать книгу", "function": self.create_book},
            {"title": "Удалить книгу", "function": self.del_book},
            {"title": "Найти книгу", "function": self.find_book},
            {"title": "Найти книгу по жанру", "function": self.find_book_genre},
            {"title": "Выйти", "function": exit},
        ]


    def open_menu(self) -> None:
        """
        Opens the menu (The data is taken from the variable self.commands_list)
        """

        # Output all functions
        for count, value in enumerate(self.commands_list, 1):
            print(f"[{Color.red}{count}{Color.reset}] {value['title']}")

        user_resp = input("> ")

        if not user_resp.isnumeric():
            self.print_error("Вы ввели не число!")
        else:
            user_resp = int(user_resp)
            if user_resp > len(self.commands_list) or user_resp <= 0:
                self.print_error("Этот параметр не подходит!")

        # Execute the function
        self.clear_console()
        self.commands_list[user_resp - 1]['function']()

    def print_error(self, text: str, exit_: bool = True) -> None:
        """
        Displays the error on the screen

        :param text: Text message
        :param exit_: Go to the menu?
        """
        
        print(f"\n[{Color.red}ОШИБКА{Color.reset}] {text}")

        if exit_:
            input(f"\n{Color.orange}Нажмите пробел что-бы вернуться в меню{Color.reset}")
            self.start()

    def print_success(self, text: str) -> None:
        """
        Display a successful message

        :param text: Text message
        """

        print(f"\n[{Color.green}УСПЕХ{Color.reset}] {text}")

    def print_books(self, books: list) -> None:
        """
        Display all books on the screen

        :param books: books from the database
        """

        for book in books:
            print(f"""{Color.gold}#{book[0]}
{Color.aqua}Заголовок: {Color.reset}{book[1]}
{Color.aqua}Автор: {Color.reset}{book[2]}
{Color.aqua}Жанр: {Color.reset}{book[3]}
{Color.aqua}Описание: {Color.reset}{book[4]}\n\n""")

    def clear_console(self) -> None:
        """
        Clears the screen
        """

        os.system("cls")
