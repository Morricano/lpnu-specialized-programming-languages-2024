from lab8.dal.data_handler import DataHandler
from lab8.bll.visualizer import Visualizer
from lab8.ui.display import display_data_overview

"""
Основна функція для завантаження даних, їх візуалізації та порівняння графіків.

Ця функція виконує кілька кроків:
1. Завантажує дані з файлу CSV за допомогою класу `DataHandler`.
2. Виводить первинний огляд даних (мінімальні та максимальні значення для кожного стовпця).
3. Ініціалізує візуалізатор (`Visualizer`) з даними та створює різні візуалізації:
   - Лінійний графік для порівняння продажів.
   - Стовпчиковий графік для категорій.
   - Діаграму розсіювання для порівняння зросту та ваги.
   - Секторний графік для порівняння регіонів.
4. Порівнює два графіки розсіювання (Зріст vs Вага) та два лінійних графіки (Продажі vs Кількість).

Параметри:
- Немає параметрів, функція працює з файлами та класами, визначеними у відповідних модулях.

Повертає:
- Нічого не повертає. Всі операції виконуються за допомогою виведення на екран та збереження файлів з графіками.
"""
def main():
    filepath = 'lab8/data.csv'
    
    # Завантажуємо дані і показуємо первинний огляд
    handler = DataHandler(filepath)
    display_data_overview(handler)

    # Ініціалізуємо візуалізатор з даними
    visualizer = Visualizer(handler.data)

    # Відображаємо та зберігаємо різні візуалізації
    visualizer.display_line_chart('Date', 'Sales', save_as='line_chart_sales')
    visualizer.display_bar_chart('Category', 'Count', save_as='bar_chart_category')
    visualizer.display_scatter_plot('Height', 'Weight', save_as='scatter_plot_height_weight')
    visualizer.display_pie_chart('Region', save_as='pie_chart_region')

    # Порівнюємо два графіки розсіювання: Height vs Weight
    visualizer.compare_charts('scatter', 'Height', 'Weight', 'Height')

    # Порівнюємо два лінійних графіки: Sales vs Count
    visualizer.compare_charts('line', 'Date', 'Sales', 'Count')

if __name__ == "__main__":
    main()
