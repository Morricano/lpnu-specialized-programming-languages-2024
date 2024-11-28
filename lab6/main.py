"""
Програма калькулятора для виконання базових математичних операцій, таких як додавання, віднімання, множення, ділення, піднесення до степеня, обчислення квадратного кореня та залишку від ділення.

Основні функції:
- Виконання математичних операцій над двома числами або одним числом для квадратного кореня.
- Перевірка введених операторів та чисел.
- Виведення результату обчислення.
- Запит на повторення обчислення.

Клас:
- `Calculator`: основний клас калькулятора, що надає методи для отримання введення користувача, перевірки операторів, обчислення результату та виведення результату.

Методи:
- `__init__(self)`: ініціалізує калькулятор з початковим результатом 0.
- `get_user_input(self)`: запитує у користувача введення чисел та оператора. Повертає False, якщо введено некоректне значення.
- `check_operator(self)`: перевіряє, чи є введений оператор допустимим. Повертає True або False.
- `calculate(self)`: виконує обчислення на основі введених чисел та оператора.
- `display_result(self)`: виводить результат обчислення.
- `ask_for_repeat(self)`: запитує користувача, чи хоче він виконати ще одне обчислення. Повертає True або False.
- `run(self)`: основний цикл програми, що дозволяє користувачу виконувати обчислення до тих пір, поки він не вибере завершити роботу.

Програма автоматично виконує обчислення та дає користувачу можливість виконати додаткові обчислення або завершити роботу.

Якщо виконати програму без помилок, вона буде пропонувати користувачу ввести нові числа та оператори до моменту, поки користувач не вирішить завершити роботу.
"""
import math

class Calculator:
    def __init__(self):
        self.result = 0

    def get_user_input(self):
        try:
            self.num1 = float(input("Введіть перше число: "))
            self.operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
            if self.operator != "√":  # Для квадратного кореня потрібно тільки одне число
                self.num2 = float(input("Введіть друге число: "))
        except ValueError:
            print("Помилка: введіть дійсне число.")
            return False
        return True

    def check_operator(self):
        if self.operator in ['+', '-', '*', '/', '^', '√', '%']:
            return True
        else:
            print("Помилка: недійсний оператор.")
            return False

    def calculate(self):
        try:
            if self.operator == '+':
                self.result = self.num1 + self.num2
            elif self.operator == '-':
                self.result = self.num1 - self.num2
            elif self.operator == '*':
                self.result = self.num1 * self.num2
            elif self.operator == '/':
                if self.num2 == 0:
                    print("Помилка: ділення на нуль.")
                    return False  # Повертаємо False, щоб вказати на помилку
                self.result = self.num1 / self.num2
            elif self.operator == '^':
                self.result = self.num1 ** self.num2
            elif self.operator == '√':
                if self.num1 < 0:
                    print("Неможливо обчислити квадратний корінь з від'ємного числа.")
                    return False  # Повертаємо False, щоб вказати на помилку
                self.result = math.sqrt(self.num1)
            elif self.operator == '%':
                self.result = self.num1 % self.num2
        except Exception as e:
            print(f"Виникла помилка: {e}")
            return False
        return True

    def display_result(self):
        print(f"Результат: {self.result}")

    def ask_for_repeat(self):
        repeat = input("Бажаєте виконати ще одне обчислення? (так/ні): ").strip().lower()
        return repeat == 'так'

    def run(self):
        while True:
            if not self.get_user_input():
                continue
            if not self.check_operator():
                continue
            if not self.calculate():
                continue
            self.display_result()
            if not self.ask_for_repeat():
                print("Дякую за використання калькулятора!")
                break

if __name__ == "__main__":
    # Створюємо об'єкт калькулятора та запускаємо його
    calculator = Calculator()
    calculator.run()
