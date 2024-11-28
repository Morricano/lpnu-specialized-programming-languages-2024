"""
Модуль для візуалізації даних з використанням різних типів графіків.

Клас `Visualizer` надає можливість відображення різних типів графіків, таких як:
- Лінійний графік
- Стовпчиковий графік
- Діаграма розсіювання
- Секторний графік

Методи:
- `display_line_chart(self, x_column, y_column, save_as=None)`: Відображає лінійний графік для вказаних стовпців.
- `display_bar_chart(self, x_column, y_column, save_as=None)`: Відображає стовпчиковий графік для вказаних стовпців.
- `display_scatter_plot(self, x_column, y_column, save_as=None)`: Відображає діаграму розсіювання для вказаних стовпців.
- `display_pie_chart(self, column, save_as=None)`: Відображає секторний графік для вказаного стовпця.
- `compare_charts(self, chart_type, x_column, y_column1, y_column2)`: Порівнює два графіки поруч для візуалізації різних наборів даних.
"""

from .visualizations import LineChart, BarChart, ScatterPlot, PieChart
import matplotlib.pyplot as plt

class Visualizer:
    """
    Клас для візуалізації даних за допомогою різних типів графіків.

    Атрибути:
    - `data`: Дані, які передаються для візуалізації.

    Методи:
    - `display_line_chart(self, x_column, y_column, save_as=None)`: Відображає лінійний графік для заданих стовпців.
    - `display_bar_chart(self, x_column, y_column, save_as=None)`: Відображає стовпчиковий графік для заданих стовпців.
    - `display_scatter_plot(self, x_column, y_column, save_as=None)`: Відображає діаграму розсіювання для заданих стовпців.
    - `display_pie_chart(self, column, save_as=None)`: Відображає секторний графік для заданого стовпця.
    - `compare_charts(self, chart_type, x_column, y_column1, y_column2)`: Порівнює два графіки поруч для порівняння даних.
    """

    def __init__(self, data):
        """
        Ініціалізує клас Visualizer.

        Параметри:
        - `data`: Дані, які будуть використовуватися для візуалізації.
        """
        self.data = data

    def display_line_chart(self, x_column, y_column, save_as=None):
        """
        Відображає лінійний графік для заданих стовпців.

        Параметри:
        - `x_column`: Стовпець для осі X.
        - `y_column`: Стовпець для осі Y.
        - `save_as`: Ім'я файлу для збереження графіка (необов'язковий параметр).
        """
        chart = LineChart(self.data)
        chart.plot(x_column, y_column, save_as=save_as)

    def display_bar_chart(self, x_column, y_column, save_as=None):
        """
        Відображає стовпчиковий графік для заданих стовпців.

        Параметри:
        - `x_column`: Стовпець для осі X.
        - `y_column`: Стовпець для осі Y.
        - `save_as`: Ім'я файлу для збереження графіка (необов'язковий параметр).
        """
        chart = BarChart(self.data)
        chart.plot(x_column, y_column, save_as=save_as)

    def display_scatter_plot(self, x_column, y_column, save_as=None):
        """
        Відображає діаграму розсіювання для заданих стовпців.

        Параметри:
        - `x_column`: Стовпець для осі X.
        - `y_column`: Стовпець для осі Y.
        - `save_as`: Ім'я файлу для збереження графіка (необов'язковий параметр).
        """
        chart = ScatterPlot(self.data)
        chart.plot(x_column, y_column, save_as=save_as)

    def display_pie_chart(self, column, save_as=None):
        """
        Відображає секторний графік для заданого стовпця.

        Параметри:
        - `column`: Стовпець для створення секторного графіка.
        - `save_as`: Ім'я файлу для збереження графіка (необов'язковий параметр).
        """
        chart = PieChart(self.data)
        chart.plot(column, save_as=save_as)

    def compare_charts(self, chart_type, x_column, y_column1, y_column2):
        """
        Відображає два графіки поруч для порівняння двох наборів даних.

        Параметри:
        - `chart_type`: Тип графіка для порівняння ('scatter' або 'line').
        - `x_column`: Стовпець для осі X.
        - `y_column1`: Перший стовпець для осі Y.
        - `y_column2`: Другий стовпець для осі Y.
        """
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))

        if chart_type == 'scatter':
            axes[0].scatter(self.data[x_column], self.data[y_column1], color='blue')
            axes[0].set_title(f'Діаграма розсіювання: {y_column1} vs {x_column}')
            axes[0].set_xlabel(x_column)
            axes[0].set_ylabel(y_column1)

            axes[1].scatter(self.data[x_column], self.data[y_column2], color='green')
            axes[1].set_title(f'Діаграма розсіювання: {y_column2} vs {x_column}')
            axes[1].set_xlabel(x_column)
            axes[1].set_ylabel(y_column2)

        elif chart_type == 'line':
            axes[0].plot(self.data[x_column], self.data[y_column1], color='blue')
            axes[0].set_title(f'Лінійний графік: {y_column1} vs {x_column}')
            axes[0].set_xlabel(x_column)
            axes[0].set_ylabel(y_column1)

            axes[1].plot(self.data[x_column], self.data[y_column2], color='green')
            axes[1].set_title(f'Лінійний графік: {y_column2} vs {x_column}')
            axes[1].set_xlabel(x_column)
            axes[1].set_ylabel(y_column2)

        plt.tight_layout()
        plt.show()
