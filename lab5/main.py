"""
Основна програма для рендерингу 3D куба та взаємодії з користувачем через командний інтерфейс.

Програма дозволяє користувачу виконувати операції над кубом, такі як обертання, зміна кольору, масштабування та збереження куба в ASCII-форматі в файл.

Імпортуються модулі:
- `Cube`: для створення та маніпуляцій з кубом.
- `Renderer`: для проектування та рендерингу куба.
- `UserInput`: для отримання введення від користувача.
- `os`: для очищення консолі.
- `time`: для затримки між кадрами.

Основні етапи роботи:
1. Ініціалізація куба з початковими розмірами.
2. Використання рендерера для відображення куба.
3. Взаємодія з користувачем для виконання операцій.
4. Оновлення зображення куба після кожної дії користувача.
5. Можливість зберегти куб у файл або завершити програму.

Функція:
- `main()`: основна функція, яка керує всім процесом: отримує введення користувача, керує обертанням куба, його кольором, масштабом та збереженням файлу.
"""
import os
import time
from models.cube import Cube
from render.renderer import Renderer
from controllers.user_input import UserInput

def main():
    user_input = UserInput(None)
    
    # Отримання початкових розмірів куба
    size_x, size_y, size_z = user_input.get_initial_size()
    cube = Cube(size_x, size_y, size_z)
    user_input.cube = cube  # Прив'язуємо куб до вводу користувача
    
    renderer = Renderer(resolution=40, foco=40, y_distorter=1.1, left_right=1.5, up_down=0.5)

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            rotated_cube = cube.rotate()
            projection = renderer.project(rotated_cube)
            lines = renderer.get_lines(projection)
            rendered_ascii = renderer.render(projection, lines, cube.color)
            time.sleep(0.5)
            action = user_input.get_next_action()

            if action == "1":
                user_input.get_rotation_input()
            elif action == "2":
                user_input.change_color()
            elif action == "3":
                user_input.get_scale_input()
            elif action == "4":
                filename = input("Enter filename to save the cube: ")
                cube.save_to_file(filename, rendered_ascii)
            elif action == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")
    except KeyboardInterrupt:
        print("Program interrupted.")

if __name__ == "__main__":
    main()
