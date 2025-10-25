import numpy as np
import matplotlib.pyplot as plt

# Настройки для LaTeX
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12


def f_with_delay(u_current, u_previous, r):
    """Функция системы с запаздыванием: uₜ₊₁ = r · uₜ² · e^(–uₜ₋₁)"""
    return r * u_current ** 2 * np.exp(-u_previous)


# Параметры
r_min, r_max = 2, 15
num_r = 5000
num_skip = 500
num_draw = 200

r_values = np.linspace(r_min, r_max, num_r)

plt.figure(figsize=(14, 8))

for r in r_values:
    # Инициализация с двумя начальными значениями (для системы с запаздыванием)
    u_prev = 0.1
    u_curr = 0.15

    # Пропускаем переходный процесс
    for _ in range(num_skip):
        u_next = f_with_delay(u_curr, u_prev, r)
        u_prev, u_curr = u_curr, u_next

    # Запоминаем точки для отображения
    points_to_draw = []
    for _ in range(num_draw):
        u_next = f_with_delay(u_curr, u_prev, r)
        points_to_draw.append(u_next)
        u_prev, u_curr = u_curr, u_next

    plt.plot([r] * len(points_to_draw), points_to_draw, ',k', alpha=0.2, markersize=0.5)

plt.xlabel(r'Параметр $r$')
plt.ylabel(r'$u_t$')
plt.title(r'Бифуркационная диаграмма: $u_{t+1} = r \cdot u_t^2 \cdot e^{-u_{t-1}}$')
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()