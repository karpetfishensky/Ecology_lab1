import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Настройки для LaTeX
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12


def f(x, r):
    return r * x ** 2 * np.exp(-x)


def f_3(x, r):
    return f(f(f(x, r), r), r)


# Автоматический подбор параметров
def find_best_parameters():
    """Автоматический поиск наилучших параметров для демонстрации"""

    best_r = None
    max_crossings = 0

    # Перебираем значения r с более мелким шагом
    # Теперь шаг: (20-1)/1000 = 0.019 (вместо 0.19)
    for r in np.linspace(1, 20, 10000):
        x_range = np.linspace(0.1, 5, 1000)
        f3_values = f(f(f(x_range, r), r), r)

        # Считаем пересечения f³(x) с y=x
        crossings = 0
        for i in range(len(x_range) - 1):
            if (f3_values[i] - x_range[i]) * (f3_values[i + 1] - x_range[i + 1]) < 0:
                crossings += 1

        if crossings > max_crossings:
            max_crossings = crossings
            best_r = r

    # Форматируем r с двумя знаками после запятой
    formatted_r = f"{best_r:.2f}"
    print(f"Лучшее r для демонстрации: {formatted_r}")
    print(f"Количество пересечений f³(x) с y=x: {max_crossings}")

    # Находим хорошее начальное x (одна из точек цикла)
    if best_r is not None:
        x_range = np.linspace(0.1, 5, 1000)
        f3_values = f(f(f(x_range, best_r), best_r), best_r)

        # Ищем точку пересечения
        for i in range(len(x_range) - 1):
            if (f3_values[i] - x_range[i]) * (f3_values[i + 1] - x_range[i + 1]) < 0:
                good_x = (x_range[i] + x_range[i + 1]) / 2
                # Проверяем, что это не неподвижная точка
                if abs(f(good_x, best_r) - good_x) > 0.1:
                    print(f"Хорошее начальное x: {good_x:.2f}")
                    return best_r, good_x, formatted_r

    return best_r, 1.0, formatted_r


def find_intersection_points(r, x_min=0, x_max=4, num_points=10000):
    """Находит точки пересечения f³(x) и y=x"""
    x_values = np.linspace(x_min, x_max, num_points)
    f3_values = f_3(x_values, r)

    # Находим точки пересечения
    intersection_points = []
    for i in range(len(x_values) - 1):
        if (f3_values[i] - x_values[i]) * (f3_values[i + 1] - x_values[i + 1]) < 0:
            # Линейная интерполяция для более точного определения точки пересечения
            x1, x2 = x_values[i], x_values[i + 1]
            y1, y2 = f3_values[i] - x_values[i], f3_values[i + 1] - x_values[i + 1]

            # Решаем линейное уравнение для нахождения точки пересечения
            if y2 != y1:  # Избегаем деления на ноль
                x_intersect = x1 - y1 * (x2 - x1) / (y2 - y1)
                y_intersect = f_3(x_intersect, r)

                # Проверяем, что это не тривиальная неподвижная точка
                if abs(f(x_intersect, r) - x_intersect) > 0.01:
                    intersection_points.append((x_intersect, y_intersect))

    return intersection_points


# Parameters
r, x_initial, formatted_r = find_best_parameters()
print(f"Используемые параметры: r={formatted_r}, x_initial={x_initial}")

# Находим точки пересечения
intersections = find_intersection_points(r)
print(f"Найдено точек пересечения: {len(intersections)}")

# Выводим координаты точек пересечения
print("Координаты точек пересечения f³(x) и y=x:")
for i, (x, y) in enumerate(intersections):
    print(f"Точка {i + 1}: x = {x:.4f}, y = {y:.4f}")

# Generate x values for the plot
x_values = np.linspace(0, 4, 1000)
y_values = f_3(x_values, r)

plt.figure(figsize=(10, 8))
plt.plot(x_values, y_values, label=r'$f^3(u)$', color='blue')
plt.plot(x_values, x_values, label=r'$u_{t+3} = u_t$', color='green', linestyle='--')

# Labels and title with LaTeX and formatted r
plt.xlabel(r'$u_t$')
plt.ylabel(r'$f^3(u_t)$')
plt.title(r'График третьей итерации: $f^3(u)$ при $r=' + formatted_r + r'$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()