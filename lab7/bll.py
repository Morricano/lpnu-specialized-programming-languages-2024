"""
Модуль бізнес-логіки, який взаємодіє з даними через репозиторій і забезпечує отримання даних через Unit of Work.

Клас:
- `Repository`: клас репозиторія, який відповідає за отримання даних через API.
- `UnitOfWork`: клас для роботи з одиничною транзакцією, який надає методи для отримання всіх необхідних даних.

Клас `Repository`:
- Відповідає за взаємодію з API для отримання користувачів та постів.
- Методи:
  - `get_users(self)`: отримує список користувачів через API.
  - `get_posts(self)`: отримує список постів через API.

Клас `UnitOfWork`:
- Відповідає за об'єднання операцій і забезпечує доступ до даних за допомогою репозиторія.
- Методи:
  - `get_all_data(self)`: отримує всі необхідні дані (користувачів і пости) через репозиторій та об'єднує їх у словник.
"""

from dal import APIClient

class Repository:
    """
    Клас репозиторія для отримання даних через API.
    """
    def __init__(self, api_client):
        """
        Ініціалізація репозиторія з переданим клієнтом API.

        :param api_client: екземпляр APIClient для взаємодії з API.
        """
        self.api_client = api_client

    def get_users(self):
        """
        Отримує список користувачів через API.

        :return: Список користувачів.
        """
        return self.api_client.fetch_data("users")

    def get_posts(self):
        """
        Отримує список постів через API.

        :return: Список постів.
        """
        return self.api_client.fetch_data("posts")


class UnitOfWork:
    """
    Клас для об'єднання операцій, що забезпечує доступ до даних через репозиторій.
    """
    def __init__(self, repository):
        """
        Ініціалізація одиничної транзакції з переданим репозиторієм.

        :param repository: екземпляр Repository для отримання даних.
        """
        self.repository = repository

    def get_all_data(self):
        """
        Отримує всі необхідні дані (користувачів і пости) через репозиторій.

        :return: Словник з даними користувачів та постів.
        """
        users = self.repository.get_users()
        posts = self.repository.get_posts()
        return {"users": users, "posts": posts}
