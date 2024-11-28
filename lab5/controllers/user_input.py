class UserInput:
    """
    Клас, що обробляє ввід користувача для управління кубом.

    Атрибути:
    cube (object): Об'єкт куба, з яким виконуються операції.
    colors (dict): Словник, що містить доступні кольори для куба.
    """

    def __init__(self, cube):
        """
        Ініціалізація класу з переданим кубом.

        Параметри:
        cube (object): Об'єкт куба, з яким будуть виконуватись операції.
        """
        self.cube = cube
        self.colors = {
            "1": "Red", "2": "Green", "3": "Blue", "4": "Yellow", "5": "Cyan", 
            "6": "Magenta", "7": "White", "8": "Black", "9": "Gray", "10": "Orange"
        }

    def get_next_action(self):
        """
        Запитує користувача, яку дію він хоче виконати далі.

        Повертає:
        str: Вибір користувача для подальшої дії (повертає номер вибору).
        """
        try:
            print("\nЩо ви хочете зробити далі?\n1 - Обертання\n2 - Зміна кольору\n3 - Масштабування\n4 - Зберегти в файл\n5 - Вихід")
            choice = input("Ваш вибір: ")
            return choice
        except Exception as e:
            print(f"Помилка при отриманні вводу для дії: {e}")
            return None

    def get_rotation_input(self):
        """
        Запитує користувача кути обертання куба по осях X та Y.

        Параметри:
        - Встановлюються кути обертання для осей X та Y.
        """
        try:
            angle_x = float(input("Введіть кут обертання по осі X (між -360 і 360): "))
            angle_y = float(input("Введіть кут обертання по осі Y (між -360 і 360): "))
            self.cube.set_rotation(angle_x, angle_y)
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть числові значення.")
        except Exception as e:
            print(f"Помилка при введенні даних для обертання: {e}")

    def get_scale_input(self):
        """
        Запитує користувача коефіцієнт масштабування для куба.

        Параметри:
        - Встановлюється коефіцієнт масштабування (межі: від 1 до 100).
        """
        try:
            scale = float(input("Введіть коефіцієнт масштабування (між 1 і 100): "))
            if scale > 0:
                self.cube.set_scale(scale)
            else:
                print("Коефіцієнт масштабування повинен бути більшим за 0.")
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть числові значення.")
        except Exception as e:
            print(f"Помилка при введенні даних для масштабування: {e}")

    def get_initial_size(self):
        """
        Запитує користувача початкові розміри куба по осях X, Y, Z.

        Повертає:
        tuple: Кортеж з трьох чисел (розміри по осях X, Y, Z), обмежений значеннями від 1 до 13.
        """
        try:
            size_x = float(input("Введіть розмір куба по осі X (між 1 і 13): "))
            size_y = float(input("Введіть розмір куба по осі Y (між 1 і 13): "))
            size_z = float(input("Введіть розмір куба по осі Z (між 1 і 13): "))
            # Обмеження розміру між 1 і 13
            size_x = max(1, min(13, size_x))
            size_y = max(1, min(13, size_y))
            size_z = max(1, min(13, size_z))
            return size_x, size_y, size_z
        except ValueError:
            print("Невірний ввід. Використано розмір 10x10x10 за замовчуванням.")
            return 10, 10, 10
        except Exception as e:
            print(f"Помилка при отриманні початкового розміру: {e}")
            return 10, 10, 10

    def change_color(self):
        """
        Запитує користувача вибір кольору для куба та змінює його.

        Параметри:
        - Користувач вибирає колір куба з доступного списку.
        """
        try:
            print("Доступні кольори: ")
            for key, color in self.colors.items():
                print(f"{key}: {color}")

            choice = input("Виберіть колір, ввівши номер: ")
            if choice in self.colors:
                self.cube.color = self.colors[choice]
                print(f"Колір змінено на {self.colors[choice]}")
            else:
                print("Невірний вибір. Колір залишився за замовчуванням.")
        except Exception as e:
            print(f"Помилка при зміні кольору: {e}")
