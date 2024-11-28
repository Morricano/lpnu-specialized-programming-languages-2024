"""
Основний модуль програми, який керує взаємодією з користувачем, отримує дані через API,
відображає їх та надає можливість збереження у файли.

Функція:
- `main()`: основна функція програми для керування процесом отримання, відображення даних та їх збереження.
"""

from dal import APIClient, DataSaver
from bll import Repository, UnitOfWork
from ui import UserInterface

def main():
    """
    Основна функція програми. Запускає цикл взаємодії з користувачем, отримує дані через API,
    відображає їх у таблиці та надає можливість збереження даних у форматах JSON, CSV, або TXT.
    
    Програма працює в нескінченному циклі, поки користувач не вибере 'quit'.
    Користувач може вибирати між переглядом даних користувачів або постів.
    Після перегляду даних, користувач може зберегти їх у вибраному форматі.
    """
    api_url = "https://jsonplaceholder.typicode.com"
    api_client = APIClient(api_url)
    repository = Repository(api_client)
    uow = UnitOfWork(repository)
    
    while True:
        # Запитуємо користувача про ввід.
        user_input = UserInterface.prompt_user_input()
        
        # Перевіряємо правильність введеного значення.
        if not UserInterface.validate_input(user_input):
            continue
        
        # Вихід з програми, якщо введено 'quit'.
        if user_input == 'quit':
            break
        
        # Отримуємо дані через UnitOfWork.
        data = uow.get_all_data()
        
        # Відображаємо дані залежно від вибору користувача.
        if user_input == 'users':
            UserInterface.display_data(data['users'], format_type='table', color=True)
        elif user_input == 'posts':
            UserInterface.display_data(data['posts'], format_type='table', color=True)
        
        # Запитуємо користувача, чи хоче він зберегти дані.
        save_option = input("Do you want to save the data? (y/n): ").strip().lower()
        
        # Якщо користувач хоче зберегти, запитуємо формат.
        if save_option == 'y':
            file_format = input("Choose file format (json/csv/txt): ").strip().lower()
            
            # Зберігаємо у вибраному форматі.
            if file_format == 'json':
                DataSaver.save_to_json(data[user_input], f"{user_input}.json")
            elif file_format == 'csv':
                DataSaver.save_to_csv(data[user_input], f"{user_input}.csv")
            elif file_format == 'txt':
                DataSaver.save_to_txt(data[user_input], f"{user_input}.txt")
            else:
                print("Invalid format.")

# Перевірка, чи є цей файл основним для виконання.
if __name__ == "__main__":
    main()
