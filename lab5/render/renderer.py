from utils.color_config import ColorConfig

class Renderer:
    """
    Клас для рендерингу 3D куба та його проектування на 2D екран.

    Атрибути:
    resolution (int): Роздільна здатність екрану (розмір ASCII-арт).
    foco (float): Відстань від об'єкта до камери (фокусна відстань).
    y_distorter (float): Множник для корекції спотворення по осі Y.
    left_right (int): Зміщення куба по горизонталі.
    up_down (int): Зміщення куба по вертикалі.
    """

    def __init__(self, resolution, foco, y_distorter, left_right, up_down):
        """
        Ініціалізація рендерера для проекції куба.

        Параметри:
        resolution (int): Роздільна здатність (розмір екрану для рендерингу).
        foco (float): Фокусна відстань для коректного відображення об'єкта.
        y_distorter (float): Множник для спотворення по осі Y.
        left_right (int): Зміщення об'єкта по осі X.
        up_down (int): Зміщення об'єкта по осі Y.
        """
        try:
            self.resolution = resolution
            self.foco = foco
            self.y_distorter = y_distorter
            self.left_right = left_right
            self.up_down = up_down
        except Exception as e:
            print(f"Помилка при ініціалізації рендерера: {e}")

    def project(self, cube):
        """
        Проектує координати вершин куба на 2D площину.

        Параметри:
        cube (list): Список вершин куба, що містить координати.

        Повертає:
        list: Список проекцій вершин куба на 2D площину.
        """
        try:
            return [(round(2 * point[0] * self.foco / (self.foco + point[2])),
                     round(point[1] * self.foco / ((self.foco + point[2]) * self.y_distorter)))
                    for point in cube]
        except Exception as e:
            print(f"Помилка при проектуванні: {e}")
            return []  

    def get_lines(self, proj):
        """
        Обчислює з'єднані лінії між точками куба після проекції.

        Параметри:
        proj (list): Список проекцій точок куба на 2D площину.

        Повертає:
        list: Список ліній, що з'єднують проекції точок.
        """
        try:
            connected_points = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 4), (2, 6), 
                                (3, 5), (3, 6), (7, 6), (7, 5), (7, 4)]
            return [self.interpolate(proj[point0][0], proj[point0][1], proj[point1][0], proj[point1][1])
                    for point0, point1 in connected_points]
        except Exception as e:
            print(f"Помилка при обчисленні ліній: {e}")
            return []  

    def interpolate(self, x0, y0, x1, y1):
        """
        Обчислює лінійне інтерполювання між двома точками.

        Параметри:
        x0 (int): Координата X першої точки.
        y0 (int): Координата Y першої точки.
        x1 (int): Координата X другої точки.
        y1 (int): Координата Y другої точки.

        Повертає:
        list: Список точок, що лежать на лінії між двома точками.
        """
        try:
            alpha = (y1 - y0 + 0.001) / (x1 - x0 + 0.001)
            beta = y0 - (alpha * x0)
            if alpha > 1 or alpha < -1:
                return [((round((y - beta) / (alpha + 0.001))), y) for y in range(int(min(y1, y0)), int(max(y1, y0) + 1))]
            else:
                return [(x, (round(x * alpha + beta))) for x in range(int(min(x1, x0)), int(max(x1, x0)) + 1)]
        except Exception as e:
            print(f"Помилка при інтерполяції: {e}")
            return []
        
    def render(self, proj, lins, cube_color):
        """
        Рендерить ASCII-арт з проекцією куба і його лініями.

        Параметри:
        proj (list): Список проекцій вершин куба на 2D площину.
        lins (list): Список ліній для з'єднання проекцій.
        cube_color (str): Колір куба для виведення.

        Повертає:
        str: ASCII-арт куба.
        """
        ascii_art = []
        color_code = ColorConfig.get_color_code(cube_color)
        reset_code = ColorConfig.COLORS["Reset"]

        for j in range(self.resolution):
            line = ""
            for i in range(self.resolution * 3):
                if (i - self.resolution * self.left_right, 
                    j - self.resolution * self.up_down) in proj:
                    line += f"{color_code}#{reset_code}"
                elif any((i - self.resolution * self.left_right, 
                          j - self.resolution * self.up_down) in lin for lin in lins):
                    line += f"{color_code}*{reset_code}"
                else:
                    line += " "
            ascii_art.append(line)
            print(line)
        return "\n".join(ascii_art)
