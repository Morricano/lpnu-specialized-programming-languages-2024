import font
import sys
sys.path.append('D:/lpnu-specialized-programming-languages-2024/lab3/font')

def run_lab3():
    """
    Запускає лабораторну роботу 3, виводячи повідомлення та викликаючи основну логіку програми.

    Викликає:
        main(): Запускає основну логіку лабораторної роботи.
    """
    print("Це лабораторна робота 3")

    # Викликаємо main() для запуску основної логіки лабораторної роботи
    main()

# ANSI-коди для кольорів
COLOR_CODES = {
    'чорно-білий': '\033[97m',  # Білий
    'червоний': '\033[91m',
    'зелений': '\033[92m',
    'жовтий': '\033[93m',
    'синій': '\033[94m',
    'фіолетовий': '\033[95m',
    'бірюзовий': '\033[96m',
    'скинути': '\033[0m'  # Скидання кольору до стандартного
}

def generate_ascii_art(text, alignment="ліворуч", width=80, height=5, symbols=('@', '#', '*'), color='\033[97m'):
    """
    Генерує ASCII-арт на основі введеного тексту та заданих параметрів.

    Параметри:
        text (str): Текст, який потрібно перетворити на ASCII-арт.
        alignment (str): Вирівнювання тексту (ліворуч, по центру, праворуч). За замовчуванням "ліворуч".
        width (int): Ширина арт-об'єкта. За замовчуванням 80.
        height (int): Висота арт-об'єкта. За замовчуванням 5.
        symbols (tuple): Символи, які використовуються для створення арт-об'єкта. За замовчуванням ('@', '#', '*').
        color (str): ANSI-код для кольору тексту. За замовчуванням білий.

    Повертає:
        str: Генерований ASCII-арт у вигляді тексту з кольором та вирівнюванням.
    """
    FONT = font.get_font()
    lines = [""] * height  # Створюємо рядки для ASCII-арту

    # Додаємо символи для кожної літери в тексті
    for char in text.upper():
        if char in FONT:
            letter = FONT[char]
            for i in range(height):
                lines[i] += letter[i] + "  "  # Пробіл між літерами
        else:
            print(f"Немає шрифту для символу: {char}")
            return None

    # Вирівнюємо текст відповідно до обраного варіанту
    max_width = min(width, max(len(line) for line in lines))
    aligned_lines = []
    for line in lines:
        if alignment == "ліворуч":
            aligned_lines.append(line.ljust(max_width))
        elif alignment == "по центру":
            aligned_lines.append(line.center(max_width))
        elif alignment == "праворуч":
            aligned_lines.append(line.rjust(max_width))
        else:
            aligned_lines.append(line)

    # Додаємо колір до тексту
    return color + "\n".join(aligned_lines) + COLOR_CODES['скинути']

def preview_ascii_art(art):
    """
    Виводить попередній перегляд згенерованого ASCII-арту.

    Параметри:
        art (str): ASCII-арт, який потрібно відобразити.
    """
    print("\nПопередній перегляд:")
    print(art)

def save_ascii_art(art):
    """
    Зберігає згенерований ASCII-арт у файл.

    Параметри:
        art (str): ASCII-арт, який потрібно зберегти у файл.

    Викликає:
        input(): Запитує у користувача ім'я файлу для збереження.
    """
    filename = input("Введіть ім'я файлу для збереження: ").strip()
    with open(filename, 'w') as file:
        file.write(art)
    print(f"ASCII-арт збережено у файл '{filename}'.")

def choose_color_option():
    """
    Запитує у користувача вибір кольору для ASCII-арту.

    Повертає:
        str: ANSI-код кольору, обраного користувачем.
    """
    print("Доступні кольори:")
    for i, color in enumerate(COLOR_CODES.keys(), start=1):
        print(f"{i}. {color.capitalize()}")

    choice = input("Виберіть колір (1/2/3/...): ").strip()
    color_names = list(COLOR_CODES.keys())

    if choice.isdigit() and 1 <= int(choice) <= len(color_names):
        return COLOR_CODES[color_names[int(choice) - 1]]
    else:
        print("Невірний вибір, використовується чорно-білий режим за замовчуванням.")
        return COLOR_CODES['чорно-білий']

def main():
    """
    Основна функція програми, що виконує наступні кроки:
    1. Отримує текст від користувача.
    2. Дозволяє вибрати колір для ASCII-арту.
    3. Запитує ширину та вирівнювання.
    4. Генерує ASCII-арт на основі введених параметрів.
    5. Відображає попередній перегляд та надає можливість зберегти результат.

    Викликає:
        generate_ascii_art(): Для створення ASCII-арту.
        preview_ascii_art(): Для відображення попереднього перегляду.
        save_ascii_art(): Для збереження результату в файл.
    """
    # 1. Отримуємо текст від користувача
    text = input("Введіть текст для ASCII-арту: ").strip()

    # 2. Вибираємо колір
    color = choose_color_option()

    # 3. Вибираємо символи для генерації
    symbols = ('@', '#', '*')

    # 4. Вводимо розміри арт-об'єкта
    width = int(input("Введіть ширину арт-об'єкта: "))
    height = 5  # Зафіксована висота (оскільки шрифт фіксований)

    # 5. Вибір вирівнювання
    print("Варіанти вирівнювання: ліворуч, по центру, праворуч.")
    alignment = input("Виберіть вирівнювання: ").strip().lower()

    # 6. Генеруємо ASCII-арт
    art = generate_ascii_art(text, alignment, width, height, symbols, color)

    # 7. Попередній перегляд
    if art:
        preview_ascii_art(art)

        # 8. Збереження у файл
        save_option = input("Бажаєте зберегти ASCII-арт у файл? (так/ні): ").strip().lower()
        if save_option == 'так':
            save_ascii_art(art)

if __name__ == "__main__":
    main()
