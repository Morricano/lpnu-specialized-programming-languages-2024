"""
Функція для відображення огляду даних.

Використовує метод `get_column_extremes` класу `DataHandler` для отримання мінімальних та максимальних значень для кожного стовпця і виводить цей огляд на екран.

Параметри:
- `data_handler`: Об'єкт класу `DataHandler`, що містить дані, які потрібно оглянути.

Повертає:
- Нічого не повертає. Функція лише виводить інформацію на екран.
"""
def display_data_overview(data_handler):
    """Відображає огляд даних."""
    print("Огляд даних:\n", data_handler.get_column_extremes())
