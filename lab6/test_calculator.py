"""
Модуль тестів для калькулятора, який перевіряє коректність виконання математичних операцій: додавання, віднімання, множення, ділення, а також обробку помилок.

Завдання:
- Тестування основних математичних операцій калькулятора: додавання, віднімання, множення, ділення.
- Перевірка обробки помилок, таких як ділення на нуль і спроба обчислення квадратного кореня з від'ємного числа.

Клас:
- `TestCalculator`: клас тестів для калькулятора, що використовує бібліотеку `unittest` для проведення тестування.

Методи:
- `setUp(self)`: ініціалізує калькулятор перед кожним тестом.
- `test_addition(self)`: перевіряє правильність виконання операції додавання для різних варіантів чисел.
- `test_subtraction(self)`: перевіряє правильність виконання операції віднімання для різних варіантів чисел.
- `test_multiplication(self)`: перевіряє правильність виконання операції множення для різних варіантів чисел.
- `test_division(self)`: перевіряє правильність виконання операції ділення, зокрема перевірку ділення на нуль.
- `test_error_handling(self)`: перевіряє правильність обробки помилок при спробі виконати некоректні операції.

Програма використовує методи класу `unittest.TestCase` для виконання та перевірки результатів тестів. Тести перевіряють як коректні операції, так і ситуації, де можуть виникати помилки, гарантуючи правильну роботу калькулятора.
"""
import unittest
from lab6.main import Calculator  # Замінили на правильний шлях до main.py

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    # Завдання 1: Тестування Додавання
    def test_addition(self):
        self.calculator.num1 = 5
        self.calculator.num2 = 3
        self.calculator.operator = '+'
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, 8)

        self.calculator.num1 = -5
        self.calculator.num2 = -3
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, -8)

        self.calculator.num1 = -5
        self.calculator.num2 = 3
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, -2)

    # Завдання 2: Тестування Віднімання
    def test_subtraction(self):
        self.calculator.num1 = 5
        self.calculator.num2 = 3
        self.calculator.operator = '-'
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, 2)

        self.calculator.num1 = 3
        self.calculator.num2 = 5
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, -2)

        self.calculator.num1 = -5
        self.calculator.num2 = -3
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, -2)

    # Завдання 3: Тестування Множення
    def test_multiplication(self):
        self.calculator.num1 = 5
        self.calculator.num2 = 3
        self.calculator.operator = '*'
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, 15)

        self.calculator.num1 = 0
        self.calculator.num2 = 5
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, 0)

        self.calculator.num1 = -5
        self.calculator.num2 = 3
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, -15)

    # Завдання 4: Тестування Ділення
    def test_division(self):
        self.calculator.num1 = 6
        self.calculator.num2 = 3
        self.calculator.operator = '/'
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, 2)

        self.calculator.num1 = 5
        self.calculator.num2 = 0
        self.calculator.calculate()
        self.assertFalse(self.calculator.calculate())  # Перевіряємо, що повертається False

    # Завдання 5: Тестування Обробки Помилок
    def test_error_handling(self):
        self.calculator.num1 = -1
        self.calculator.operator = '√'
        self.assertFalse(self.calculator.calculate())  # Перевіряємо, що повертається False

        self.calculator.num1 = 5
        self.calculator.num2 = 0
        self.calculator.operator = '/'
        self.assertFalse(self.calculator.calculate())  # Перевіряємо, що повертається False

if __name__ == "__main__":
    unittest.main()
