from math import cos, sin, radians
from numpy import dot
import re
import os

class Cube:
    """
    Клас для моделювання куба, який може обертатись, масштабуватись та зберігатися у файл.

    Атрибути:
    corners (list): Список з восьми вершин куба.
    angle_x (float): Кут обертання куба навколо осі X.
    angle_y (float): Кут обертання куба навколо осі Y.
    scale (float): Масштаб куба.
    color (str): Колір куба.
    """

    def __init__(self, size_x=10, size_y=10, size_z=10, angle_x=0, angle_y=0, scale=1, color="White"):
        """
        Ініціалізація куба з початковими параметрами.

        Параметри:
        size_x (float): Розмір куба по осі X (за замовчуванням 10).
        size_y (float): Розмір куба по осі Y (за замовчуванням 10).
        size_z (float): Розмір куба по осі Z (за замовчуванням 10).
        angle_x (float): Кут обертання по осі X (за замовчуванням 0).
        angle_y (float): Кут обертання по осі Y (за замовчуванням 0).
        scale (float): Масштаб куба (за замовчуванням 1).
        color (str): Колір куба (за замовчуванням "White").
        """
        self.corners = [[-size_x, -size_y, -size_z], [size_x, -size_y, -size_z],
                        [-size_x, -size_y, size_z], [-size_x, size_y, -size_z],
                        [size_x, -size_y, size_z], [size_x, size_y, -size_z],
                        [-size_x, size_y, size_z], [size_x, size_y, size_z]]
        self.angle_x = angle_x
        self.angle_y = angle_y
        self.scale = scale
        self.color = color

    def rotate(self):
        """
        Обертає куб на основі заданих кутів обертання по осях X та Y.

        Повертає:
        list: Список нових координат вершин куба після обертання та масштабування.
        """
        x_rotator = [[1, 0, 0],
                     [0, cos(radians(self.angle_x)), sin(radians(self.angle_x))],
                     [0, -sin(radians(self.angle_x)), cos(radians(self.angle_x))]]
        y_rotator = [[cos(radians(self.angle_y)), 0, -sin(radians(self.angle_y))],
                     [0, 1, 0],
                     [sin(radians(self.angle_y)), 0, cos(radians(self.angle_y))]]
        rotated_cube = [dot(dot(point, x_rotator), y_rotator) for point in self.corners]
        return self.scale_cube(rotated_cube)

    def scale_cube(self, cube):
        """
        Масштабує координати куба.

        Параметри:
        cube (list): Список координат куба для масштабування.

        Повертає:
        list: Масштабовані координати куба.
        """
        return [[point[0] * self.scale, point[1] * self.scale, point[2] * self.scale] for point in cube]

    def set_rotation(self, angle_x, angle_y):
        """
        Встановлює кути обертання для куба.

        Параметри:
        angle_x (float): Кут обертання по осі X.
        angle_y (float): Кут обертання по осі Y.
        """
        self.angle_x = max(-360, min(360, angle_x))
        self.angle_y = max(-360, min(360, angle_y))

    def set_scale(self, scale):
        """
        Встановлює масштаб для куба.

        Параметри:
        scale (float): Масштаб куба, має бути між 1 та 5.
        """
        if 1 <= scale <= 5:
            self.scale = scale
        else:
            print("Невірний масштаб. Він має бути між 1 і 5.")

    def save_to_file(self, filename, rendered_ascii):
        """
        Зберігає ASCII-подання куба у файл у директорії ../../results/lab5.

        Параметри:
        filename (str): Ім'я файлу для збереження.
        rendered_ascii (str): ASCII-подання куба у вигляді рядка.

        Викидає:
        Exception: У разі виникнення помилки при збереженні в файл.
        """
        try:
            # Визначаємо шлях до директорії
            directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "lab5", "results")
            
            # Якщо директорія не існує, створюємо її
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            # Видалення всіх ANSI-кодів (форматування, кольори, стилі)
            clean_ascii = re.sub(r'\033\[\d+;?\d*;?\d*m', '', rendered_ascii)
            
            # Повний шлях до файлу
            file_path = os.path.join(directory, f"{filename}.txt")
            
            # Записуємо ASCII-арт у файл
            with open(file_path, 'w') as file:
                file.write(clean_ascii)  # Запис ASCII у файл
            
            print(f"Куб збережено у файл: {file_path}")
        except Exception as e:
            print(f"Помилка під час збереження у файл: {e}")
