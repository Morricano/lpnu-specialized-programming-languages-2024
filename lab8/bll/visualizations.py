"""
Модуль для візуалізації даних у вигляді різних типів графіків.

Класи:
- `LineChart`: Клас для побудови лінійного графіка.
- `BarChart`: Клас для побудови стовпчикового графіка.
- `ScatterPlot`: Клас для побудови діаграми розсіювання.
- `PieChart`: Клас для побудови секторного графіка.

Методи:
- `plot(self, x_column, y_column, save_as=None)`: Побудова графіка. Параметри залежать від типу графіка.
- `export_chart(self, filename, format='png')`: Експортує побудований графік у файл (успадкований з класу `BaseVisualization`).
"""

import matplotlib.pyplot as plt
from .base_visualization import BaseVisualization

class LineChart(BaseVisualization):
    """
    Клас для побудови лінійного графіка.

    Методи:
    - `plot(self, x_column, y_column, save_as=None)`: Побудова лінійного графіка для даних із вказаних стовпців.

    Параметри:
    - `x_column`: Стовпець для осі X.
    - `y_column`: Стовпець для осі Y.
    - `save_as`: Ім'я файлу для збереження графіка (необов'язковий параметр).
    """
    def plot(self, x_column, y_column, save_as=None):
        plt.plot(self.data[x_column], self.data[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title('Лінійний графік')
        if save_as:
            self.export_chart(save_as)
        plt.show()

class BarChart(BaseVisualization):
    """
    Клас для побудови стовпчикового графіка.

    Методи:
    - `plot(self, x_column, y_column, save_as=None)`: Побудова стовпчикового графіка для даних із вказаних стовпців.

    Параметри:
    - `x_column`: Стовпець для осі X.
    - `y_column`: Стовпець для осі Y.
    - `save_as`: Ім'я файлу для збереження графіка (необов'язковий параметр).
    """
    def plot(self, x_column, y_column, save_as=None):
        plt.bar(self.data[x_column], self.data[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title('Стовпчиковий графік')
        if save_as:
            self.export_chart(save_as)
        plt.show()

class ScatterPlot(BaseVisualization):
    """
    Клас для побудови діаграми розсіювання.

    Методи:
    - `plot(self, x_column, y_column, save_as=None)`: Побудова діаграми розсіювання для даних із вказаних стовпців.

    Параметри:
    - `x_column`: Стовпець для осі X.
    - `y_column`: Стовпець для осі Y.
    - `save_as`: Ім'я файлу для збереження графіка (необов'язковий параметр).
    """
    def plot(self, x_column, y_column, save_as=None):
        plt.scatter(self.data[x_column], self.data[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title('Діаграма розсіювання')
        if save_as:
            self.export_chart(save_as)
        plt.show()

class PieChart(BaseVisualization):
    """
    Клас для побудови секторного графіка.

    Методи:
    - `plot(self, column, save_as=None)`: Побудова секторного графіка для вказаного стовпця.

    Параметри:
    - `column`: Стовпець для створення секторного графіка (значення якого будуть представлені на графіку).
    - `save_as`: Ім'я файлу для збереження графіка (необов'язковий параметр).
    """
    def plot(self, column, save_as=None):
        plt.pie(self.data[column].value_counts(), labels=self.data[column].unique(), autopct='%1.1f%%')
        plt.title('Секторний графік')
        if save_as:
            self.export_chart(save_as)
        plt.show()
