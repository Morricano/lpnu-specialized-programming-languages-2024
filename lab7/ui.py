"""
Модуль для взаємодії з користувачем, відображення даних та збереження їх у файли.

Класи:
- `UserInterface`: клас для взаємодії з користувачем.
- Функція `main()`: основна функція для запуску програми.

Клас `UserInterface`:
- Відповідає за виведення даних, запит користувацького вводу та перевірку введених даних.
- Методи:
  - `display_data(data, format_type='list', color=False)`: відображає дані в різних форматах (список або таблиця) та підтримує кольорове оформлення.
  - `prompt_user_input()`: виводить запит на ввід користувача для вибору між 'users', 'posts' або 'quit'.
  - `validate_input(user_input)`: перевіряє, чи введений користувачем ввід є коректним ('users', 'posts', 'quit').

Функція `main()`:
- Запускає програму, здійснює взаємодію з API для отримання даних, відображає їх у потрібному форматі та надає можливість збереження даних у файли (JSON, CSV, TXT).
"""

import re
from colorama import Fore, Style
from tabulate import tabulate
from bll import UnitOfWork, Repository
from dal import APIClient, DataSaver

class UserInterface:
    """
    Клас для взаємодії з користувачем, відображення даних та отримання вводу.
    """
    @staticmethod
    def display_data(data, format_type='list', color=False):
        """
        Виводить дані у відповідному форматі (список або таблиця).

        :param data: Дані для відображення.
        :param format_type: Формат виведення ('list' або 'table'). За замовчуванням 'list'.
        :param color: Чи використовувати кольорове оформлення. За замовчуванням False.
        """
        if format_type == 'table':
            if color:
                print(Fore.CYAN + tabulate(data, headers="keys", tablefmt="pretty"))
            else:
                print(tabulate(data, headers="keys", tablefmt="pretty"))
        else:
            for item in data:
                if color:
                    print(Fore.GREEN + str(item))
                else:
                    print(item)

    @staticmethod
    def prompt_user_input():
        """
        Запитує користувача про введення вибору.

        :return: Вибір користувача ('users', 'posts', 'quit').
        """
        print(Fore.YELLOW + "Enter 'users' to view users, 'posts' to view posts, 'quit' to exit:")
        user_input = input("Your choice: ").strip().lower()
        return user_input

    @staticmethod
    def validate_input(user_input):
        """
        Перевіряє, чи є введене значення коректним.

        :param user_input: Введене користувачем значення.
        :return: True, якщо ввід правильний, інакше False.
        """
        if user_input not in ['users', 'posts', 'quit']:
            print(Fore.RED + "Invalid input. Please try again.")
            return False
        return True

def main():
    """
    Основна функція програми. Запускає взаємодію з користувачем, отримує дані з API, відображає їх та зберігає у файли.
    """
    api_url = "https://jsonplaceholder.typicode.com"
    api_client = APIClient(api_url)
    repository = Repository(api_client)
    uow = UnitOfWork(repository)
    
    while True:
        user_input = UserInterface.prompt_user_input()
        if not UserInterface.validate_input(user_input):
            continue
        
        if user_input == 'quit':
            break
        
        data = uow.get_all_data()
        if user_input == 'users':
            UserInterface.display_data(data['users'], format_type='table', color=True)
        elif user_input == 'posts':
            UserInterface.display_data(data['posts'], format_type='table', color=True)
        
        save_option = input(Fore.YELLOW + "Do you want to save the data? (y/n): ").strip().lower()
        if save_option == 'y':
            file_format = input("Choose file format (json/csv/txt): ").strip().lower()
            if file_format == 'json':
                DataSaver.save_to_json(data[user_input], f"{user_input}.json")
            elif file_format == 'csv':
                DataSaver.save_to_csv(data[user_input], f"{user_input}.csv")
            elif file_format == 'txt':
                DataSaver.save_to_txt(data[user_input], f"{user_input}.txt")
            else:
                print(Fore.RED + "Invalid format.")

if __name__ == "__main__":
    main()
