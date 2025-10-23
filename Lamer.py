import numpy as np
import matplotlib.pyplot as plt

# Настройки для LaTeX
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

# Определяем вашу функцию: uₜ₊₁ = r · uₜ² · e^(–uₜ)
def f(x, r):
    return r * x**2 * np.exp(-x)

# Параметры
x_min, x_max = 0, 5
x = np.linspace(x_min, x_max, 400)

# Выбираем значение параметра r (можно изменить)
r_value = 6.0  # Пример значения параметра

plt.figure(figsize=(10, 10))
# Рисуем график функции с LaTeX формулой
plt.plot(x, f(x, r_value), color='black',
         label=rf'$f(u) = {r_value} \cdot u^2 \cdot e^{{-u}}$')
# Рисуем линию y=x
plt.plot(x, x, color='black', label=r'$u_{t+1} = u_t$', linestyle='--')

x0 = 1.23  # Начальная точка
iterations = 10  # Количество итераций

# Инициализируем списки для диаграммы паутины
x_vals = [x0]
y_vals = [0]

# Генерируем точки для диаграммы паутины
for _ in range(iterations):
    y = f(x_vals[-1], r_value)
    # Вертикальная линия: от (x, x) до (x, y)
    plt.plot([x_vals[-1], x_vals[-1]], [x_vals[-1], y], color='red', linewidth=0.8)
    # Горизонтальная линия: от (x, y) до (y, y)
    plt.plot([x_vals[-1], y], [y, y], color='red', linewidth=0.8)
    x_vals.append(y)

# Устанавливаем пределы графика
plt.xlim(x_min, x_max)
plt.ylim(x_min, x_max)

# Добавляем метки и заголовок с LaTeX
plt.xlabel(r'$u_t$')
plt.ylabel(r'$u_{t+1}$')
plt.title(r'Диаграмма паутины: $u_{t+1} = r \cdot u_t^2 \cdot e^{-u_t}$')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()