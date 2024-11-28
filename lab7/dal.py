"""
Модуль для взаємодії з API та збереження даних у різних форматах (JSON, CSV, TXT).

Класи:
- `APIClient`: клас для отримання даних з API.
- `DataSaver`: клас для збереження даних у файли (JSON, CSV, TXT).

Клас `APIClient`:
- Відповідає за отримання даних з API.
- Методи:
  - `fetch_data(self, endpoint)`: здійснює запит до API на зазначений endpoint і повертає отримані дані у вигляді JSON. У разі помилки виводить повідомлення про помилку.

Клас `DataSaver`:
- Відповідає за збереження даних у різних форматах (JSON, CSV, TXT).
- Методи:
  - `save_to_json(data, filename)`: зберігає дані у форматі JSON.
  - `save_to_csv(data, filename)`: зберігає дані у форматі CSV.
  - `save_to_txt(data, filename)`: зберігає дані у текстовому форматі TXT.
"""

import requests
import json
import csv
from colorama import Fore

class APIClient:
    """
    Клас для отримання даних з API.
    """
    def __init__(self, base_url):
        """
        Ініціалізація клієнта API з базовим URL.

        :param base_url: базова URL-адреса для API.
        """
        self.base_url = base_url

    def fetch_data(self, endpoint):
        """
        Отримує дані з API для зазначеного endpoint.

        :param endpoint: кінцевий шлях для запиту (наприклад, "users", "posts").
        :return: Дані у форматі JSON або None у разі помилки.
        """
        try:
            response = requests.get(f"{self.base_url}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Error fetching data: {e}")
            return None


class DataSaver:
    """
    Клас для збереження даних у різних форматах (JSON, CSV, TXT).
    """
    @staticmethod
    def save_to_json(data, filename):
        """
        Зберігає дані у форматі JSON у файл.

        :param data: Дані, які потрібно зберегти.
        :param filename: Назва файлу для збереження.
        """
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(Fore.GREEN + f"Data saved to {filename}")

    @staticmethod
    def save_to_csv(data, filename):
        """
        Зберігає дані у форматі CSV у файл.

        :param data: Список словників, які потрібно зберегти.
        :param filename: Назва файлу для збереження.
        """
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(Fore.GREEN + f"Data saved to {filename}")

    @staticmethod
    def save_to_txt(data, filename):
        """
        Зберігає дані у текстовому форматі TXT у файл.

        :param data: Список елементів, які потрібно зберегти.
        :param filename: Назва файлу для збереження.
        """
        with open(filename, 'w') as f:
            for item in data:
                f.write(f"{item}\n")
        print(Fore.GREEN + f"Data saved to {filename}")
